# Mallowglass Icons

Line and fill icons for [Mallowglass](../mallowglass). They use the same names as
Bootstrap Icons, with their own design: 24 × 24 grid, 1.5 px stroke and rounded ends.
They take the text color, so you change them with CSS.

## Use

```html
<link rel="stylesheet" href="font/mallowglass-icons.css">

<i class="mgi mgi-heart" aria-hidden="true"></i>
<i class="mgi mgi-heart-fill" aria-hidden="true"></i>
```

You can also copy any SVG from `icons/`.

## Structure

| Folder | Content |
| --- | --- |
| `source/` | The drawings, one Python file per category (`draw.py` writes them to `icons/`) |
| `icons/` | One SVG per icon (generated) |
| `font/` | `mallowglass-icons.css`, the stylesheet with every icon (generated) |
| `build/` | `build-css.mjs`, which builds the stylesheet from `icons/` |

## Build

```sh
npm run build
```

## License

MIT · Designed by Sara Paez Yamuza
