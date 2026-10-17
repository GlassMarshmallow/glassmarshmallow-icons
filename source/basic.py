"""Set básico: los iconos de interfaz más usados."""
import math
from lib import CIRCLE, W, K, p, dot, layer, knock_dot

CATEGORY = 'Básicos'

# --- Piezas que se repiten ----------------------------------------------------

def gear_path():
    pts = []
    for i in range(8):
        a = i * 45
        for r, d in ((7.2, -13), (9.2, -8), (9.2, 8), (7.2, 13)):
            t = math.radians(a + d - 90)
            pts.append((r, 12 + r * math.cos(t), 12 + r * math.sin(t)))
    d = f'M{pts[0][1]:.2f} {pts[0][2]:.2f}'
    for i in range(1, len(pts)):
        x, y = pts[i][1], pts[i][2]
        if i % 4 == 0:  # tramo entre dientes: arco sobre el radio interior
            d += f'A7.2 7.2 0 0 1 {x:.2f} {y:.2f}'
        else:
            d += f'L{x:.2f} {y:.2f}'
    x, y = pts[0][1], pts[0][2]
    return d + f'A7.2 7.2 0 0 1 {x:.2f} {y:.2f}Z'

GEAR = gear_path()
TRIANGLE = 'M10.3 4.6a2 2 0 0 1 3.4 0l7 12.1a2 2 0 0 1-1.7 3H5a2 2 0 0 1-1.7-3Z'
HOUSE = 'M4 10.5L12 4l8 6.5V19a1.5 1.5 0 0 1-1.5 1.5H15v-5.5h-6v5.5H5.5A1.5 1.5 0 0 1 4 19Z'
BELL = 'M6 11a6 6 0 0 1 12 0v5l1.5 2.5h-15L6 16Z'
CHAT = 'M6.5 4h11A2.5 2.5 0 0 1 20 6.5v8a2.5 2.5 0 0 1-2.5 2.5H11l-4.5 3.5V17A2.5 2.5 0 0 1 4 14.5v-8A2.5 2.5 0 0 1 6.5 4Z'
HEART = 'M12 19.5S4 14.8 4 9.4C4 6.9 5.9 5 8.3 5c1.6 0 2.9.8 3.7 2.1C12.8 5.8 14.1 5 15.7 5 18.1 5 20 6.9 20 9.4c0 5.4-8 10.1-8 10.1Z'
STAR = 'M12 3.5l2.35 5.76 6.21.46-4.76 4.02 1.49 6.04L12 16.5l-5.29 3.28 1.49-6.04-4.76-4.02 6.21-.46Z'
MOON = 'M20 14.2A8.5 8.5 0 1 1 9.8 4a6.8 6.8 0 0 0 10.2 10.2Z'
SUN_RAYS = 'M12 2.75v1.75M12 19.5v1.75M2.75 12h1.75M19.5 12h1.75M5.46 5.46l1.59 1.59M16.95 16.95l1.59 1.59M18.54 5.46l-1.59 1.59M7.05 16.95l-1.59 1.59'
CLIP_BODY = 'M7.5 4.5h9a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2h-9a2 2 0 0 1-2-2v-12a2 2 0 0 1 2-2Z'
TRASH_BIN = 'M6.5 6.5l.9 12.1a2 2 0 0 0 2 1.9h5.2a2 2 0 0 0 2-1.9l.9-12.1Z'
TRASH_TOP = 'M4.5 6.5h15M9.5 6.5V5a1.5 1.5 0 0 1 1.5-1.5h2A1.5 1.5 0 0 1 14.5 5v1.5'
PENCIL = 'M16.59 4.59A2 2 0 0 1 19.41 7.41L9.41 17.41 4.5 19.5l2.09-4.91Z'
PHONE = ('M8.2 3.8l1.6 3.4a1.2 1.2 0 0 1-.3 1.4L8 9.9a11 11 0 0 0 6.1 6.1l1.3-1.5a1.2 1.2 0 0 1 1.4-.3'
         'l3.4 1.6a1.2 1.2 0 0 1 .7 1.3l-.4 2.1a1.8 1.8 0 0 1-1.9 1.5C10.9 20.2 3.8 13.1 3.3 5.4'
         'a1.8 1.8 0 0 1 1.5-1.9l2.1-.4a1.2 1.2 0 0 1 1.3.7Z')
