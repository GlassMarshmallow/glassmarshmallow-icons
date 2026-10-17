"""Iconos que necesita la web de GlassMarshmallow (barra, documentación y herramientas).

Cada uno va en la categoría que le da Bootstrap Icons (bootstrap-categories.json).
"""
from lib import CIRCLE, W, K, p, dot, layer, knock_dot

CATEGORY = 'Web'

LINE = {}
FILL = {}

# Traducir: un carácter de escritura oriental a la izquierda y una «A» a la derecha
LINE['translate'] = p('M3 6h10M8 3.5V6M5 9.5c1 3 3.5 5.5 7 6.5M11 9.5c-1 3.5-3.5 6-7.5 7M13 20.5l4-10 4 10M14.6 17h4.8')

# Luna con estrellas: la luna del set básico y dos destellos en el hueco
MOON = 'M20 14.2A8.5 8.5 0 1 1 9.8 4a6.8 6.8 0 0 0 10.2 10.2Z'
STARS = 'M16.5 3v3M15 4.5h3M20.5 8v2M19.5 9h2'
LINE['moon-stars'] = p(MOON) + p(STARS)
FILL['moon-stars'] = [layer(W, p(MOON)), layer(W, p(STARS), False)]

# Círculo partido (tema automático): mitad izquierda rellena
LINE['circle-half'] = CIRCLE + '<path d="M12 3.5a8.5 8.5 0 0 0 0 17Z" fill="currentColor"/>'

# Libro abierto
BOOK = 'M12 6.5c-1.8-1.3-4.3-2-8-2v13c3.7 0 6.2.7 8 2 1.8-1.3 4.3-2 8-2v-13c-3.7 0-6.2.7-8 2Z'
LINE['book'] = p(BOOK) + p('M12 6.5v13')
FILL['book'] = [layer(W, p(BOOK)), layer(K, p('M12 6.5v13'), False)]

# Cuadrícula de cuatro casillas
GRID = ''.join(f'<rect x="{x}" y="{y}" width="6.5" height="6.5" rx="1.5"/>' for x in (4, 13.5) for y in (4, 13.5))
LINE['grid'] = GRID
FILL['grid'] = [layer(W, GRID)]

# Cuaderno con anillas y líneas de texto
LINE['journal-text'] = ('<rect x="5.5" y="3.5" width="13" height="17" rx="2"/>'
                        + p('M3.5 7.5h3M3.5 12h3M3.5 16.5h3M9.5 8.5h6M9.5 12h6M9.5 15.5h4'))

# Ventanas apiladas
LINE['window-stack'] = (p('M7 8V5.5a2 2 0 0 1 2-2h10.5a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H17.5')
                        + '<rect x="3.5" y="8" width="14" height="12.5" rx="2"/>' + p('M3.5 11.5h14'))

# Paleta de pintor con cuatro gotas de color
PALETTE = ('M12 3.5c-4.97 0-9 3.6-9 8.2 0 4.4 3.6 8.3 8.3 8.3 1.5 0 2.2-1 2.2-2 0-1.4-1.3-1.8-1.3-3 '
           '0-1 .8-1.6 1.8-1.6h2.6c2.6 0 4.4-1.6 4.4-4C21 6.6 17 3.5 12 3.5Z')
PAINT = [(7.5, 11.5), (9.5, 7.8), (14, 7.3), (17.2, 10.2)]
LINE['palette'] = p(PALETTE) + ''.join(dot(x, y, 1.2) for x, y in PAINT)
FILL['palette'] = [layer(W, p(PALETTE))] + [knock_dot(x, y, 1.3) for x, y in PAINT]
