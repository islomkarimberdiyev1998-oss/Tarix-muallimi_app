#!/usr/bin/env python3
"""Tarix muallim — natijalar serveri (@Tarixustoz_bot uchun).

Faqat Python 3 standart kutubxonasi ishlatiladi (qo'shimcha o'rnatish shart emas).

Vazifasi:
  * Mini App'dan ishtirokchilar natijalarini qabul qilish va SQLite bazada saqlash;
  * umumiy reytingni berish (hamma uchun);
  * admin uchun batafsil natijalar va bot orqali ishtirokchiga xabar yuborish.

Har bir so'rov Telegram initData imzosi (BOT_TOKEN bilan HMAC) orqali tekshiriladi,
shuning uchun boshqa birov o'zini ishtirokchi yoki admin qilib ko'rsata olmaydi.

Muhit o'zgaruvchilari:
  BOT_TOKEN   — @BotFather bergan token (majburiy)
  ADMIN_IDS   — admin Telegram ID lari, vergul bilan: 123456789,987654321
  PORT        — tinglanadigan port (standart 8080)
  DB_PATH     — baza fayli (standart results.db)
  ALLOW_ORIGIN— Mini App manzili, masalan https://foydalanuvchi.github.io (standart *)

Server bot yangilanishlarini (getUpdates/webhook) o'qimaydi, faqat sendMessage chaqiradi,
shuning uchun mavjud bot kodi bilan to'qnashmaydi.
"""
import hashlib
import hmac
import json
import os
import re
import sqlite3
import threading
import time
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN_IDS = {int(x) for x in re.findall(r"\d+", os.environ.get("ADMIN_IDS", ""))}
PORT = int(os.environ.get("PORT", "8080"))
DB_PATH = os.environ.get("DB_PATH", "results.db")
ALLOW_ORIGIN = os.environ.get("ALLOW_ORIGIN", "*")
INIT_MAX_AGE = 30 * 24 * 3600  # initData 30 kungacha amal qiladi
PT_MAX = 50
TOPIC_RE = re.compile(r"^[\w\-]{1,60}$")

_lock = threading.Lock()
_db = sqlite3.connect(DB_PATH, check_same_thread=False)
_db.executescript(
    """
CREATE TABLE IF NOT EXISTS users(
  id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, username TEXT,
  photo_url TEXT, first_seen INTEGER, last_seen INTEGER);
CREATE TABLE IF NOT EXISTS points(
  user_id INTEGER, topic TEXT, title TEXT, pts REAL, updated INTEGER,
  PRIMARY KEY(user_id, topic));
CREATE TABLE IF NOT EXISTS attempts(
  id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, topic TEXT, title TEXT,
  ok INTEGER, n INTEGER, pts REAL, first INTEGER, at INTEGER);
CREATE INDEX IF NOT EXISTS att_user ON attempts(user_id, at);
"""
)
_db.commit()


def check_init_data(init_data):
    """Telegram WebApp initData imzosini tekshiradi; foydalanuvchi lug'atini qaytaradi."""
    if not BOT_TOKEN or not init_data:
        return None
    try:
        pairs = urllib.parse.parse_qsl(init_data, keep_blank_values=True, strict_parsing=True)
    except ValueError:
        return None
    data = dict(pairs)
    got = data.pop("hash", "")
    check = "\n".join(f"{k}={data[k]}" for k in sorted(data))
    secret = hmac.new(b"WebAppData", BOT_TOKEN.encode(), hashlib.sha256).digest()
    want = hmac.new(secret, check.encode(), hashlib.sha256).hexdigest()
    if not hmac.compare_digest(want, got):
        return None
    try:
        if time.time() - int(data.get("auth_date", "0")) > INIT_MAX_AGE:
            return None
        user = json.loads(data.get("user", "null"))
    except (ValueError, TypeError):
        return None
    if not isinstance(user, dict) or not isinstance(user.get("id"), int):
        return None
    return user


def _s(v, n=100):
    return v[:n] if isinstance(v, str) else None


