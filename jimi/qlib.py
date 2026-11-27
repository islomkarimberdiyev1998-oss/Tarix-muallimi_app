import random, itertools, os
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # repo ildizi
os.makedirs(REPO + '/img/q', exist_ok=True)
T_ = 'To‘g‘ri'; N_ = 'Noto‘g‘ri'
ROM = ['I', 'II', 'III', 'IV', 'V']

class Topic:
    def __init__(self, tid, seed):
        self.tid, self.Q, self.R, self.nv = tid, [], random.Random(seed), 0

    def B(self, q, ok, w1, w2, w3, e):
        assert len({ok, w1, w2, w3}) == 4, q
        self.Q.append({'q': q, 'a': [ok, w1, w2, w3], 'c': 0, 'e': e})

    def TF(self, s, val, e):
        self.Q.append({'q': 'Mulohaza to‘g‘rimi yoki noto‘g‘rimi?\n' + s, 'a': [T_, N_], 'c': 0 if val else 1, 'e': e})

    def MUL(self, items, e):
        f = lambda bits: '; '.join(f'{ROM[i]}-{T_ if b else N_}' for i, b in enumerate(bits))
        cor = tuple(v for _, v in items)
        others = [b for b in itertools.product([True, False], repeat=len(items)) if b != cor]
        opts = [f(cor)] + [f(b) for b in self.R.sample(others, 3)]
        q = 'Mulohazalarni tahlil qiling.\n' + '\n'.join(f'{ROM[i]}. {t}' for i, (t, _) in enumerate(items))
        self.Q.append({'q': q, 'a': opts, 'c': 0, 'e': e, 't': 40})

    def MATCH(self, title, left, right, ans, e):
        letters = 'abcdefg'[:len(right)]
        assert len(ans) == len(left) and len(set(ans)) == len(ans) and set(ans) <= set(letters)
        f = lambda s: ', '.join(f'{i+1}-{c}' for i, c in enumerate(s))
        seen = {ans}; opts = [f(ans)]
        while len(opts) < 4:
            s = ''.join(self.R.sample(letters, len(left)))
            if s not in seen:
                seen.add(s); opts.append(f(s))
        q = title + '\n' + '\n'.join(f'{i+1}. {t}' for i, t in enumerate(left)) + '\n\n' + '\n'.join(f'{letters[i]}) {t}' for i, t in enumerate(right))
        self.Q.append({'q': q, 'a': opts, 'c': 0, 'e': e, 't': 40})

    def CHR(self, title, items, e):
        n = len(items)
        while True:
            perm = self.R.sample(range(n), n)
            if perm != list(range(n)):
                break
        disp = [items[p] for p in perm]
        cor = tuple(perm.index(i) + 1 for i in range(n))
        f = lambda t: ', '.join(map(str, t))
        allp = [p for p in itertools.permutations(range(1, n + 1)) if p != cor]
        opts = [f(cor)] + [f(p) for p in self.R.sample(allp, 3)]
        q = title + '\n' + '\n'.join(f'{k+1}) {t}' for k, t in enumerate(disp))
        self.Q.append({'q': q, 'a': opts, 'c': 0, 'e': e, 't': 40})

    def VENN(self, l1, l2, items, e):
        letters = 'abcdefghij'
        def f(groups):
            parts = []
            for g in (1, 2, 3):
                ls = [letters[i] for i, x in enumerate(groups) if x == g]
                parts.append(f'{ROM[g-1]}-' + (', '.join(ls) if ls else 'yo‘q'))
            return '; '.join(parts)
        cor = tuple(g for _, g in items)
        seen = {cor}; opts = [f(cor)]
        while len(opts) < 4:
            g = list(cor)
            for i in self.R.sample(range(len(g)), self.R.choice([2, 3])):
                g[i] = self.R.choice([1, 2, 3])
            g = tuple(g)
            if g not in seen and all(k in g for k in (1, 2, 3)):
                seen.add(g); opts.append(f(g))
        self.nv += 1
        name = f'{self.tid}-venn{self.nv}'
        venn_svg(name, l1, l2)
        q = 'Eyler–Venn diagrammasiga ko‘ra ma’lumotlar to‘g‘ri guruhlangan javobni aniqlang.\n' + '\n'.join(f'{letters[i]}) {t}' for i, (t, _) in enumerate(items))
        self.Q.append({'q': q, 'a': opts, 'c': 0, 'e': e, 't': 45, 'img': f'img/q/{name}.svg'})

