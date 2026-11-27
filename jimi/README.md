# Jimi — savollar tuzish namunasi

"Jimi" — Tarix muallim ilovasi uchun darslik matnidan test savollari tuzishning
kelishilgan namunasi. Foydalanuvchi "Jimi bo'yicha tuzing" desa, quyidagi qoidalar
to'liq qo'llanadi.

## Asosiy qoidalar
1. **Faqat berilgan matn.** Har bir savol, javob, xarita joyi va izoh foydalanuvchi
   yuborgan darslik matnidan olinadi. Matnda yo'q fakt, sana yoki joy ishlatilmaydi.
   Agar xaritada belgilash uchun joy matnda bo'lmasa — savol boshqa joy bilan
   yoki MAPN turida tuziladi.
2. **Har bir mavzu alohida test.** Mavzu id: `e{sinf}{j|u}{raqam}` (masalan `e10j5`,
   `e8u12`); birlashtirilgan mavzular `e10j7-8`.
3. **100 ballik tizim.** Ball ilovada avtomatik hisoblanadi (to'g'ri javoblar ulushi × 100).
4. **To'g'ri javob har doim birinchi yoziladi** (`c: 0`), ilova variantlarni o'zi aralashtiradi.
5. **Izoh (`e`)** — to'g'ri javobni matndan qisqa asoslaydi.

## Bir mavzudagi savollar tarkibi (o'rtacha ~22 ta)
| Tur | Metod | Soni | Izoh |
|---|---|---|---|
| Oddiy savol | `B` | 12–18 | sana, shaxs, joy, atama, sabab |
| Voqea natijasi | `NAT` | 2–4 | "Voqea → natijasi nima bo'ldi?" |
| To'g'ri / noto'g'ri | `TF` | 2 | biri to'g'ri, biri noto'g'ri |
| 4 ta hukm (T/N) | `TF4` | 1 | bitta testda 4 ta voqea/hukm, har biriga T yoki N; javob «1-T, 2-N, 3-T, 4-N» |
| I–II–III mulohaza | `MUL` | 1 | 3 ta mulohaza, kamida bittasi noto'g'ri |
| Xronologiya | `CHR` | 1 | 4–6 voqea (kamida 3), sanalar matnda bo'lishi shart |
| Eyler–Venn | `VENN` | 1 | 2 tushuncha, 5–6 belgi; I, II, III guruhlarning har biri bo'sh emas |
| Xarita | `MAPMATCH` / `MAPN` / `MAP1` | 1–2 | joylar 1–4 raqamlar bilan belgilanadi |
| Moslashtirish | `MATCH` | 0–2 | shaxs ↔ ish, sana ↔ voqea va h.k. |

Murakkab turlar (MUL, MATCH, CHR, VENN) uchun vaqt ko'proq beriladi (`t`: 40–45 s).

## Xaritalar
- `map_svg` orqali 600×470 SVG yaratiladi (`img/q/<id>-mapN.svg`), dunyo xaritasi
  `mapgen/map.mjs` (d3-geo + world-atlas) bilan chiziladi.
- Hududlar `REG` lug'atida (`europe`, `globe`, `eastasia`, `latam`, ...), joylar `PLACES` da.
- `asia`, `africa`, `namerica`, `samerica` — foydalanuvchi yuborgan rasm xaritalar
  (`cal/*.jpg`, kalibrlash `cal/*_coef.json`).
- Raqamlar ustma-ust tushmasligi shart: `python3 jimi/ovl.py 'img/q/<prefiks>*.svg'` → `[]`.

## Ish tartibi
1. Darslik (docx) matnini mavzularga ajratish.
2. `jimi/mavzular/<modul>.py` da har mavzu uchun `Topic('id', seed)` va savollar
   (namuna: `jimi/mavzular/mj10_1.py`).
3. `questions2.json` da mavzular ro'yxati (id, title, bo'sh `questions`) bo'lishi kerak.
4. Joylash: `python3 jimi/build.py eski 10 jahon <chiqish.md> mj10_1 mj10_2 ...`
5. Tekshirish:
   - `python3 jimi/ovl.py 'img/q/e10j*.svg'` — xaritalarda ustma-ust raqam yo'q;
   - `node jimi/t20.js <papka> 0 <mavzular_soni> '<Kitob nomi>'` — barcha mavzular
     brauzerda yechiladi: rasmlar yuklanadi, xato yo'q, ball to'g'ri.
6. `.md` ro'yxatni foydalanuvchiga yuborish, commit, push, PR.

## O'rnatish (yangi muhitda)
```
cd jimi/mapgen && npm install    # d3-geo, topojson-client, world-atlas
pip install pillow numpy         # rasm xaritalar uchun
```