def touch_user(u):
    now = int(time.time())
    photo = _s(u.get("photo_url"), 300)
    if photo and not photo.startswith("https://"):
        photo = None
    _db.execute(
        """INSERT INTO users(id,first_name,last_name,username,photo_url,first_seen,last_seen)
           VALUES(?,?,?,?,?,?,?)
           ON CONFLICT(id) DO UPDATE SET first_name=excluded.first_name,last_name=excluded.last_name,
           username=excluded.username,photo_url=excluded.photo_url,last_seen=excluded.last_seen""",
        (u["id"], _s(u.get("first_name")), _s(u.get("last_name")), _s(u.get("username"), 40), photo, now, now),
    )


def valid_pts(v):
    return isinstance(v, (int, float)) and 0 <= v <= PT_MAX


def save_points(uid, topic, title, pts):
    # Reytingga faqat birinchi urinish yoziladi; u test davomida faqat o'sadi -> eng kattasi saqlanadi.
    _db.execute(
        """INSERT INTO points(user_id,topic,title,pts,updated) VALUES(?,?,?,?,?)
           ON CONFLICT(user_id,topic) DO UPDATE SET title=excluded.title,
           pts=MAX(points.pts,excluded.pts),updated=excluded.updated""",
        (uid, topic, _s(title, 200), round(float(pts), 1), int(time.time())),
    )


def name_of(r):
    return " ".join(x for x in (r["first_name"], r["last_name"]) if x) or "Ishtirokchi"


def leaderboard(limit=None):
    _db.row_factory = sqlite3.Row
    rows = _db.execute(
        """SELECT u.*, COALESCE(SUM(p.pts),0) AS total, COUNT(p.topic) AS topics
           FROM users u LEFT JOIN points p ON p.user_id=u.id
           GROUP BY u.id ORDER BY total DESC, u.first_seen ASC"""
    ).fetchall()
    _db.row_factory = None
    return rows[:limit] if limit else rows


def send_message(chat_id, text):
    body = json.dumps({"chat_id": chat_id, "text": text}).encode()
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data=body,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        try:
            return json.load(e)
        except ValueError:
            return {"ok": False, "description": f"HTTP {e.code}"}
    except OSError:
        return {"ok": False, "description": "network"}


