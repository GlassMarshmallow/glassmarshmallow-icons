"""Flechas: Arrows, Chevrons, Carets, Shape arrows y Box arrows de Bootstrap Icons.

Casi todas se dibujan una vez mirando hacia arriba y se giran para el resto de direcciones.
"""
import math
from lib import CIRCLE, SQUARE, W, K, p, rot, mirror_x, mirror_y, layer, arrow_segment

CATEGORY = 'Flechas'

# Grados de giro desde «arriba»
DIRS = {'up': 0, 'up-right': 45, 'right': 90, 'down-right': 135, 'down': 180, 'down-left': 225, 'left': 270, 'up-left': 315}
STRAIGHT = ('up', 'right', 'down', 'left')
DIAGONAL = ('up-right', 'down-right', 'down-left', 'up-left')

LINE = {}
FILL = {}

# --- Arrows -----------------------------------------------------------------------
ARROW = p('M12 19.5V4.5M6 10.5l6-6 6 6')
ARROW_SHORT = p('M12 16.5v-9M8 11.5l4-4 4 4')
# La flecha se aleja de la barra, como en Bootstrap
ARROW_BAR = p('M5 19.5h14M12 15.5V4.5M7 9.5l5-5 5 5')
ARROW_90 = p('M20 19H9.5a2 2 0 0 1-2-2V5M3.5 9l4-4 4 4')

for d in STRAIGHT + DIAGONAL:
    LINE[f'arrow-{d}'] = rot(ARROW, DIRS[d])
for d in STRAIGHT:
    LINE[f'arrow-{d}-short'] = rot(ARROW_SHORT, DIRS[d])
    LINE[f'arrow-bar-{d}'] = rot(ARROW_BAR, DIRS[d])

# Giro de 90°: la línea llega por abajo a la derecha y la flecha sale en la dirección del nombre
LINE['arrow-90deg-up'] = ARROW_90
LINE['arrow-90deg-down'] = mirror_y(ARROW_90)
LINE['arrow-90deg-right'] = rot(ARROW_90, 90)
LINE['arrow-90deg-left'] = mirror_x(rot(ARROW_90, 90))

LINE['arrow-return-left'] = p('M19.5 5v6a3 3 0 0 1-3 3H4.5M9 9.5L4.5 14 9 18.5')
LINE['arrow-return-right'] = mirror_x(LINE['arrow-return-left'])
LINE['arrow-clockwise'] = p('M19.5 12A7.5 7.5 0 1 1 12 4.5c2.1 0 4 .85 5.35 2.25M18 3.5v4h-4')
LINE['arrow-counterclockwise'] = mirror_x(LINE['arrow-clockwise'])
LINE['arrow-repeat'] = p('M4.5 12a7.5 7.5 0 0 1 13-5.1M19.5 12a7.5 7.5 0 0 1-13 5.1M18 3.5V7h-3.5M6 20.5V17h3.5')
LINE['arrow-left-right'] = p('M4.5 8.5h15M15.5 4.5l4 4-4 4M19.5 15.5h-15M8.5 11.5l-4 4 4 4')
LINE['arrow-down-up'] = rot(LINE['arrow-left-right'], 90)
LINE['arrows'] = p('M4 12h16M7.5 8.5L4 12l3.5 3.5M16.5 8.5L20 12l-3.5 3.5')
LINE['arrows-vertical'] = rot(LINE['arrows'], 90)
LINE['arrows-move'] = p('M12 3v18M3 12h18M9.5 5.5L12 3l2.5 2.5M9.5 18.5L12 21l2.5-2.5M5.5 9.5L3 12l2.5 2.5M18.5 9.5L21 12l-2.5 2.5')
LINE['arrows-angle-expand'] = p('M14 10l5.5-5.5M15 4.5h4.5V9M10 14l-5.5 5.5M4.5 15v4.5H9')
LINE['arrows-angle-contract'] = p('M19.5 4.5L14 10M14 5.5V10h4.5M4.5 19.5L10 14M5.5 14H10v4.5')
LINE['arrows-fullscreen'] = p('M4.5 9V4.5H9M15 4.5h4.5V9M19.5 15v4.5H15M9 19.5H4.5V15'
                              'M4.5 4.5l5 5M19.5 4.5l-5 5M19.5 19.5l-5-5M4.5 19.5l5-5')
LINE['arrows-expand'] = p('M4 12h16M12 9.5v-6M9.5 6L12 3.5 14.5 6M12 14.5v6M9.5 18l2.5 2.5 2.5-2.5')
LINE['arrows-collapse'] = p('M4 12h16M12 3.5v6M9.5 7l2.5 2.5L14.5 7M12 20.5v-6M9.5 17l2.5-2.5 2.5 2.5')
LINE['arrows-expand-vertical'] = rot(LINE['arrows-expand'], 90)
LINE['arrows-collapse-vertical'] = rot(LINE['arrows-collapse'], 90)
LINE['shuffle'] = p('M4 7h3.5c4.5 0 4.5 10 9 10H20M4 17h3.5c1.6 0 2.6-1.3 3.4-3M13.1 10c.8-1.7 1.8-3 3.4-3H20'
                    'M17.5 4.5L20 7l-2.5 2.5M17.5 14.5L20 17l-2.5 2.5')


def recycle():
    """Tres flechas siguiendo los lados de un triángulo."""
    r = 9.6
    pts = [(12 + r * math.cos(math.radians(a)), 13.2 + r * math.sin(math.radians(a))) for a in (-90, 30, 150)]
    d = ''
    for i in range(3):
        (x1, y1), (x2, y2) = pts[i], pts[(i + 1) % 3]
        # Cada flecha ocupa la parte central del lado
        sx, sy = x1 + (x2 - x1) * .14, y1 + (y2 - y1) * .14
        ex, ey = x1 + (x2 - x1) * .76, y1 + (y2 - y1) * .76
        d += arrow_segment(sx, sy, ex, ey, 3)
    return p(d)