EYE = 'M2.5 12s3.5-6.5 9.5-6.5 9.5 6.5 9.5 6.5-3.5 6.5-9.5 6.5S2.5 12 2.5 12Z'
FILE = 'M14 3.5H7a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8.5Z'
FOLDER = 'M3.5 7a2 2 0 0 1 2-2h4l2 2.5h7a2 2 0 0 1 2 2V17a2 2 0 0 1-2 2h-13a2 2 0 0 1-2-2Z'
LOCK_BODY = '<rect x="5" y="10.5" width="14" height="10" rx="2"/>'
TRAY = 'M4.5 15.5v2.5a1.5 1.5 0 0 0 1.5 1.5h12a1.5 1.5 0 0 0 1.5-1.5v-2.5'
SHARE_LINES = 'M8.7 10.8l6.6-4.1M8.7 13.2l6.6 4.1'
SHARE_DOTS = '<circle cx="17.5" cy="5.5" r="2.5"/><circle cx="6.5" cy="12" r="2.5"/><circle cx="17.5" cy="18.5" r="2.5"/>'

# --- Iconos de línea ------------------------------------------------------------
LINE = {
    'list': p('M4 7h16M4 12h16M4 17h16'),
    'search': '<circle cx="10.5" cy="10.5" r="6"/>' + p('M15 15l5 5'),
    'link': p('M10 14a4 4 0 0 0 5.66 0l3-3a4 4 0 0 0-5.66-5.66l-1 1M14 10a4 4 0 0 0-5.66 0l-3 3a4 4 0 0 0 5.66 5.66l1-1'),
    'download': p('M12 4v11M7.5 10.5L12 15l4.5-4.5' + TRAY),
    'upload': p('M12 15V4M7.5 8.5L12 4l4.5 4.5' + TRAY),
    'bell': p(BELL) + p('M10 21a2.2 2.2 0 0 0 4 0'),
    'chat': p(CHAT),
    'clipboard': p('M9 4.5H7.5a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h9a2 2 0 0 0 2-2v-12a2 2 0 0 0-2-2H15') + '<rect x="9" y="3" width="6" height="3" rx="1"/>',
    'heart': p(HEART),
    'star': p(STAR),
    'moon': p(MOON),
    'sun': '<circle cx="12" cy="12" r="4"/>' + p(SUN_RAYS),
    'house': p(HOUSE),
    'person': '<circle cx="12" cy="8" r="3.75"/>' + p('M4.75 20a7.25 7.25 0 0 1 14.5 0'),
    'people': '<circle cx="9" cy="8.5" r="3.25"/>' + p('M2.75 19.5a6.25 6.25 0 0 1 12.5 0')
              + '<circle cx="16.5" cy="8.75" r="2.75"/>' + p('M15.5 14a5 5 0 0 1 6 4.9'),
    'gear': p(GEAR) + '<circle cx="12" cy="12" r="3"/>',
    'trash': p(TRASH_TOP) + p(TRASH_BIN) + p('M10 10.5v6M14 10.5v6'),
    'pencil': p(PENCIL) + p('M13.6 7.6l2.8 2.8'),
    'share': SHARE_DOTS + p(SHARE_LINES),
    'envelope': '<rect x="3.5" y="5.5" width="17" height="13" rx="2"/>' + p('M4 7l8 6 8-6'),
    'telephone': p(PHONE),
    'calendar': '<rect x="3.5" y="5" width="17" height="15.5" rx="2"/>' + p('M3.5 10h17M8 3v4M16 3v4'),
    'clock': CIRCLE + p('M12 7.5V12l3 2'),
    'lock': LOCK_BODY + p('M8 10.5V7.5a4 4 0 0 1 8 0v3'),
    'unlock': LOCK_BODY + p('M8 10.5V7.5a4 4 0 0 1 7.76-1.37'),
    'eye': p(EYE) + '<circle cx="12" cy="12" r="3"/>',
    'eye-slash': p(EYE) + '<circle cx="12" cy="12" r="3"/>' + p('M4 4l16 16'),
    'image': '<rect x="3.5" y="4.5" width="17" height="15" rx="2"/><circle cx="9" cy="9.5" r="1.75"/>' + p('M3.5 17l5-5 4 4 2.5-2.5 5.5 5.5'),
    'file': p(FILE) + p('M14 3.5v5h5'),
    'folder': p(FOLDER),
}

