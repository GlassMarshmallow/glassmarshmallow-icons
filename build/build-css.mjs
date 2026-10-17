// Genera font/mallowglass-icons.css a partir de los SVG de icons/.
// Cada icono se usa con <i class="mgi mgi-nombre" aria-hidden="true"></i> y toma el color del texto.
// Uso: node build/build-css.mjs
import { readdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const svgDir = join(root, 'icons');
const names = readdirSync(svgDir).filter((f) => f.endsWith('.svg')).map((f) => f.slice(0, -4)).sort();

const rules = names.map((name) => {
  const svg = readFileSync(join(svgDir, `${name}.svg`), 'utf8').trim();
  const uri = `data:image/svg+xml,${encodeURIComponent(svg)}`;
  return `.mgi-${name} { --mgi-src: url("${uri}"); }`;
});

const css = `/*!
 * Mallowglass icons v0.1 · Licencia MIT
 * Diseñados por Sara Paez Yamuza. Archivo generado con build/build-css.mjs: no editar a mano.
 */
.mgi {
  display: inline-block;
  width: 1em;
  height: 1em;
  flex-shrink: 0;
  vertical-align: -.125em;
  background-color: currentColor;
  -webkit-mask: var(--mgi-src) no-repeat center / contain;
  mask: var(--mgi-src) no-repeat center / contain;
}
${rules.join('\n')}
`;

writeFileSync(join(root, 'font', 'mallowglass-icons.css'), css);
writeFileSync(join(root, 'icons.json'), JSON.stringify(names, null, 2) + '\n');
console.log(`${names.length} iconos → font/mallowglass-icons.css`);
