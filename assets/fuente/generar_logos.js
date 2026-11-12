// Genera lenguajes.svg y tecnologias.svg con logos de simple-icons.
// Uso: node gen_logos.js carpeta_salida
const fs = require('fs');
const path = require('path');
const si = require('simple-icons');
const OUT = process.argv[2];

const BG0 = '#0a0e16', INK = '#e8edf4', MUTED = '#8b97a8', GOLD = '#e8b04b', TEAL = '#5eead4';
const SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif";
const MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace";
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

// Colores oscuros no se ven sobre fondo oscuro: se reemplazan
const FIX = { siOpenjdk: '#f89820', siExpress: '#e8edf4', siGithub: '#e8edf4', siLangchain: '#5eead4',
  siSocketdotio: '#e8edf4', siJsonwebtokens: '#e8edf4', siApachemaven: '#e0485f' };
const color = (k) => FIX[k] || '#' + si[k].hex;

// Icono de base de datos para "SQL" (no tiene logo de marca)
const DB = 'M12 2C7 2 3 3.6 3 5.5v13C3 20.4 7 22 12 22s9-1.6 9-3.5v-13C21 3.6 17 2 12 2Zm0 2c4.4 0 7 1.3 7 1.5S16.4 7 12 7 5 5.7 5 5.5 7.6 4 12 4Zm7 14.5c0 .2-2.6 1.5-7 1.5s-7-1.3-7-1.5v-3.2C6.6 16.4 9.2 17 12 17s5.4-.6 7-1.7v3.2Zm0-6c0 .2-2.6 1.5-7 1.5s-7-1.3-7-1.5V9.3C6.6 10.4 9.2 11 12 11s5.4-.6 7-1.7v3.2Z';

const icon = (k, x, y, size, fill) => {
  const d = k === 'db' ? DB : si[k].path;
  return `<g transform="translate(${x} ${y}) scale(${size / 24})"><path d="${d}" fill="${fill}"/></g>`;
};

const CSS = `<style>
.sans{font-family:${SANS}}.mono{font-family:${MONO}}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-4px)}}
@keyframes ring{0%{opacity:.55}100%{opacity:0;transform:scale(1.5)}}
@keyframes sweep{from{transform:translateX(-220px)}to{transform:translateX(1400px)}}
.fl{animation:float 4s ease-in-out infinite}
.rg{transform-box:fill-box;transform-origin:center;animation:ring 3s ease-out infinite}
.sw{animation:sweep 6s ease-in-out infinite}
@media (prefers-reduced-motion:reduce){*{animation:none!important}}
</style>`;

// ---------------- Lenguajes principales ----------------
function lenguajes() {
  const L = [
    ['siOpenjdk', 'Java', 'Spring Boot · Swing · JDBC', '4 proyectos'],
    ['siPython', 'Python', 'LangChain · Streamlit · pytest', '3 proyectos'],
    ['siTypescript', 'TypeScript', 'Node.js · Express · React', '2 proyectos'],
    ['siJavascript', 'JavaScript', 'Web · n8n · Web Workers', '4 proyectos'],
    ['db', 'SQL', 'MySQL · PostgreSQL', '6 proyectos'],
  ];
  const W = 1200, H = 250, tw = 224, gap = (W - 5 * tw) / 4;
  let s = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-labelledby="t"><title id="t">Lenguajes que domino: Java, Python, TypeScript, JavaScript y SQL</title>${CSS}
<defs><linearGradient id="sh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".06"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="c"><rect width="${W}" height="${H}" rx="16"/></clipPath></defs>`;
  L.forEach(([k, nombre, sub, usado], i) => {
    const x = i * (tw + gap), col = k === 'db' ? TEAL : color(k);
    const tile = `<rect x=".5" y=".5" width="${tw - 1}" height="${H - 1}" rx="16" fill="${BG0}" stroke="${col}" stroke-opacity=".35"/>
<rect x="0" y="0" width="${tw}" height="4" rx="2" fill="${col}"/>
<radialGradient id="g${i}" cx=".5" cy=".3" r=".6"><stop offset="0" stop-color="${col}" stop-opacity=".18"/><stop offset="1" stop-color="${col}" stop-opacity="0"/></radialGradient>
<rect width="${tw}" height="${H}" rx="16" fill="url(#g${i})"/>
<g class="fl" style="animation-delay:${i * .5}s">
<circle cx="${tw / 2}" cy="82" r="40" fill="${col}" fill-opacity=".10" stroke="${col}" stroke-opacity=".4"/>
<circle cx="${tw / 2}" cy="82" r="40" fill="none" stroke="${col}" class="rg" style="animation-delay:${i * .6}s"/>
${icon(k, tw / 2 - 22, 60, 44, col)}
</g>
<text x="${tw / 2}" y="160" class="sans" font-size="22" font-weight="700" fill="${INK}" text-anchor="middle">${nombre}</text>
<text x="${tw / 2}" y="186" class="mono" font-size="11.5" fill="${MUTED}" text-anchor="middle">${esc(sub)}</text>
<rect x="${tw / 2 - 52}" y="204" width="104" height="24" rx="12" fill="${col}" fill-opacity=".12"/>
<text x="${tw / 2}" y="220" class="mono" font-size="11" fill="${col}" text-anchor="middle">${usado}</text>`;
    s += `<g transform="translate(${x} 0)">${tile}</g>`;
    // Versión suelta de cada lenguaje, para enlazarla a su proyecto en el README
    const suelto = tile.replace(`>${usado}</text>`, '>ver código &#8599;</text>');
    fs.writeFileSync(path.join(OUT, `lang-${nombre.toLowerCase()}.svg`),
      `<svg xmlns="http://www.w3.org/2000/svg" width="${tw}" height="${H}" viewBox="0 0 ${tw} ${H}" role="img" aria-labelledby="t"><title id="t">${nombre}: ${esc(sub)}</title>${CSS}${suelto}</svg>`);
  });
  s += `</svg>`;
  fs.writeFileSync(path.join(OUT, 'lenguajes.svg'), s);
}

