#!/usr/bin/env python3
"""Rebuild index.html from src/template.html + data/data.json + data/perk_tags.txt.
Edit perk moods/descriptions in data/perk_tags.txt, then run: python3 src/build.py"""
import json, os
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda *a: os.path.join(root, *a)
data = json.load(open(P('data/data.json')))
VALID = {'annoy','hidden','chase','support','gens','lucky','chaos'}
tags = {}
for line in open(P('data/perk_tags.txt'), encoding='utf-8'):
    line = line.strip()
    if not line or line.startswith('#'): continue
    name, t, blurb = [x.strip() for x in line.split('|', 2)]
    tl = [x.strip() for x in t.split(',') if x.strip()]
    bad = set(tl) - VALID
    if bad or not tl: raise SystemExit(f'Bad tags for {name}: {t}')
    tags[name] = (tl, blurb)
names = {p[0] for p in data['perks']}
missing, extra = names - set(tags), set(tags) - names
if missing or extra: raise SystemExit(f'Tag list mismatch. missing={missing} extra={extra}')
js = lambda o: json.dumps(o, ensure_ascii=False).replace('</', '<\\/')
lines = ',\n'.join(f' {js(n)}: [{js(",".join(tags[n][0]))}, {js(tags[n][1])}]' for n in sorted(tags, key=str.lower))
tpl = open(P('src/template.html'), encoding='utf-8').read()
out = tpl.replace('__DATA__', js(data)).replace('__PERK_TAGS__', '{\n' + lines + '\n}')
open(P('index.html'), 'w', encoding='utf-8').write(out)
print(f'built index.html ({len(out)} bytes, {len(tags)} tagged perks)')
