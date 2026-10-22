// Genera font/glassmarshmallow-icons.css a partir de los SVG de icons/.
// Cada icono se usa con <i class="gmi gmi-nombre" aria-hidden="true"></i> y toma el color del texto.
// Uso: node build/build-css.mjs
import { readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const svgDir = join(root, 'icons');
const { version } = JSON.parse(readFileSync(join(root, 'package.json'), 'utf8'));
const names = readdirSync(svgDir).filter((f) => f.endsWith('.svg')).map((f) => f.slice(0, -4)).sort();

const rules = names.map((name) => {
  const svg = readFileSync(join(svgDir, `${name}.svg`), 'utf8').trim();
  const uri = `data:image/svg+xml,${encodeURIComponent(svg)}`;
  return `.gmi-${name} { --gmi-src: url("${uri}"); }`;
});

const css = `/*!
 * GlassMarshmallow icons v${version} · Licencia MIT
 * Diseñados por Sara Paez Yamuza. Archivo generado con build/build-css.mjs: no editar a mano.
 */
/* En la subcapa de los iconos de GlassMarshmallow (@layer): el CSS propio, sin capa, gana siempre, y los componentes
   y las utilidades del framework los ajustan (van en subcapas posteriores). El orden, el mismo que el del framework */
@layer glassmarshmallow.tokens, glassmarshmallow.base, glassmarshmallow.layout, glassmarshmallow.icons, glassmarshmallow.components, glassmarshmallow.theme, glassmarshmallow.utilities, glassmarshmallow.extra;
@layer glassmarshmallow.icons {
.gmi {
  display: inline-block;
  width: 1em;
  height: 1em;
  flex-shrink: 0;
  vertical-align: -.125em;
  background-color: currentColor;
  -webkit-mask: var(--gmi-src) no-repeat center / contain;
  mask: var(--gmi-src) no-repeat center / contain;
}
${rules.join('\n')}
}
`;

writeFileSync(join(root, 'font', 'glassmarshmallow-icons.css'), css);
writeFileSync(join(root, 'icons.json'), JSON.stringify(names, null, 2) + '\n');
console.log(`${names.length} iconos → font/glassmarshmallow-icons.css`);
