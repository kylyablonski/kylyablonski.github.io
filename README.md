# Fog Log

A personal [Dead by Daylight](https://deadbydaylight.com/) survivor match diary. Log a trial, look back at what worked, and spin a perk loadout from the perks you own. Match history stays in your browser (`localStorage`) — nothing is sent anywhere.

The live site is one file, `index.html` (plain HTML, CSS, and JavaScript).

## Editing perk tags

Perk moods and one-line descriptions live in [`data/perk_tags.txt`](data/perk_tags.txt). Each line is:

```
Perk name | tags | one-line description
```

Tags are a comma-separated list drawn from `annoy`, `hidden`, `chase`, `support`, `gens`, `lucky`, and `chaos`. Lines starting with `#` are comments.

Beginner how-to tips live in [`data/perk_tips.txt`](data/perk_tips.txt).

After you edit the file, rebuild the page:

```bash
python3 src/build.py
```

That rewrites `index.html` from `src/template.html` and the files in `data/`.