// ---------------- Tecnologías por categoría ----------------
function tecnologias() {
  const G = [
    ['Frameworks', GOLD, [['siSpringboot', 'Spring Boot'], ['siSpringsecurity', 'Spring Security'], ['siJsonwebtokens', 'JWT'], ['siExpress', 'Express'], ['siReact', 'React'], ['siStreamlit', 'Streamlit']]],
    ['Automatización e IA', TEAL, [['siN8n', 'n8n'], ['siTelegram', 'Telegram Bot API'], ['siLangchain', 'LangChain'], ['siGooglegemini', 'Gemini'], ['siPydantic', 'Pydantic']]],
    ['Bases de datos', GOLD, [['siMysql', 'MySQL'], ['siPostgresql', 'PostgreSQL'], ['siFlyway', 'Flyway'], ['siGooglesheets', 'Google Sheets']]],
    ['Web', TEAL, [['siHtml5', 'HTML5'], ['siCss3', 'CSS3'], ['siNodedotjs', 'Node.js'], ['siSocketdotio', 'Socket.IO']]],
    ['Calidad y entrega', GOLD, [['siJunit5', 'JUnit 5'], ['siPytest', 'pytest'], ['siDocker', 'Docker'], ['siPostman', 'Postman'], ['siSwagger', 'Swagger'], ['siApachemaven', 'Maven'], ['siGit', 'Git'], ['siGithub', 'GitHub']]],
  ];
  const W = 1200, rowH = 78, H = 24 + rowH * G.length;
  let s = `<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" role="img" aria-labelledby="t d"><title id="t">Tecnologías por categoría</title><desc id="d">${esc(G.map(([n, , it]) => n + ': ' + it.map((x) => x[1]).join(', ')).join('. '))}</desc>${CSS}
<rect x=".5" y=".5" width="${W - 1}" height="${H - 1}" rx="16" fill="${BG0}" stroke="#ffffff" stroke-opacity=".08"/>`;
  G.forEach(([grupo, acc, items], gi) => {
    const y = 12 + gi * rowH;
    s += `<rect x="24" y="${y + 22}" width="4" height="34" rx="2" fill="${acc}"/>
<text x="42" y="${y + 45}" class="sans" font-size="16" font-weight="700" fill="${INK}">${esc(grupo)}</text>`;
    let x = 250;
    items.forEach(([k, nombre], ii) => {
      const w = 54 + nombre.length * 8.2, col = color(k);
      s += `<g class="fl" style="animation-delay:${(gi * 6 + ii) * .23 % 4}s;animation-duration:5s">
<rect x="${x}" y="${y + 18}" width="${w.toFixed(0)}" height="42" rx="10" fill="${col}" fill-opacity=".08" stroke="${col}" stroke-opacity=".38"/>
${icon(k, x + 12, y + 29, 20, col)}
<text x="${x + 42}" y="${y + 44}" class="mono" font-size="13" fill="${INK}">${esc(nombre)}</text></g>`;
      x += w + 10;
    });
    if (gi < G.length - 1) s += `<line x1="24" y1="${y + rowH - 1}" x2="${W - 24}" y2="${y + rowH - 1}" stroke="#ffffff" stroke-opacity=".05"/>`;
  });
  s += '</svg>';
  fs.writeFileSync(path.join(OUT, 'tecnologias.svg'), s);
}

lenguajes();
tecnologias();

// Exporta también los trazos para el portafolio
const usados = ['siOpenjdk', 'siPython', 'siTypescript', 'siJavascript', 'siSpringboot', 'siSpringsecurity', 'siJsonwebtokens', 'siExpress', 'siReact', 'siStreamlit', 'siN8n', 'siTelegram', 'siLangchain', 'siGooglegemini', 'siPydantic', 'siMysql', 'siPostgresql', 'siFlyway', 'siGooglesheets', 'siHtml5', 'siCss3', 'siNodedotjs', 'siSocketdotio', 'siJunit5', 'siPytest', 'siDocker', 'siPostman', 'siSwagger', 'siApachemaven', 'siGit', 'siGithub'];
const mapa = { db: { d: DB, c: TEAL } };
usados.forEach((k) => { mapa[k.slice(2)] = { d: si[k].path, c: color(k) }; });
if (process.argv[3]) fs.writeFileSync(process.argv[3], '/* Logos de simple-icons (licencia CC0) */\nconst LOGOS = ' + JSON.stringify(mapa) + ';\n');
console.log('ok');
