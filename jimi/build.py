"""Jimi: tayyor mavzu modullarini questions2.json ga joylash.

Foydalanish (repo ildizidan):
    python3 jimi/build.py <bo'lim> <sinf> <kitob> <chiqish.md> <modul> [<modul> ...]
Misol:
    python3 jimi/build.py eski 10 jahon /tmp/10-jahon.md mj10_1 mj10_2

- Modullar jimi/mavzular/ ichida turadi va TOPICS = {mavzu_id: Topic} beradi.
- Mavzu questions2.json da oldindan bo'sh holda bo'lishi kerak (ustiga yozmaydi).
- Chiqish .md fayli foydalanuvchiga yuboriladigan savollar ro'yxati.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path[:0] = [HERE, os.path.join(HERE, 'mavzular')]

sec, grade, book, md_out, *mods = sys.argv[1:]
TOP = {}
for m in mods:
    TOP.update(__import__(m).TOPICS)
f = os.path.join(os.path.dirname(HERE), 'questions2.json')
d = json.load(open(f, encoding='utf-8'))
topics = d['sections'][sec]['grades'][grade]['books'][book]['topics']
md = []
for t in topics:
    if t['id'] not in TOP:
        continue
    Q = TOP[t['id']].Q
    for q in Q:
        assert len(set(q['a'])) == len(q['a']), q['q'][:60]
    assert not t['questions'], t['id'] + ' allaqachon to‘ldirilgan'
    t['questions'] = Q
    md.append(f"# {t['title']}\n")
    for i, q in enumerate(Q, 1):
        md.append(f"**{i}.** " + q['q'].replace('\n', '  \n'))
        if q.get('img'):
            md.append('*(Xarita: raqamlar bilan belgilangan joylar)*' if 'map' in q['img'] else
                      '*(Eyler–Venn diagrammasi: I – chap doira, II – o‘ng doira, III – umumiy qism)*')
        for j, a in enumerate(q['a']):
            md.append(f"- {'ABCD'[j]}) {a}" + (' ✅' if j == q['c'] else ''))
        md.append(f"> {q['e']}\n")
missing = set(TOP) - {t['id'] for t in topics}
assert not missing, f'questions2.json da yo‘q mavzular: {missing}'
open(f, 'w', encoding='utf-8').write(json.dumps(d, ensure_ascii=False, separators=(',', ':')) + '\n')
open(md_out, 'w', encoding='utf-8').write('\n'.join(md))
print({k: len(v.Q) for k, v in TOP.items()}, sum(len(v.Q) for v in TOP.values()))
