"""Dibujo de los iconos de glassmarshmallow.

Cuadrícula de 24 × 24, trazo de 1,5 px con extremos y uniones redondeados.
- Línea: el contorno con stroke="currentColor".
- Relleno (-fill): una máscara dentro del SVG; lo blanco se pinta y lo negro se recorta.

Cada categoría está en su propio archivo (basic.py, arrows.py…) con dos diccionarios: LINE y FILL.
Los nombres son los de Bootstrap Icons; bootstrap-categories.json dice a qué categoría pertenece cada uno.

Uso: python3 source/draw.py  (escribe los SVG en icons/ y catalog.json)
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import alerts  # noqa: E402
import app  # noqa: E402
import arrows  # noqa: E402
import basic  # noqa: E402
import brands  # noqa: E402
import web  # noqa: E402

MODULES = [basic, arrows, alerts, web, app, brands]

OUT = HERE.parent / 'icons'
ROOT = ('<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" '
        'fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">')

bootstrap_categories = json.loads((HERE / 'bootstrap-categories.json').read_text())

# Iconos de Bootstrap que no se hacen en glassmarshmallow (decidido por Sara)
EXCLUDED = {'arrow-through-heart', 'plus-circle-dotted', 'plus-square-dotted'}

line, fill = {}, {}
for module in MODULES:
    for name in module.LINE:
        if name in line:
            sys.exit(f'Icono repetido: {name}')
        if name not in bootstrap_categories and module is not brands:
            sys.exit(f'{name} no existe en Bootstrap Icons')
        if name in EXCLUDED:
            sys.exit(f'{name} está en la lista de excluidos')
    line.update(module.LINE)
    fill.update(module.FILL)

missing_line = set(fill) - set(line)
if missing_line:
    sys.exit(f'Relleno sin versión de línea: {sorted(missing_line)}')


def write(name, body):
    (OUT / f'{name}.svg').write_text(ROOT + body + '</svg>\n')


OUT.mkdir(exist_ok=True)
for old in OUT.glob('*.svg'):
    old.unlink()
for name, body in line.items():
    write(name, body)
for name, layers in fill.items():
    mid = f'gmi-{name}-fill'
    write(f'{name}-fill', f'<defs><mask id="{mid}">{"".join(layers)}</mask></defs>'
          f'<rect width="24" height="24" fill="currentColor" stroke="none" mask="url(#{mid})"/>')

catalog = [{'name': n, 'category': 'Brand' if n in brands.LINE else bootstrap_categories[n], 'fill': n in fill} for n in sorted(line)]
(HERE.parent / 'catalog.json').write_text(json.dumps(catalog, indent=1, ensure_ascii=False) + '\n')

done = len(set(line) & set(bootstrap_categories))
total = len(set(bootstrap_categories) - EXCLUDED)
print(f'{done} de línea y {len(fill)} de relleno · {done} de {total} nombres de Bootstrap Icons')