class H(BaseHTTPRequestHandler):
    server_version = "TarixMuallim/1"

    def log_message(self, fmt, *a):  # tokenni yoki initData ni logga yozmaslik
        pass

    def _send(self, code, obj):
        b = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(b)))
        self.send_header("Access-Control-Allow-Origin", ALLOW_ORIGIN)
        self.send_header("Vary", "Origin")
        self.end_headers()
        self.wfile.write(b)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", ALLOW_ORIGIN)
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Authorization, Content-Type")
        self.send_header("Access-Control-Max-Age", "86400")
        self.end_headers()

    def _auth(self):
        a = self.headers.get("Authorization", "")
        return check_init_data(a[4:]) if a.startswith("tma ") else None

    def _body(self):
        n = int(self.headers.get("Content-Length") or 0)
        if n > 200_000:
            return None
        try:
            return json.loads(self.rfile.read(n) or b"{}")
        except ValueError:
            return None

    def do_GET(self):
        self._route("GET")

    def do_POST(self):
        self._route("POST")

    def _route(self, method):
        u = urllib.parse.urlparse(self.path)
        if u.path == "/health":
            return self._send(200, {"ok": True})
        user = self._auth()
        if not user:
            return self._send(401, {"error": "auth"})
        uid = user["id"]
        admin = uid in ADMIN_IDS
        body = self._body() if method == "POST" else {}
        if body is None or not isinstance(body, dict):
            return self._send(400, {"error": "body"})
        q = urllib.parse.parse_qs(u.query)
        with _lock:
            try:
                return self._handle(method, u.path, uid, user, admin, body, q)
            finally:
                _db.commit()

    def _handle(self, method, path, uid, user, admin, body, q):
        if method == "POST" and path == "/api/sync":
            touch_user(user)
            for it in (body.get("items") or [])[:3000]:
                if (isinstance(it, list) and len(it) == 3 and isinstance(it[0], str)
                        and TOPIC_RE.match(it[0]) and valid_pts(it[2])):
                    save_points(uid, it[0], it[1], it[2])
            return self._send(200, {"ok": True, "admin": admin})

        if method == "POST" and path == "/api/result":
            touch_user(user)
            t, ok, n, pts = body.get("id"), body.get("ok"), body.get("n"), body.get("pts")
            if not (isinstance(t, str) and TOPIC_RE.match(t) and isinstance(ok, int) and isinstance(n, int)
                    and 0 <= ok <= n <= 1000 and valid_pts(pts)):
                return self._send(400, {"error": "data"})
            first = 1 if body.get("first") else 0
            _db.execute(
                "INSERT INTO attempts(user_id,topic,title,ok,n,pts,first,at) VALUES(?,?,?,?,?,?,?,?)",
                (uid, t, _s(body.get("title"), 200), ok, n, round(float(pts), 1), first, int(time.time())),
            )
            if first:
                save_points(uid, t, body.get("title"), pts)
            return self._send(200, {"ok": True})

        if method == "GET" and path == "/api/top":
            rows = leaderboard()
            me = next((i for i, r in enumerate(rows) if r["id"] == uid), None)
            top = [{"name": name_of(r), "username": r["username"], "photo": r["photo_url"],
                    "pts": round(r["total"], 1), "topics": r["topics"], "me": r["id"] == uid}
                   for r in rows[:100] if r["total"] > 0]
            return self._send(200, {
                "top": top, "count": sum(1 for r in rows if r["total"] > 0),
                "me": None if me is None else {"rank": me + 1, "pts": round(rows[me]["total"], 1)},
            })

        if not admin:
            return self._send(403, {"error": "admin"})

        if method == "GET" and path == "/api/admin/users":
            _db.row_factory = sqlite3.Row
            att = {r["user_id"]: (r["c"], r["last"]) for r in _db.execute(
                "SELECT user_id, COUNT(*) c, MAX(at) last FROM attempts GROUP BY user_id")}
            _db.row_factory = None
            users = [{"id": r["id"], "name": name_of(r), "username": r["username"], "photo": r["photo_url"],
                      "pts": round(r["total"], 1), "topics": r["topics"],
                      "attempts": att.get(r["id"], (0, None))[0],
                      "last": max(r["last_seen"] or 0, att.get(r["id"], (0, 0))[1] or 0)}
                     for r in leaderboard()]
            return self._send(200, {"users": users})

        if method == "GET" and path == "/api/admin/user":
            try:
                tid = int((q.get("id") or ["0"])[0])
            except ValueError:
                return self._send(400, {"error": "id"})
            _db.row_factory = sqlite3.Row
            u = _db.execute("SELECT * FROM users WHERE id=?", (tid,)).fetchone()
            if not u:
                _db.row_factory = None
                return self._send(404, {"error": "none"})
            pts = [dict(r) for r in _db.execute(
                "SELECT topic,title,pts,updated FROM points WHERE user_id=? ORDER BY updated DESC", (tid,))]
            att = [dict(r) for r in _db.execute(
                "SELECT topic,title,ok,n,pts,first,at FROM attempts WHERE user_id=? ORDER BY at DESC LIMIT 300",
                (tid,))]
            _db.row_factory = None
            return self._send(200, {"user": {"id": u["id"], "name": name_of(u), "username": u["username"],
                                             "photo": u["photo_url"], "first_seen": u["first_seen"],
                                             "last_seen": u["last_seen"]},
                                    "points": pts, "attempts": att})

        if method == "POST" and path == "/api/admin/msg":
            tid, text = body.get("id"), body.get("text")
            if not isinstance(tid, int) or not isinstance(text, str) or not text.strip() or len(text) > 3500:
                return self._send(400, {"error": "data"})
            r = send_message(tid, text.strip())
            return self._send(200, {"ok": bool(r.get("ok")), "error": r.get("description")})

        return self._send(404, {"error": "path"})


def main():
    if not BOT_TOKEN:
        raise SystemExit("BOT_TOKEN muhit o'zgaruvchisini kiriting")
    if not ADMIN_IDS:
        print("Diqqat: ADMIN_IDS kiritilmagan — admin bo'limi hech kimga ochilmaydi.")
    print(f"Natijalar serveri: port {PORT}, baza {DB_PATH}")
    ThreadingHTTPServer(("0.0.0.0", PORT), H).serve_forever()


if __name__ == "__main__":
    main()
