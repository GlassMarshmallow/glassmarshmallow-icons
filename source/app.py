"""Iconos que necesita My Book Box App (lector, voces y subida de archivos).

Cada uno va en la categoría que le da Bootstrap Icons (bootstrap-categories.json).
"""
from lib import K, W, p, layer

CATEGORY = 'App'

LINE = {}
FILL = {}

FILE = 'M14 3.5H7a2 2 0 0 0-2 2v13a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8.5Z'
EARMARK = 'M14 3.5v5h5'
BOOK = 'M12 6.5c-1.8-1.3-4.3-2-8-2v13c3.7 0 6.2.7 8 2 1.8-1.3 4.3-2 8-2v-13c-3.7 0-6.2.7-8 2Z'


def sparkle(cx, cy, r):
    """Destello de cuatro puntas con los lados curvados hacia dentro."""
    return (f'M{cx} {cy - r}Q{cx} {cy} {cx + r} {cy}Q{cx} {cy} {cx} {cy + r}'
            f'Q{cx} {cy} {cx - r} {cy}Q{cx} {cy} {cx} {cy - r}Z')


# Altavoz con dos ondas (Escuchar)
LINE['volume-up'] = p('M4 9.5h3.5L12 5.5v13l-4.5-4H4Z') + p('M15.5 9a4.2 4.2 0 0 1 0 6M18.2 6.5a7.8 7.8 0 0 1 0 11')

# Reproductor de vídeo (GlassMarshmallow): reproducir, pausa, sonido, silencio y subtítulos
PLAY = 'M8 5.6v12.8a1 1 0 0 0 1.53.85l10.1-6.4a1 1 0 0 0 0-1.7L9.53 4.75A1 1 0 0 0 8 5.6Z'
LINE['play'] = p(PLAY)
FILL['play'] = [layer(W, p(PLAY))]
PAUSE = '<rect x="6.5" y="5" width="3.5" height="14" rx="1"/><rect x="14" y="5" width="3.5" height="14" rx="1"/>'
LINE['pause'] = PAUSE
FILL['pause'] = [layer(W, PAUSE)]
SPEAKER = 'M4 9.5h3.5L12 5.5v13l-4.5-4H4Z'
WAVES = 'M15.5 9a4.2 4.2 0 0 1 0 6M18.2 6.5a7.8 7.8 0 0 1 0 11'
FILL['volume-up'] = [layer(W, p(SPEAKER)), layer(W, p(WAVES), False)]
MUTE = 'M15.5 9.5l5 5M20.5 9.5l-5 5'
LINE['volume-mute'] = p(SPEAKER) + p(MUTE)
FILL['volume-mute'] = [layer(W, p(SPEAKER)), layer(W, p(MUTE), False)]
BADGE = '<rect x="3" y="5.5" width="18" height="13" rx="2.5"/>'
CC = 'M10.6 10.3a2.3 2.3 0 1 0 0 3.4M17.1 10.3a2.3 2.3 0 1 0 0 3.4'
LINE['badge-cc'] = BADGE + p(CC)
FILL['badge-cc'] = [layer(W, BADGE), layer(K, p(CC), False)]

# Plantilla de portfolio (franja y tarjetas de tecnologías): código y base de datos
LINE['code-slash'] = p('M8 7.5 3.5 12 8 16.5M16 7.5l4.5 4.5-4.5 4.5M13.6 5.5l-3.2 13')
DB_TOP = '<ellipse cx="12" cy="6" rx="7" ry="2.5"/>'
DB_BODY = 'M5 6v12c0 1.4 3.1 2.5 7 2.5s7-1.1 7-2.5V6'
DB_MID = 'M5 12c0 1.4 3.1 2.5 7 2.5s7-1.1 7-2.5'
LINE['database'] = DB_TOP + p(DB_BODY) + p(DB_MID)
FILL['database'] = [layer(W, DB_TOP + p(DB_BODY + 'c0 1.4-3.1 2.5-7 2.5S5 7.4 5 6Z')), layer(K, p(DB_MID) + p('M5 6c0 1.4 3.1 2.5 7 2.5s7-1.1 7-2.5'), False)]

# Cuadrado de «detener»
STOP = '<rect x="6" y="6" width="12" height="12" rx="2"/>'
LINE['stop'] = STOP
FILL['stop'] = [layer(W, STOP)]

# Tres destellos (voces con IA)
LINE['stars'] = p(sparkle(10, 14, 6.5)) + p(sparkle(17.5, 6.5, 3.5)) + p(sparkle(19, 15.5, 2))

# Pantalla completa: cuatro esquinas hacia fuera; salir: las esquinas hacia dentro
LINE['fullscreen'] = p('M4 8.5v-3A1.5 1.5 0 0 1 5.5 4h3M15.5 4h3A1.5 1.5 0 0 1 20 5.5v3'
                       'M20 15.5v3a1.5 1.5 0 0 1-1.5 1.5h-3M8.5 20h-3A1.5 1.5 0 0 1 4 18.5v-3')
LINE['fullscreen-exit'] = p('M8.5 4v3A1.5 1.5 0 0 1 7 8.5H4M20 8.5h-3A1.5 1.5 0 0 1 15.5 7V4'
                            'M15.5 20v-3a1.5 1.5 0 0 1 1.5-1.5h3M4 15.5h3A1.5 1.5 0 0 1 8.5 17v3')

# Marca de elegido, más recta que «check»
LINE['check2'] = p('M5.5 13l4 4 9-10')

# Libro abierto con la página derecha rellena (Empezar a leer)
LINE['book-half'] = p(BOOK) + p('M12 6.5v13') + '<path d="M12 6.5c1.8-1.3 4.3-2 8-2v13c-3.7 0-6.2.7-8 2Z" fill="currentColor"/>'

# Dos imágenes apiladas (Cómic)
LINE['images'] = (p('M7 4.5h11.5a2 2 0 0 1 2 2V16')
                  + '<rect x="3.5" y="7.5" width="14" height="13" rx="2"/><circle cx="8" cy="11.5" r="1.5"/>'
                  + p('M3.5 18l4.5-4.5 3.5 3.5 2-2 4 4'))

# Documento con la esquina doblada y una flecha hacia arriba (subir archivo)
LINE['file-earmark-arrow-up'] = p(FILE) + p(EARMARK) + p('M12 17.5v-6M9.5 14l2.5-2.5 2.5 2.5')

# Documento con una imagen dentro (elegir portada)
LINE['file-earmark-image'] = (p(FILE) + p(EARMARK) + '<circle cx="9.5" cy="11.5" r="1.25"/>'
                              + p('M7.5 17.5l3-3 2 2 1.5-1.5 2.5 2.5'))

# Dos hojas apiladas (varios tomos)
LINE['files'] = (p('M8.5 3.5h8a2 2 0 0 1 2 2v11')
                 + '<rect x="4.5" y="6.5" width="11" height="14" rx="2"/>')

# Colección: una caja con dos líneas encima, como hojas de una pila
LINE['collection'] = '<rect x="3.5" y="9" width="17" height="11.5" rx="2"/>' + p('M5.5 6h13M7.5 3.5h9')

# Carpeta abierta (elegir carpeta)
LINE['folder2-open'] = (p('M4 18.5V6.5a2 2 0 0 1 2-2h3.5l2 2.5H17a2 2 0 0 1 2 2V11')
                        + p('M4 18.5l2.7-6.3a2 2 0 0 1 1.8-1.2h12a1 1 0 0 1 .9 1.4l-2.6 6a2 2 0 0 1-1.8 1.1H5a1 1 0 0 1-1-1Z'))
