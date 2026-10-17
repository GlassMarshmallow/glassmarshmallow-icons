"""Piezas comunes para dibujar los iconos de mallowglass (cuadrícula de 24 × 24, trazo de 1,5 px)."""
import math

CIRCLE = '<circle cx="12" cy="12" r="8.5"/>'
SQUARE = '<rect x="3.5" y="3.5" width="17" height="17" rx="3"/>'
W, K = 'white', 'black'


def p(d):
    return f'<path d="{d}"/>'


def dot(cx, cy, r=1):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="currentColor" stroke="none"/>'


def rot(content, deg):
    """Gira el dibujo alrededor del centro de la cuadrícula."""
    return content if deg % 360 == 0 else f'<g transform="rotate({deg} 12 12)">{content}</g>'


def mirror_x(content):
    """Espejo horizontal (izquierda ↔ derecha)."""
    return f'<g transform="matrix(-1 0 0 1 24 0)">{content}</g>'


def mirror_y(content):
    """Espejo vertical (arriba ↔ abajo)."""
    return f'<g transform="matrix(1 0 0 -1 0 24)">{content}</g>'


def layer(color, content, fill=True, width=None):
    """Capa de máscara para los rellenos: blanco se pinta, negro se recorta."""
    f = color if fill else 'none'
    w = f' stroke-width="{width}"' if width else ''
    return f'<g fill="{f}" stroke="{color}"{w}>{content}</g>'


def knock_dot(cx, cy, r=1):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="black" stroke="none"/>'


def arrow_segment(x1, y1, x2, y2, head=3.2):
    """Línea con punta de flecha en (x2, y2)."""
    dx, dy = x2 - x1, y2 - y1
    n = math.hypot(dx, dy)
    ux, uy = dx / n, dy / n
    # Puntas a ±45° de la dirección
    c, s = math.cos(math.radians(135)), math.sin(math.radians(135))
    l1 = (x2 + head * (ux * c - uy * s), y2 + head * (ux * s + uy * c))
    l2 = (x2 + head * (ux * c + uy * s), y2 + head * (-ux * s + uy * c))
    return (f'M{x1:.2f} {y1:.2f}L{x2:.2f} {y2:.2f}'
            f'M{l1[0]:.2f} {l1[1]:.2f}L{x2:.2f} {y2:.2f}L{l2[0]:.2f} {l2[1]:.2f}')