# --- Iconos de relleno: capas de máscara (blanco = se pinta, negro = se recorta) ----

CIRCLE_FILL = layer(W, CIRCLE)
FILL = {
    'bell': [layer(W, p(BELL) + p('M10 21a2.2 2.2 0 0 0 4 0'))],
    'chat': [layer(W, p(CHAT))],
    'clipboard': [layer(W, p(CLIP_BODY)), layer(K, '<rect x="8.25" y="2.25" width="7.5" height="4.5" rx="1.6"/>', False),
                  layer(W, '<rect x="9" y="3" width="6" height="3" rx="1"/>')],
    'heart': [layer(W, p(HEART))],
    'star': [layer(W, p(STAR))],
    'moon': [layer(W, p(MOON))],
    'sun': [layer(W, '<circle cx="12" cy="12" r="4.5"/>' + p(SUN_RAYS))],
    'house': [layer(W, p(HOUSE))],
    'person': [layer(W, '<circle cx="12" cy="8" r="3.75"/>' + p('M4.75 20a7.25 7.25 0 0 1 14.5 0Z'))],
    'people': [layer(W, '<circle cx="16.5" cy="8.75" r="2.75"/>' + p('M15.5 14a5 5 0 0 1 6 4.9H15.5Z')),
               layer(K, '<circle cx="9" cy="8.5" r="3.25"/>' + p('M2.75 19.5a6.25 6.25 0 0 1 12.5 0Z'), True, width=4),
               layer(W, '<circle cx="9" cy="8.5" r="3.25"/>' + p('M2.75 19.5a6.25 6.25 0 0 1 12.5 0Z'))],
    'gear': [layer(W, p(GEAR)), knock_dot(12, 12, 3)],
    'trash': [layer(W, p(TRASH_BIN)), layer(W, p(TRASH_TOP), False), layer(K, p('M10 10.5v6M14 10.5v6'), False)],
    'pencil': [layer(W, p(PENCIL)), layer(K, p('M13.6 7.6l2.8 2.8'), False)],
    'share': [layer(W, SHARE_DOTS + p(SHARE_LINES))],
    'envelope': [layer(W, '<rect x="3.5" y="5.5" width="17" height="13" rx="2"/>'), layer(K, p('M5 7.5l7 5.25 7-5.25'), False)],
    'telephone': [layer(W, p(PHONE))],
    'calendar': [layer(W, '<rect x="3.5" y="5" width="17" height="15.5" rx="2"/>'), layer(K, p('M3.5 10h17'), False),
                 layer(W, p('M8 3v4M16 3v4'), False)],
    'clock': [CIRCLE_FILL, layer(K, p('M12 7.5V12l3 2'), False)],
    'lock': [layer(W, LOCK_BODY), layer(W, p('M8 10.5V7.5a4 4 0 0 1 8 0v3'), False), layer(K, p('M12 14.25v2.5'), False)],
    'unlock': [layer(W, LOCK_BODY), layer(W, p('M8 10.5V7.5a4 4 0 0 1 7.76-1.37'), False), layer(K, p('M12 14.25v2.5'), False)],
    'eye': [layer(W, p(EYE)), knock_dot(12, 12, 3.25), '<circle cx="12" cy="12" r="1.75" fill="white" stroke="none"/>'],
    'eye-slash': [layer(W, p(EYE)), knock_dot(12, 12, 3.25), '<circle cx="12" cy="12" r="1.75" fill="white" stroke="none"/>',
                  layer(K, p('M4 4l16 16'), False, width=4.5),
                  layer(W, p('M4 4l16 16'), False)],
    'image': [layer(W, '<rect x="3.5" y="4.5" width="17" height="15" rx="2"/>'), knock_dot(9, 9.5, 1.75),
              layer(K, p('M3.5 17l5-5 4 4 2.5-2.5 5.5 5.5'), False)],
    'file': [layer(W, p(FILE)), layer(K, p('M14 3.5v5h5'), False)],
    'folder': [layer(W, p(FOLDER))],
}