def venn_svg(name, a, b):
    fs = 24 if max(len(a), len(b)) <= 14 else 19
    open(f'{REPO}/img/q/{name}.svg', 'w', encoding='utf-8').write(f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 540 250">
<rect width="540" height="250" fill="#fff"/>
<text x="170" y="30" text-anchor="middle" font-family="Georgia,serif" font-size="{fs}" fill="#111">{a}</text>
<text x="370" y="30" text-anchor="middle" font-family="Georgia,serif" font-size="{fs}" fill="#111">{b}</text>
<clipPath id="c"><ellipse cx="200" cy="148" rx="150" ry="85"/></clipPath>
<ellipse cx="340" cy="148" rx="150" ry="85" fill="#d9d9d9" clip-path="url(#c)"/>
<g fill="none" stroke="#111" stroke-width="4"><ellipse cx="200" cy="148" rx="150" ry="85"/><ellipse cx="340" cy="148" rx="150" ry="85"/></g>
<g font-family="Georgia,serif" font-size="34" text-anchor="middle" fill="#111"><text x="125" y="160">I</text><text x="270" y="160">III</text><text x="415" y="160">II</text></g>
</svg>''')

# ---------- xarita va voqea-natija savollari ----------
import json as _json, subprocess as _sp
MAPGEN = os.path.dirname(os.path.abspath(__file__)) + '/mapgen'
REG = {  # [lon0, lat0, lon1, lat1]
    'europe': [-11, 32.5, 42, 61],
    'arabia': [31, 11, 61, 35],
    'mideast': [-10, 8, 81, 48],
    'crusade': [-6, 28, 46, 55],
    'rus': [18, 41.3, 62, 63],
    'eurasia': [-10, 30, 120, 62],
}
IMGMAPS = {  # foydalanuvchi yuborgan xaritalar: (fayl, kalibrlash)
    'asia': (os.path.dirname(os.path.abspath(__file__)) + '/cal/63d190fd-image.jpg', 'asia'),
    'africa': (os.path.dirname(os.path.abspath(__file__)) + '/cal/b764da1a-image.jpg', 'africa'),
    'namerica': (os.path.dirname(os.path.abspath(__file__)) + '/cal/ec894145-image.jpg', 'namerica'),
    'samerica': (os.path.dirname(os.path.abspath(__file__)) + '/cal/74153b09-image.jpg', 'samerica'),
}
OVR = {('namerica', 'Yukatan yarimoroli'): (468, 556), ('asia', 'Shri Lanka'): (295, 532)}
PLACES = {
    'Angliya': (-1.5, 52.6), 'London': (-0.45, 51.75), 'Galliya': (2.3, 46.8), 'Parij': (2.35, 48.85),
    'Italiya': (12.6, 42.8), 'Rim': (12.5, 41.9), 'Pireney yarimoroli': (-4.0, 40.0), 'Germaniya': (10.0, 51.0),
    'Saksoniya': (9.8, 52.6), 'Shimoliy Afrika': (9.8, 35.2), 'Konstantinopol': (28.98, 41.0),
    'Bolgariya': (25.3, 42.7), 'Chexiya': (15.2, 49.8), 'Polsha': (19.2, 52.1), 'Kiyev': (30.5, 50.45),
    'Novgorod': (31.3, 58.5), 'Daniya': (9.3, 56.1), 'Vengriya': (19.3, 47.2), 'Verden': (5.4, 49.16),
    'Axen': (6.08, 50.78), 'Lex daryosi': (10.9, 48.4), 'Kichik Osiyo': (33.0, 39.0), 'Irlandiya': (-8.0, 53.2),
    'Shotlandiya': (-4.2, 56.8), 'Ravenna': (12.2, 44.4), 'Sitsiliya': (14.2, 37.5), 'Afina': (23.7, 37.98),
    'Misr': (30.5, 27.5), 'Suriya': (38.0, 35.0),
    'Makka': (39.8, 21.4), 'Madina (Yasrib)': (39.6, 24.5), 'Yaman': (45.5, 15.3),
    'Ikki daryo oralig‘i': (44.2, 33.0), 'Falastin': (35.2, 31.7),
}

def img_map_svg(name, region, marks):
    import base64, sys as _s
    _s.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + '/cal')
    from fit import proj
    from PIL import Image
    f, cal = IMGMAPS[region]
    coef = _json.load(open(os.path.dirname(os.path.abspath(__file__)) + f'/cal/{cal}_coef.json'))
    W, H = Image.open(f).size
    k = max(W, H) / 700
    b64 = base64.b64encode(open(f, 'rb').read()).decode()
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}">',
           f'<rect width="{W}" height="{H}" fill="#fff"/><image width="{W}" height="{H}" xlink:href="data:image/jpeg;base64,{b64}"/>',
           f'<g font-family="Georgia,serif" font-weight="bold" font-size="{25*k:.0f}" text-anchor="middle">']
    for n, p in marks:
        x, y = OVR[(region, p)] if (region, p) in OVR else proj(coef, *PLACES[p])
        assert 0 < x < W and 0 < y < H, p
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{19*k:.1f}" fill="#fff" stroke="#c0392b" stroke-width="{3*k:.1f}"/><text x="{x:.1f}" y="{y+9*k:.1f}" fill="#c0392b">{n}</text>')
    out.append('</g></svg>\n')
    open(f'{REPO}/img/q/{name}.svg', 'w').write(''.join(out))

def map_svg(name, region, marks):
    if region in IMGMAPS:
        return img_map_svg(name, region, marks)
    bbox = REG[region]
    pts = [PLACES[p] for _, p in marks]
    def _mind(bb):
        sc = min(600 / (bb[2] - bb[0]), 470 / (bb[3] - bb[1]) / 1.25)
        return min([((a[0]-b[0])**2 + (a[1]-b[1])**2) ** .5 * sc for i, a in enumerate(pts) for b in pts[i+1:]] or [999])
    if len(pts) > 1 and _mind(bbox) < 46:
        lo0, lo1 = min(p[0] for p in pts), max(p[0] for p in pts)
        la0, la1 = min(p[1] for p in pts), max(p[1] for p in pts)
        pad = max(1.2, 0.3 * max(lo1 - lo0, la1 - la0))
        bbox = [max(-179, lo0 - pad), max(-80, la0 - pad), min(179, lo1 + pad), min(80, la1 + pad)]
    spec = {'out': f'{REPO}/img/q/{name}.svg', 'bbox': bbox,
            'marks': [{'n': n, 'lon': PLACES[p][0], 'lat': PLACES[p][1]} for n, p in marks]}
    fn = f'{MAPGEN}/spec.json'
    open(fn, 'w').write(_json.dumps(spec))
    _sp.run(['node', f'{MAPGEN}/map.mjs', fn], check=True)

def _map_q(self, region, marks, q, ok, w, e):
    self.nm = getattr(self, 'nm', 0) + 1
    name = f'{self.tid}-map{self.nm}'
    map_svg(name, region, marks)
    assert len({ok, *w}) == 4, q
    self.Q.append({'q': q, 'a': [ok, *w], 'c': 0, 'e': e, 't': 35, 'img': f'img/q/{name}.svg'})

def MAP1(self, region, place, q, ok, w, e):
    """Xaritada bitta joy 1 raqami bilan belgilangan."""
    _map_q(self, region, [(1, place)], 'Xaritada 1 raqami bilan belgilangan hududga oid savol.\n' + q, ok, w, e)

def MAPN(self, region, places, q, e, ask_idx=None):
    """Xaritada bir nechta joy 1..n raqamlari bilan; javob – raqam."""
    marks = [(i + 1, p) for i, p in enumerate(places)]
    k = ask_idx if ask_idx is not None else 0
    ok = f'{k+1}'
    w = [str(i + 1) for i in range(len(places)) if i != k][:3]
    _map_q(self, region, marks, 'Xaritada ' + ', '.join(str(i + 1) for i in range(len(places))) + ' raqamlari bilan hududlar belgilangan.\n' + q, ok, w, e)

def MAPMATCH(self, region, places, labels, e):
    """Raqamlar bilan belgilangan joylarni nomlari bilan moslashtirish (labels – to'g'ri tartibda)."""
    assert len(places) >= 3, 'MAPMATCH needs 3+ places'
    letters = 'abcd'[:len(places)]
    perm = self.R.sample(range(len(places)), len(places))
    shown = [labels[i] for i in perm]          # a), b), ... ko'rinish tartibi
    ans = ''.join(letters[perm.index(i)] for i in range(len(places)))
    f = lambda s: ', '.join(f'{i+1}-{c}' for i, c in enumerate(s))
    seen = {ans}; opts = [f(ans)]
    while len(opts) < 4:
        s = ''.join(self.R.sample(letters, len(places)))
        if s not in seen:
            seen.add(s); opts.append(f(s))
    marks = [(i + 1, p) for i, p in enumerate(places)]
    self.nm = getattr(self, 'nm', 0) + 1
    name = f'{self.tid}-map{self.nm}'
    map_svg(name, region, marks)
    q = 'Xaritada raqamlar bilan belgilangan hududlarni ularga oid ma’lumotlar bilan moslashtiring.\n' + '\n'.join(f'{letters[i]}) {t}' for i, t in enumerate(shown))
    self.Q.append({'q': q, 'a': opts, 'c': 0, 'e': e, 't': 45, 'img': f'img/q/{name}.svg'})

def NAT(self, event, ok, w1, w2, w3, e):
    """Voqea va uning natijasi."""
    self.B('Voqea natijasi mos keladigan variantni belgilang.\nVoqea: ' + event, ok, w1, w2, w3, e)

Topic.MAP1, Topic.MAPN, Topic.MAPMATCH, Topic.NAT = MAP1, MAPN, MAPMATCH, NAT

PLACES.update({
    'Gibraltar': (-5.35, 36.1), 'Puate': (0.34, 46.58), 'Kufa': (44.4, 32.0), 'Marv': (61.8, 37.6), 'Bag‘dod': (44.4, 33.3),
    'Kordova': (-4.78, 37.9), 'Damashq': (36.3, 33.5), 'Talas': (72.2, 42.5), 'Mo‘lton': (71.5, 30.2), 'Samarqand': (67.0, 39.65),
    'Ozarbayjon': (47.8, 39.0), 'Qohira': (31.2, 30.05), 'Buxoro': (64.4, 39.8), 'Granada': (-3.6, 37.18), 'Eron': (54.0, 32.5),
    'Pataliputra': (85.1, 25.6), 'Dehli': (77.2, 28.6), 'Kalikut': (75.8, 11.25), 'G‘azna': (68.4, 33.5), 'Ajanta': (75.7, 20.55),
    'Chanyan': (108.9, 34.3), 'Loyan': (112.45, 34.6), 'Xanchjou': (120.15, 30.25), 'Yanchjou': (119.4, 32.4), 'Pxenyan': (125.7, 39.0),
    'Pekin': (116.4, 39.9), 'Kioto': (135.8, 35.0), 'Isfahon': (51.7, 32.65), 'Gaochan': (89.2, 42.9),
    'Hindiston': (78.5, 22.5), 'Xitoy': (110.0, 31.0), 'Yaponiya': (138.5, 36.3), 'Koreya': (127.5, 36.8), 'Mo‘g‘uliston': (103.0, 46.5),
    'Venetsiya': (12.3, 45.4), 'Genuya': (8.9, 44.4), 'Florensiya': (11.25, 43.77), 'Marsel': (5.37, 43.3), 'Lyubek': (10.7, 53.87),
    'Bryugge': (3.22, 51.2), 'Shampan': (4.03, 49.0), 'Antverpen': (4.4, 51.2), 'Lion': (4.83, 45.76), 'Klermon': (3.08, 45.78),
    'Quddus': (35.23, 31.78), 'Rodos': (28.0, 36.2), 'Malta': (14.4, 35.9),
})
REG['france'] = [-6, 42, 9, 53.5]
PLACES.update({
    'Avinon': (4.8, 43.95), 'Kresi': (1.88, 50.25), 'Orlean': (1.9, 47.9), 'Reyms': (4.03, 49.25), 'Ruan': (1.1, 49.44), 'Azenkur': (2.14, 50.46),
    'Kale': (1.86, 50.95), 'Normandiya': (0.0, 49.0), 'Akvitaniya': (0.0, 44.8), 'Bretan': (-2.8, 48.1), 'Burgundiya': (4.8, 47.0),
    'Flandriya': (3.2, 50.9), 'Gastings': (0.57, 50.86), 'Milan': (9.19, 45.46), 'Lenyano': (8.92, 45.6), 'Palermo': (13.36, 38.12),
    'Neapol': (14.25, 40.85), 'Kyoln': (6.96, 50.94), 'Bove': (2.08, 49.43), 'Tuluza': (1.44, 43.6), 'Bosvort': (-1.4, 52.6), 'Provans': (6.0, 43.7),
    'Moskva': (37.6, 55.75), 'Vladimir': (40.4, 56.13), 'Lyubech': (30.65, 51.7), 'Pskov': (28.33, 57.82), 'Neva': (30.4, 59.9),
    'Chud ko‘li': (27.5, 58.7), 'Saroy Botu': (47.9, 46.6), 'Nikeya': (29.72, 40.43), 'Galich': (24.7, 49.1), 'Puate (Fransiya)': (0.34, 46.58),
})
PLACES.update({
    'Tver': (35.9, 56.86), 'Voje daryosi': (39.0, 54.2), 'Kulikovo': (38.6, 53.7), 'Kunduzcha': (50.5, 53.7), 'Tarak daryosi': (46.5, 43.6),
    'Ryazan': (39.7, 54.6), 'Kalka daryosi': (37.7, 47.5), 'Saroy Berka': (45.0, 48.6), 'Astraxan': (48.03, 46.35), 'Qrim': (34.3, 45.0), 'Qozon': (49.1, 55.8),
    'Parij (Sorbonna)': (2.35, 48.85), 'Bolonya': (11.34, 44.49), 'Oksford': (-1.26, 51.75), 'Maynts': (8.27, 50.0), 'Shartr': (1.49, 48.45),
    'Mansikert': (42.5, 39.15), 'Anqara': (32.85, 39.93), 'Bursa': (29.06, 40.18), 'Istanbul': (28.98, 41.0), 'Nikomediya': (29.92, 40.77),
    'Qoraqurum': (102.8, 47.2), 'Onon daryosi': (111.5, 49.0), 'Xorazm': (60.6, 41.5), 'Shimoliy Xitoy': (114.0, 39.0),
    'Kayfin': (114.3, 34.8), 'Chendu': (104.07, 30.67), 'Uchan': (114.3, 30.6), 'Shandun': (118.0, 36.4), 'Nankin': (118.8, 32.06),
    'Shri Lanka': (80.7, 7.8), 'Ormuz': (56.3, 27.1), 'Vyetnam': (106.0, 16.0), 'Kamakura': (139.55, 35.3), 'Nagasaki': (129.87, 32.75),
    'Sonak (Keson)': (126.55, 37.97), 'Xanson (Seul)': (126.98, 37.57), 'Panjob': (74.0, 31.0), 'Bengaliya': (88.5, 23.5), 'Sind': (68.5, 26.0),
    'Gana': (-7.97, 15.77), 'Mali (Niara)': (-8.4, 11.4), 'Gao': (-0.05, 16.27), 'Tombuktu': (-3.0, 16.8), 'Aksum': (38.7, 14.1),
    'Benin': (5.6, 6.3), 'Marokash': (-7.0, 31.6), 'Misr (Afrika)': (30.0, 26.5),
    'Yukatan yarimoroli': (-89.0, 20.5), 'Tenochtitlan': (-99.13, 19.43), 'Kusko': (-71.97, -13.53), 'And tog‘lari': (-75.5, -8.0),
})
REG.update({'uzb': [55, 35.5, 77, 46], 'egypt': [22, 18, 42, 36.5], 'world': [-20, -38, 135, 62],
            'hellas': [19, 34.5, 30.5, 42.5], 'italy': [5.5, 36, 19.5, 47.5], 'medit': [-10, 28, 45, 50]})
PLACES.update({
    'Selungur': (71.4, 40.2), 'Ko‘lbuloq': (70.0, 41.0), 'Teshiktosh': (66.5, 38.3), 'Obishir': (70.6, 40.0), 'Machay': (67.0, 38.4),
    'Zarautsoy': (67.4, 37.9), 'Zamonbobo': (64.0, 39.7), 'Sopollitepa': (67.3, 37.6), 'Jarqo‘ton': (67.0, 37.4), 'Baqtriya': (67.5, 36.8),
    'So‘g‘d': (66.3, 39.7), 'Toshkent': (69.25, 41.3), 'Farg‘ona': (71.8, 40.6), 'Avstralopitek (Janubiy Afrika)': (25.0, -26.0),
    'Zinj vodiysi': (35.35, -2.99), 'Yava oroli': (110.0, -7.5), 'Sinantrop (Xitoy)': (115.9, 39.7), 'Neandertal (Germaniya)': (6.95, 51.23),
    'Kromanyon (Fransiya)': (1.0, 44.95), 'Altamir': (-4.1, 43.4), 'Lasko': (1.17, 45.05), 'Kapova g‘ori': (57.0, 53.0),
    'Memfis': (31.25, 29.85), 'Fiva': (32.65, 25.7), 'Nubiya': (32.5, 20.5), 'Sinay yarimoroli': (33.8, 29.3), 'Liviya': (25.5, 27.5),
    'Suriya (qadimgi)': (37.5, 35.0), 'Falastin (qadimgi)': (34.9, 31.5), 'Nil deltasi': (31.0, 30.9), 'Rozett': (30.4, 31.4),
    'Behistun': (47.43, 34.39), 'Kirmonshoh': (47.06, 34.31), 'Xettlar (Kichik Osiyo)': (34.0, 39.5), 'Maykop': (40.1, 44.6),
})
REG.update({'mesop': [38.5, 29.0, 53.5, 39.5]})
PLACES.update({
    'Ur': (46.1, 30.96), 'Uruk': (45.64, 31.32), 'Lagash': (46.4, 31.4), 'Bobil': (44.42, 32.54), 'Nineviya': (43.15, 36.36), 'Oshshur': (43.26, 35.46),
    'Xattusa': (34.61, 40.02), 'Tushpa': (43.33, 38.5), 'Tir': (35.2, 33.27), 'Suza': (48.25, 32.19), 'Persepol': (52.89, 29.93),
    'Ekbatana': (48.5, 34.8), 'Lidiya': (28.04, 38.48), 'Iyerusalim': (35.23, 31.78), 'Shumer': (46.0, 31.0), 'Akkad': (44.2, 33.0),
    'Moxenjodaro': (68.14, 27.32), 'Xarappa': (72.86, 30.63), 'Gang vodiysi': (83.0, 26.0), 'Hind vodiysi': (70.0, 29.0),
    'Xao (Sian)': (108.9, 34.3), 'Xuanxe': (112.0, 36.0), 'Yantszi': (112.0, 30.0),
    'Afrosiyob': (66.98, 39.67), 'Yerqo‘rg‘on': (65.75, 38.85), 'Uzunqir': (66.5, 39.0), 'Ko‘zaliqir': (61.2, 42.1), 'Qiziltepa': (67.4, 37.65),
    'Marg‘iyona': (61.8, 37.6), 'Orol dengizi': (60.0, 45.0),
})
PLACES.update({
    'Afina': (23.73, 37.98), 'Sparta': (22.43, 37.07), 'Knoss (Krit)': (25.16, 35.3), 'Miken': (22.75, 37.73), 'Olimp tog‘i': (22.35, 40.08),
    'Olimpiya': (21.63, 37.64), 'Marafon': (23.97, 38.15), 'Fermopil': (22.53, 38.8), 'Salamin': (23.5, 37.95), 'Plateya': (23.27, 38.22),
    'Xeroniya': (22.85, 38.5), 'Korinf': (22.93, 37.94), 'Troya': (26.24, 39.96), 'Delfi': (22.5, 38.48), 'Makedoniya': (22.0, 40.9),
    'Attika': (23.9, 38.1), 'Peloponnes': (22.2, 37.5), 'Sirakuza': (15.29, 37.08), 'Olviya': (31.9, 46.7), 'Xersones': (33.49, 44.61),
    'Pantikapey': (36.47, 45.35), 'Sitsiliya (qadimgi)': (14.2, 37.5), 'Yunoniston': (22.5, 39.0), 'Frakiya': (25.5, 41.5),
})
PLACES.update({
    'Maroqanda': (66.98, 39.67), 'Baqtra': (66.9, 36.76), 'Kurushkat': (68.95, 39.95), 'Aleksandriya Esxata': (69.6, 40.28), 'Termiz': (67.28, 37.22),
    'Tuproqqal’a': (60.8, 41.9), 'Qanqa': (69.0, 40.95), 'Davan (Farg‘ona)': (71.8, 40.7), 'Dalvarzintepa': (67.9, 37.85), 'Xolchayon': (67.85, 38.35),
    'Peshovar': (71.58, 34.01), 'Parfiya': (57.5, 37.6), 'Dunxuan': (94.66, 40.14), 'Hisor tog‘lari': (68.5, 38.9), 'Amudaryo (Oks)': (64.0, 39.0),
})
PLACES.update({
    'Kapuya': (14.25, 41.08), 'Vezuviy': (14.43, 40.82), 'Kann': (16.13, 41.31), 'Po daryosi': (11.5, 45.0), 'Etruriya': (11.3, 43.2),
    'Rubikon': (12.4, 44.07), 'Karfagen': (10.32, 36.85), 'Zama': (9.3, 35.9), 'Alp tog‘lari': (9.5, 46.4), 'Sardiniya': (9.0, 40.0),
    'Korsika': (9.1, 42.1), 'Aleksandriya (Misr)': (29.9, 31.2), 'Dakiya': (24.5, 45.8), 'Vifleem': (35.2, 31.7), 'Ispaniya (qadimgi)': (-4.0, 40.0),
})
REG['oldasia'] = [26, 27, 55, 42.5]
PLACES.update({'Gang vodiysi': (81.5, 26.8), 'Korinf': (22.88, 37.82), 'Nil deltasi': (31.0, 31.3)})
REG.update({'ca': [50, 33.5, 80, 48], 'steppe': [45, 33.5, 80, 58]})
PLACES.update({
    'Tura': (65.5, 57.0), 'Sig‘noq': (67.8, 44.4), 'Turkiston': (68.25, 43.3), 'Hirot': (62.2, 34.35), 'Andijon': (72.35, 40.78), 'Axsi': (71.4, 41.0),
    'Kobul': (69.2, 34.5), 'Balx': (66.9, 36.76), 'Karmana': (65.38, 40.14), 'Hisor': (68.55, 38.53), 'Maymana': (64.78, 35.92), 'Urganch': (60.6, 41.55),
    'Xiva': (60.36, 41.38), 'Qo‘qon': (70.94, 40.53), 'O‘ratepa': (69.0, 39.92), 'Xo‘jand': (69.6, 40.28), 'Qarshi': (65.8, 38.86), 'Shahrisabz': (66.83, 39.06),
    'Mashhad': (59.6, 36.3), 'Badaxshon': (71.5, 37.0), 'Qashqar': (75.99, 39.47), 'Dashti Qipchoq': (65.0, 50.0), 'Eron': (55.0, 34.5), 'Termiz': (67.28, 37.22),
})
PLACES.update({'G‘ijduvon': (64.68, 40.1), 'Nishopur': (58.8, 36.2), 'Ashtarxon': (48.03, 46.35), 'Farg‘ona vodiysi': (71.8, 40.7), 'Urgut': (67.24, 39.4)})
PLACES.update({'Nurota': (65.68, 40.56), 'Hazorasp': (61.07, 41.32), 'Orenburg': (55.1, 51.77), 'Qorako‘l': (63.85, 39.5),
               'Miyonqol': (66.3, 39.95), 'Afg‘oniston': (66.0, 34.0), 'Kitob': (66.88, 39.12)})
REG['xorazm'] = [55, 37, 66, 46]
PLACES.update({'Ko‘hna Urganch': (59.15, 42.33), 'Chimboy': (59.78, 42.93), 'Qo‘ng‘irot': (58.9, 43.05),
               'Nijniy Novgorod': (44.0, 56.33), 'Peterburg': (30.3, 59.93), 'Orol bo‘yi': (60.0, 44.3)})
REG['fargona'] = [68.8, 39.3, 74.2, 42.3]
PLACES.update({'O‘sh': (72.8, 40.53), 'O‘zgan': (73.3, 40.77), 'Chust': (71.24, 41.0), 'Namangan': (71.67, 41.0), 'Marg‘ilon': (71.72, 40.47),
               'Chimkent': (69.6, 42.3), 'Isfara': (70.6, 40.12), 'Nukus': (59.6, 42.46), 'Mo‘ynoq': (59.0, 43.77), 'Xo‘jayli': (59.45, 42.4),
               'Bo‘zatov': (58.6, 43.4), 'Ko‘lob': (69.78, 37.91), 'Avliyoota': (71.37, 42.9), 'Pishpak': (74.6, 42.87), 'Oqmachit': (65.5, 44.85)})
PLACES.update({'Yorkent': (77.24, 38.42), 'Oqmasjid': (65.5, 44.85), 'Raim': (61.9, 45.9)})
REG['xorazm'] = [56, 39.5, 63.5, 45]
PLACES.update({'Bagama orollari': (-76.0, 24.5), 'Yaxshi Umid burni': (18.5, -34.3), 'Lissabon': (-9.14, 38.72), 'Sevilya': (-5.98, 37.39),
               'Kalkutta (Hindiston)': (88.3, 22.6), 'Portugaliya': (-8.2, 39.6), 'Ispaniya': (-3.7, 40.2), 'Avstraliya': (134.0, -25.0),
               'Madeyra': (-16.9, 32.7), 'Gollandiya': (5.3, 52.2)})
REG['globe'] = [-135, -48, 179, 70]
PLACES.update({'Vittenberg': (12.65, 51.87), 'Vorms': (8.36, 49.63), 'Jeneva': (6.14, 46.2), 'Fransiya': (2.5, 46.8)})
PLACES.update({'Vestfaliya (Myunster)': (7.63, 51.96), 'Kuchukqaynarji': (26.6, 44.0), 'Shvetsiya': (15.5, 60.5), 'Avstriya': (14.5, 47.6), 'Uels': (-3.7, 52.3)})
PLACES.update({'Valmi': (4.77, 49.08), 'Belgiya': (4.5, 50.6), 'Jironda': (-0.6, 44.8), 'Prussiya': (13.4, 52.5)})
PLACES.update({'Vena': (16.37, 48.2), 'Berlin': (13.4, 52.52), 'Strasburg': (7.75, 48.58), 'Nishtadt': (21.4, 60.8)})
REG['usa_e'] = [-92, 28, -64, 47]
PLACES.update({'Jeymstaun': (-76.78, 37.21), 'Filadelfiya': (-75.16, 39.95), 'Boston': (-71.06, 42.36), 'Nyu-York': (-74.0, 40.71),
               'Zalsburg': (13.05, 47.8), 'Dublin': (-6.26, 53.35), 'Veymar': (11.33, 50.98)})
REG['eastasia'] = [95, 8, 145, 46]
REG['india'] = [60, 6, 95, 37]
PLACES.update({'Panipat': (76.97, 29.39), 'Agra': (78.02, 27.18), 'Tayvan': (121.0, 23.7), 'Guanchjou': (113.26, 23.13), 'Filippin': (121.5, 14.0),
               'Manjuriya': (126.0, 45.0), 'Edo (Tokio)': (139.7, 35.7), 'Nagasaki': (129.87, 32.75), 'Seul': (126.98, 37.57)})
PLACES.update({'Ardabil': (48.3, 38.25), 'Tabriz': (46.3, 38.08), 'Tehron': (51.39, 35.69), 'Sheroz': (52.53, 29.6), 'Turkiya': (33.0, 39.0)})
PLACES.update({'Jazoir': (3.06, 36.75), 'Tripoli': (13.18, 32.89), 'Tunis': (10.18, 36.8), 'Kongo daryosi': (15.3, -4.3), 'Oltin qirg‘oq': (-1.0, 5.3),
               'Yashil burun': (-17.5, 14.7), 'Senegal': (-14.5, 14.5), 'Liberiya': (-9.4, 6.4)})
PLACES.update({'Kanada': (-100.0, 56.0), 'Yangi Zelandiya': (172.5, -41.5)})
PLACES.update({'Austerlis': (16.76, 49.15), 'Tilzit': (21.88, 55.08), 'Borodino': (35.82, 55.52), 'Leypsig': (12.37, 51.34), 'Vaterloo': (4.4, 50.68),
               'Elba oroli': (10.25, 42.78)})
PLACES.update({'Alyaska': (-150.0, 64.0), 'Kavkaz': (44.0, 42.5), 'Turkiston o‘lkasi': (66.0, 41.0), 'Sibir': (95.0, 60.0)})
PLACES.update({'Virjiniya': (-78.6, 37.5), 'Shimoliy shtatlar': (-75.0, 42.5), 'Janubiy shtatlar': (-86.0, 32.5)})
REG['latam'] = [-118, -56, -34, 33]
PLACES.update({'Meksika': (-102.0, 23.5), 'Venesuela': (-66.0, 7.5), 'Argentina': (-64.0, -34.0), 'Braziliya': (-50.0, -10.0), 'Boliviya': (-64.5, -16.5),
               'Kuba': (-79.5, 21.8), 'Chili': (-71.0, -30.0), 'Paragvay': (-58.0, -23.4), 'Peru': (-75.0, -9.5), 'Kolumbiya': (-73.0, 4.0)})
PLACES.update({'Kalkutta': (88.36, 22.57), 'Gonkong': (114.17, 22.3), 'Bombey': (72.88, 19.08)})
PLACES.update({'Jejudo oroli': (126.55, 33.38)})
PLACES.update({'Gretsiya': (22.0, 39.3), 'Bolqon': (21.0, 43.0), 'Sudan': (30.0, 15.5)})
PLACES.update({'Qandahor': (65.7, 31.6), 'Ozarbayjon (Tabriz)': (46.3, 38.08)})
REG['iranafg'] = [43, 24, 76, 41]
PLACES.update({'Efiopiya': (39.5, 9.0), 'Madagaskar': (46.8, -19.0), 'Kap koloniyasi': (19.5, -32.5), 'Angola': (17.5, -12.0), 'Mozambik': (35.5, -17.0),
               'Monroviya': (-10.8, 6.3)})
PLACES.update({'Versal': (2.12, 48.8), 'Vashington': (-77.04, 38.9), 'Lozanna': (6.63, 46.52), 'Manchjuriya': (126.0, 45.0), 'Chikago': (-87.63, 41.88),
               'Nyu-Meksiko': (-106.0, 34.4), 'Toshkent (1928)': (69.24, 41.3)})
PLACES.update({'Amritsar': (74.87, 31.63), 'Myunxen': (11.58, 48.14), 'Sudet viloyati': (14.0, 50.6), 'Elzas': (7.5, 48.3), 'Lotaringiya': (6.2, 49.0),
               'Saar': (6.95, 49.4), 'Chexoslovakiya': (17.0, 49.2)})
PLACES.update({'Pyorl-Xarbor': (-157.95, 21.35), 'Kil': (10.13, 54.32), 'Rur': (7.2, 51.45), 'Veymar': (11.33, 50.98)})
REG['globe2'] = [-170, -48, 179, 72]
PLACES.update({'Brest-Litovsk': (23.7, 52.1), 'Vladivostok': (131.9, 43.12), 'Hasan ko‘li': (130.6, 42.43), 'Xalxin-Gol': (118.5, 47.6), 'Rapallo': (9.23, 44.35)})
REG['eurasia2'] = [-10, 25, 150, 70]
PLACES.update({'Albaniya': (20.0, 41.1), 'Kataloniya': (1.5, 41.8), 'Eritreya': (39.0, 15.3), 'Somali': (46.0, 6.0), 'Urugvay': (-56.0, -32.8)})
PLACES.update({'Saxalin': (142.7, 50.5), 'Tokio': (139.7, 35.7)})
REG['fareast'] = [100, 18, 156, 58]
PLACES.update({'Shanxay': (121.47, 31.23), 'Shandun': (118.0, 36.4), 'Uxan': (114.3, 30.6)})
PLACES.update({'Anqara': (32.85, 39.93), 'Sevr': (2.21, 48.82)})
PLACES.update({'Stalingrad': (44.5, 48.7), 'Tehron (1943)': (51.39, 35.69), 'Yalta': (34.16, 44.5), 'Potsdam': (13.06, 52.39), 'Nyurnberg': (11.08, 49.45),
               'Xirosima': (132.46, 34.39), 'Kareliya': (33.0, 63.0)})
PLACES.update({'Fulton': (-91.95, 38.85), 'Reykyavik': (-21.9, 64.15), 'Varshava': (21.0, 52.23)})
PLACES.update({'Memfis (AQSH)': (-90.05, 35.15), 'Dallas': (-96.8, 32.78), 'Vyetnam (Janubiy)': (106.7, 12.0)})
PLACES.update({'Minsk': (27.56, 53.9), 'Qozog‘iston (qo‘riq yerlar)': (68.0, 50.0)})
PLACES.update({'Folklend orollari': (-59.5, -51.7), 'Shimoliy Irlandiya': (-6.7, 54.6), 'Xelsinki': (24.94, 60.17)})
PLACES.update({'Bonn': (7.1, 50.73)})
PLACES.update({'Janubiy Koreya': (127.8, 36.3), 'Singapur': (103.82, 1.35), 'Malayziya': (102.0, 4.0), 'Tayland': (101.0, 15.5), 'Indoneziya': (113.0, -1.0)})
REG['seasia'] = [90, -10, 146, 45]
PLACES.update({'Yanan': (109.49, 36.6)})
PLACES.update({'Pokiston': (69.5, 29.5), 'Dehli (1947)': (77.2, 28.6)})
REG['sasia'] = [55, 5, 95, 46]
PLACES.update({'Iroq': (43.7, 33.2)})
REG['nearest'] = [25, 24, 76, 44]
PLACES.update({'Nikaragua': (-85.0, 12.9), 'Gavana': (-82.38, 23.13)})
PLACES.update({'Nigeriya': (8.0, 9.5), 'Kongo': (23.0, -2.5), 'Janubiy Afrika Respublikasi': (25.0, -29.0), 'Manchester': (-2.24, 53.48)})
# 9-sinf O‘zbekiston tarixi
PLACES.update({'Rishton': (71.28, 40.36), 'Shahrixon': (72.06, 40.71)})
PLACES.update({'Verniy (Almati)': (76.95, 43.25), 'Ashxobod': (58.38, 37.95), 'Petro-Aleksandrovsk (To‘rtko‘l)': (61.0, 41.55),
               'Jizzax': (67.84, 40.12), 'Erjar': (68.75, 40.55), 'Kattaqo‘rg‘on': (66.26, 39.9), 'Zirabuloq': (66.0, 39.98),
               'Mahram': (69.2, 40.4), 'Dushanbe': (68.78, 38.56), 'Krasnovodsk': (52.97, 40.02), 'Panjikent': (67.6, 39.5),
               'Uchqo‘rg‘on': (72.08, 41.11)})
REG['ca2'] = [52, 35.5, 80, 46]
PLACES.update({'Mang‘it': (60.06, 42.12), 'Mang‘ishloq': (51.5, 44.2)})
REG['zarafshon'] = [64, 38.5, 68.5, 40.6]
PLACES.update({'Go‘ktepa': (57.97, 38.16)})
PLACES.update({'Qizilarvat': (56.27, 39.0), 'Mingtepa': (72.33, 40.5)})
PLACES.update({'Zomin': (68.4, 39.96)})
PLACES.update({'Chorjo‘y': (63.58, 39.08), 'Denov': (67.9, 38.27), 'Karki': (65.2, 37.83), 'Baljuvon': (69.68, 38.32), 'Kalif': (65.25, 37.53)})
REG['buxamir'] = [61, 36.3, 72, 41.2]
PLACES.update({'Gurlan': (60.39, 41.84), 'Yangi Urganch': (60.63, 41.55)})
# 9-sinf Jahon tarixi
PLACES.update({'Gavayi orollari': (-157.0, 20.8), 'Puerto-Riko': (-66.5, 18.2), 'Guam': (144.8, 13.45),
               'Sedan': (4.94, 49.7), 'Mets': (6.18, 49.12), 'Frankfurt': (8.68, 50.11)})
PLACES.update({'Togo': (1.0, 8.6), 'Kamerun': (12.5, 5.5), 'Zanzibar': (39.3, -6.1), 'Quvayt': (47.9, 29.3),
               'Laos': (103.0, 19.5), 'Bosfor': (29.05, 41.1)})
PLACES.update({'Kipr': (33.2, 35.0), 'Suvaysh kanali': (32.55, 30.6), 'Keniya': (37.9, 0.2), 'Uganda': (32.4, 1.3),
               'Transvaal': (28.5, -25.0), 'Panama kanali': (-79.7, 9.1), 'Kaliforniya': (-119.5, 37.0), 'Texas': (-99.0, 31.0),
               'Gavana (Kuba)': (-82.38, 23.13)})
PLACES.update({'Kolorado': (-105.5, 39.0), 'Mexiko': (-99.13, 19.43)})
PLACES.update({'Buenos-Ayres': (-58.38, -34.6)})
PLACES.update({'Rio-de-Janeyro': (-43.2, -22.9), 'Gvatemala': (-90.5, 15.5), 'Port-Artur': (121.25, 38.8), 'Susima': (129.3, 34.4),
               'Kuril orollari': (150.0, 46.5), 'Kushka': (62.35, 35.28), 'Bosniya': (17.8, 44.2), 'Serbiya': (20.9, 44.0),
               'Chernogoriya': (19.3, 42.7), 'Ruminiya': (25.0, 45.9), 'Kars': (43.1, 40.6), 'Batumi': (41.64, 41.64),
               'San-Stefano': (28.82, 40.98), 'Riga': (24.1, 56.95), 'Boku': (49.87, 40.41), 'Peterburg (1905)': (30.3, 59.94)})
REG['balkan'] = [12, 36, 45, 48]
PLACES.update({'Praga': (14.42, 50.08), 'Budapesht': (19.04, 47.5), 'Galitsiya': (24.0, 49.6), 'Adua': (38.9, 14.16),
               'Xorvatiya': (16.0, 45.3), 'Sofiya': (23.32, 42.7), 'Belgrad': (20.46, 44.82), 'Bosniya va Gersegovina': (17.8, 44.0)})
PLACES.update({'Ryukyu orollari': (127.8, 26.3), 'Sindao': (120.38, 36.07), 'Assam': (92.9, 26.2), 'Simonoseki': (130.94, 33.95)})
PLACES.update({'Puna': (73.86, 18.52), 'Surat': (72.83, 21.17), 'Gandamak': (70.0, 34.3), 'Izmir': (27.14, 38.42),
               'Monastir': (21.33, 41.03), 'Saloniki': (22.94, 40.64), 'Adrianopol': (26.56, 41.68)})
PLACES.update({'Iskandariya': (29.92, 31.2), 'Xartum': (32.53, 15.6), 'Keyptaun': (18.42, -33.92), 'Sarayevo': (18.41, 43.86),
               'Marna daryosi': (3.6, 48.95), 'Ipr': (2.88, 50.85), 'Somma daryosi': (2.3, 49.9), 'Dardanell': (26.4, 40.2)})
PLACES.update({'Brest': (23.69, 52.1), 'Kompyen': (2.83, 49.42), 'Sen-Gotard': (8.57, 46.56)})
OVR.update({('africa', 'Tunis'): (296, 52), ('africa', 'Jazoir'): (230, 105)})
# 10-sinf O‘zbekiston tarixi
PLACES.update({'Jalolobod': (73.0, 40.93)})
PLACES.update({'Taxta': (59.85, 41.65), 'Porsu': (59.4, 42.1)})
PLACES.update({'Vilnyus': (25.28, 54.69), 'Viborg': (28.75, 60.71)})
PLACES.update({'Bekobod': (69.23, 40.22), 'Gdansk': (18.65, 54.35), 'Gomel': (31.0, 52.43), 'Yelna': (33.18, 54.58), 'Kursk': (36.19, 51.73)})
PLACES.update({'Guliston': (68.78, 40.49)})
PLACES.update({'Leningrad': (30.32, 59.94)})
PLACES.update({'Beynov': (55.2, 45.32), 'Navoiy': (65.38, 40.1), 'Chirchiq': (69.58, 41.47)})
PLACES.update({'Gazli': (63.45, 40.13), 'Muborak': (65.15, 39.26), 'Uchquduq': (63.55, 42.15)})
PLACES.update({'Quvasoy': (71.98, 40.3)})
# Yangi darslik 10-sinf Jahon tarixi
PLACES.update({'Bryussel': (4.35, 50.85), 'Liverpul': (-2.98, 53.41), 'Nant': (-1.55, 47.22), 'Bristol': (-2.59, 51.45)})
PLACES.update({'Liviya (Afrika)': (17.5, 27.0)})
PLACES.update({'Ukraina': (31.5, 49.2), 'Litva': (24.0, 55.3)})
REG['swasia'] = [30, 19, 60, 39]
PLACES.update({'Iordaniya': (36.6, 31.0), 'Livan': (35.9, 33.9), 'BAA': (54.3, 23.9), 'Saudiya Arabistoni': (45.0, 24.0), 'Bayrut': (35.5, 33.9)})
PLACES.update({'Gana (Oltin Qirg‘oq)': (-1.2, 7.9)})
REG.update({'europeN': [-11, 34, 42, 64.5], 'amerpac': [-178, -5, 150, 72]})
PLACES.update({'Janubiy Manchjuriya': (123.5, 42.3)})