LINE['recycle'] = recycle()

# --- Chevrons -------------------------------------------------------------------------
CHEVRON = p('M5 15l7-7 7 7')
CHEVRON_DOUBLE = p('M6 12.5l6-6 6 6M6 18.5l6-6 6 6')
CHEVRON_BAR = p('M5 4.5h14M6 15.5l6-6 6 6')
CHEVRON_COMPACT = p('M3.5 14.5L12 10l8.5 4.5')
for d in STRAIGHT:
    LINE[f'chevron-{d}'] = rot(CHEVRON, DIRS[d])
    LINE[f'chevron-double-{d}'] = rot(CHEVRON_DOUBLE, DIRS[d])
    LINE[f'chevron-bar-{d}'] = rot(CHEVRON_BAR, DIRS[d])
    LINE[f'chevron-compact-{d}'] = rot(CHEVRON_COMPACT, DIRS[d])
LINE['chevron-expand'] = p('M7 9l5-5 5 5M7 15l5 5 5-5')
LINE['chevron-contract'] = p('M7 5l5 5 5-5M7 19l5-5 5 5')
LINE['chevron-bar-expand'] = p('M4 12h16M8 7.5l4-4 4 4M8 16.5l4 4 4-4')
LINE['chevron-bar-contract'] = p('M4 12h16M8 3.5l4 4 4-4M8 20.5l4-4 4 4')

# --- Carets -----------------------------------------------------------------------------
CARET = p('M10.6 7.6a1.8 1.8 0 0 1 2.8 0l5 6.2a1.3 1.3 0 0 1-1 2.2H6.6a1.3 1.3 0 0 1-1-2.2Z')
CARET_SMALL = p('M11.2 9a1 1 0 0 1 1.6 0l3.1 4.1a.8.8 0 0 1-.6 1.4H8.7a.8.8 0 0 1-.6-1.4Z')
for d in STRAIGHT:
    LINE[f'caret-{d}'] = rot(CARET, DIRS[d])
    FILL[f'caret-{d}'] = [layer(W, rot(CARET, DIRS[d]))]
    LINE[f'caret-{d}-square'] = SQUARE + rot(CARET_SMALL, DIRS[d])
    FILL[f'caret-{d}-square'] = [layer(W, SQUARE), layer(K, rot(CARET_SMALL, DIRS[d]))]

# --- Shape arrows (flecha dentro de un círculo o un cuadrado) --------------------------------
INNER = p('M12 16.5v-9M8.5 11l3.5-3.5 3.5 3.5')
for d in STRAIGHT + DIAGONAL:
    inner = rot(INNER, DIRS[d])
    LINE[f'arrow-{d}-circle'] = CIRCLE + inner
    FILL[f'arrow-{d}-circle'] = [layer(W, CIRCLE), layer(K, inner, False)]
    LINE[f'arrow-{d}-square'] = SQUARE + inner
    FILL[f'arrow-{d}-square'] = [layer(W, SQUARE), layer(K, inner, False)]

# --- Box arrows ----------------------------------------------------------------------------------
# Hacia fuera: la caja a la izquierda y la flecha sale por la derecha (luego se gira)
BOX_OUT = p('M14 7.5V6a1.5 1.5 0 0 0-1.5-1.5h-7A1.5 1.5 0 0 0 4 6v12a1.5 1.5 0 0 0 1.5 1.5h7A1.5 1.5 0 0 0 14 18v-1.5'
            'M9.5 12h11M17 8.5l3.5 3.5-3.5 3.5')
# Hacia dentro: la caja ocupa casi todo el icono, con una abertura en el lado por el que entra la flecha,
# y la punta queda dentro de la caja
BOX_IN = p('M8 8.5V5.5a2 2 0 0 1 2-2h8.5a2 2 0 0 1 2 2v13a2 2 0 0 1-2 2H10a2 2 0 0 1-2-2v-3'
           'M3.5 12H15M11.5 8.5L15 12l-3.5 3.5')
for d, deg in (('right', 0), ('down', 90), ('left', 180), ('up', 270)):
    LINE[f'box-arrow-{d}'] = rot(BOX_OUT, deg)
    LINE[f'box-arrow-in-{d}'] = rot(BOX_IN, deg)

# Diagonales: la caja en una esquina y la flecha sale (o entra) en diagonal
BOX_UP_RIGHT = p('M13 4.5h6.5V11M19.5 4.5L11 13M17 14v4a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V9a2 2 0 0 1 2-2h4')
# Diagonal hacia dentro: la caja abierta solo por la esquina por la que entra la flecha
BOX_IN_DOWN_LEFT = p('M10.5 7h-5a2 2 0 0 0-2 2v9.5a2 2 0 0 0 2 2H15a2 2 0 0 0 2-2v-5'
                     'M20.5 3.5L8.5 15.5M8.5 9.5v6h6')
LINE['box-arrow-up-right'] = BOX_UP_RIGHT
LINE['box-arrow-up-left'] = mirror_x(BOX_UP_RIGHT)
LINE['box-arrow-down-right'] = mirror_y(BOX_UP_RIGHT)
LINE['box-arrow-down-left'] = rot(BOX_UP_RIGHT, 180)
LINE['box-arrow-in-down-left'] = BOX_IN_DOWN_LEFT
LINE['box-arrow-in-down-right'] = mirror_x(BOX_IN_DOWN_LEFT)
LINE['box-arrow-in-up-left'] = mirror_y(BOX_IN_DOWN_LEFT)
LINE['box-arrow-in-up-right'] = rot(BOX_IN_DOWN_LEFT, 180)
