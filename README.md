# GlassMarshmallow Icons

Line and fill icons for [GlassMarshmallow](https://glassmarshmallow.com). They use the same names as
Bootstrap Icons, with their own design: 24 × 24 grid, 1.5 px stroke and rounded ends.
They take the text color, so you change them with CSS.

Browse and search them at [glassmarshmallow.com/icons](https://glassmarshmallow.com/icons).

## Use

```html
<link rel="stylesheet" href="font/glassmarshmallow-icons.css">

<i class="gmi gmi-heart" aria-hidden="true"></i>
<i class="gmi gmi-heart-fill" aria-hidden="true"></i>
```

You can also copy any SVG from `icons/`.

## Structure

| Folder | Content |
| --- | --- |
| `source/` | The drawings, one Python file per category (`draw.py` writes them to `icons/`) |
| `icons/` | One SVG per icon (generated) |
| `font/` | `glassmarshmallow-icons.css`, the stylesheet with every icon (generated) |
| `build/` | `build-css.mjs`, which builds the stylesheet from `icons/` |

## Build

```sh
npm run build
```

## License

MIT · Designed by Sara Paez Yamuza
