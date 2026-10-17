"""Avisos y señales (Alerts, warnings, and signs de Bootstrap Icons).

Cada icono es un símbolo (check, más, menos, x, exclamación, info, interrogación, barra) solo o dentro de
un contenedor: círculo, cuadrado, rombo u octógono, y sus versiones de borde punteado.
"""
import math
from lib import CIRCLE, SQUARE, W, K, p, layer, knock_dot

CATEGORY = 'Avisos'

LINE = {}
FILL = {}


def dots(points, color='currentColor'):
    return ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}" stroke="none"/>' for x, y, r in points)


# Símbolo pequeño, para dentro de un contenedor: (trazo, puntos)
INNER = {
    'check': ('M8.5 12.2l2.4 2.4 4.6-4.8', []),
    'dash': ('M8.5 12h7', []),
    'plus': ('M12 8.5v7M8.5 12h7', []),
    'x': ('M9.5 9.5l5 5M14.5 9.5l-5 5', []),
    'slash': ('M14.5 9.5l-5 5', []),
    'exclamation': ('M12 7.5V13', [(12, 16.25, 1)]),
    'info': ('M12 11v5', [(12, 8, 1)]),
    'question': ('M9.6 9.6a2.5 2.5 0 1 1 3.3 2.35c-.55.2-.9.7-.9 1.3v.5', [(12, 16.5, 1)]),
}

# Símbolo suelto (mediano) y grande (-lg)
BARE = {
    'check': ('M5 12.5l4.5 4.5L19 7.5', []),
    'dash': ('M5 12h14', []),
    'plus': ('M12 5v14M5 12h14', []),
    'x': ('M6 6l12 12M18 6L6 18', []),
    'slash': ('M15.5 8.5l-7 7', []),
    'exclamation': ('M12 5v10', [(12, 19, 1.1)]),
    'info': ('M10.5 10.5H12v8.5M10 19h4', [(12, 6.5, 1.1)]),
    'question': ('M8.5 8.5a3.5 3.5 0 1 1 4.6 3.3c-.7.25-1.1.9-1.1 1.6v1.1', [(12, 18.5, 1.1)]),
}
LARGE = {
    'check': ('M3.5 12.5l5.5 5.5L20.5 6', []),
    'dash': ('M3.5 12h17', []),
    'plus': ('M12 3.5v17M3.5 12h17', []),
    'x': ('M5 5l14 14M19 5L5 19', []),
    'slash': ('M19 5L5 19', []),
    'exclamation': ('M12 3v13', [(12, 20.5, 1.3)]),
    'info': ('M9.5 9H12v11.5M9 20.5h6', [(12, 4.5, 1.3)]),
    'question': ('M7.5 7.5a4.5 4.5 0 1 1 5.9 4.25c-.85.3-1.4 1.1-1.4 2v1.75', [(12, 20, 1.3)]),
}


def octagon():
    pts = [(12 + 9.4 * math.cos(math.radians(22.5 + 45 * i)), 12 + 9.4 * math.sin(math.radians(22.5 + 45 * i)))
           for i in range(8)]
    return 'M' + 'L'.join(f'{x:.2f} {y:.2f}' for x, y in pts) + 'Z'


CONTAINERS = {
    'circle': CIRCLE,
    'square': SQUARE,
    'diamond': '<rect x="5.28" y="5.28" width="13.44" height="13.44" rx="2.5" transform="rotate(45 12 12)"/>',
    'octagon': p(octagon()),
}
# Borde de puntos: pathLength fija el número de puntos y los reparte por igual
DOTTED = {
    'circle-dotted': '<circle cx="12" cy="12" r="8.5" pathLength="16" stroke-dasharray="0 1"/>',
    'square-dotted': '<rect x="3.5" y="3.5" width="17" height="17" rx="3" pathLength="20" stroke-dasharray="0 1"/>',
}

# Qué combinaciones existen en Bootstrap Icons (y cuáles tienen relleno)
WITH_FILL = {
    'check': ('circle', 'square'),
    'dash': ('circle', 'square'),
    'plus': ('circle', 'square'),
    'x': ('circle', 'square', 'diamond', 'octagon'),
    'slash': ('circle', 'square'),
    'exclamation': ('circle', 'square', 'diamond', 'octagon'),
    'info': ('circle', 'square'),
    'question': ('circle', 'square', 'diamond', 'octagon'),
}
DOTTED_GLYPHS = {'dash': ('circle-dotted', 'square-dotted')}

for glyph, (d, pts) in BARE.items():
    LINE[glyph] = p(d) + dots(pts)
for glyph, (d, pts) in LARGE.items():
    LINE[f'{glyph}-lg'] = p(d) + dots(pts)

for glyph, shapes in WITH_FILL.items():
    d, pts = INNER[glyph]
    for shape in shapes:
        container = CONTAINERS[shape]
        LINE[f'{glyph}-{shape}'] = container + p(d) + dots(pts)
        FILL[f'{glyph}-{shape}'] = [layer(W, container), layer(K, p(d), False) + dots(pts, 'black')]

for glyph, shapes in DOTTED_GLYPHS.items():
    d, pts = INNER[glyph]
    for shape in shapes:
        LINE[f'{glyph}-{shape}'] = DOTTED[shape] + p(d) + dots(pts)

# Triángulo de aviso
TRIANGLE = 'M10.3 4.6a2 2 0 0 1 3.4 0l7 12.1a2 2 0 0 1-1.7 3H5a2 2 0 0 1-1.7-3Z'
LINE['exclamation-triangle'] = p(TRIANGLE) + p('M12 9.5v4') + dots([(12, 16.6, 1)])
FILL['exclamation-triangle'] = [layer(W, p(TRIANGLE)), layer(K, p('M12 9.5v4'), False) + knock_dot(12, 16.6)]
