"""Genera tarjeta.svg: la tarjeta de presentación digital del perfil.
Necesita la librería qrcode (pip install qrcode).
Uso: python generar_tarjeta.py carpeta_salida
"""
import os
import sys
import qrcode
from xml.sax.saxutils import escape as esc

OUT = sys.argv[1]
BG0, BG1, INK, MUTED, GOLD, TEAL = '#0b0f16', '#11171f', '#eef1f5', '#8e98a7', '#c9a04f', '#c9a04f'
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
URL = 'https://camilogarcia079.github.io/portafolio/'

# Logo: la misma C de tres tramos del portafolio (viewBox 64)
TRAMOS = [('M39.89 15.82 A18 18 0 0 0 24.11 15.82', '#e8b04b'),
          ('M19.05 19.50 A18 18 0 0 0 19.05 44.50', '#c5c785'),
          ('M24.11 48.18 A18 18 0 0 0 39.89 48.18', '#5eead4')]
NODO = (45.79, 20.43)

DATOS = [('FORMACIÓN', 'CampusLands · un año intensivo · 2026'), ('PRÓXIMO PASO', 'Etapa productiva · Globant · dic 2026'),
         ('ENFOQUE', 'Automatización, bots y aplicaciones web'), ('STACK', 'Java · Spring Boot · Python · TypeScript'),
         ('IDIOMAS', 'Español nativo · Inglés A2 · Portugués A1'), ('UBICACIÓN', 'Bucaramanga, Colombia')]
CONTACTO = [('correo', 'kaliko2411@gmail.com'), ('linkedin', 'in/camilo-andrés-garcía-almeida-7570693b7'),
            ('web', 'camilogarcia079.github.io/portafolio')]
ICONOS = {  # trazos de 24x24
    'correo': 'M3 6h18v12H3zM3 7l9 6 9-6',
    'linkedin': 'M4 9h4v11H4zM6 4.5a2 2 0 1 1 0 4 2 2 0 0 1 0-4zM10 9h4v1.6c.6-1 1.8-1.9 3.6-1.9 3 0 3.4 2 3.4 4.6V20h-4v-5.6c0-1.3 0-2.6-1.6-2.6s-1.4 1.3-1.4 2.6V20h-4z',
    'web': 'M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18zM3 12h18M12 3c2.5 2.6 3.7 5.6 3.7 9S14.5 18.4 12 21c-2.5-2.6-3.7-5.6-3.7-9S9.5 5.6 12 3z',
}

W, H = 1200, 600
s = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">
<title id="t">Tarjeta de presentación de Camilo Andrés García Almeida</title>
<desc id="d">Junior Developer. {esc('. '.join(f'{k}: {v}' for k, v in DATOS))}. Correo kaliko2411@gmail.com. Portafolio {URL}</desc>
<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG1}"/><stop offset="1" stop-color="{BG0}"/></linearGradient>
<linearGradient id="lado" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#16202f"/><stop offset="1" stop-color="#0d131d"/></linearGradient>
<linearGradient id="oro" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{GOLD}"/><stop offset="1" stop-color="{TEAL}"/></linearGradient>
<linearGradient id="brillo" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".07"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<pattern id="puntos" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="#fff" fill-opacity=".05"/></pattern>
<clipPath id="tarjeta"><rect x="20" y="20" width="{W - 40}" height="{H - 40}" rx="26"/></clipPath>
</defs>
<style>
.sans{{font-family:{SANS}}}.mono{{font-family:{MONO}}}
@keyframes barrido{{from{{transform:translateX(-500px) skewX(-20deg)}}to{{transform:translateX(1500px) skewX(-20deg)}}}}
@keyframes paso{{0%,100%{{opacity:1}}40%{{opacity:.25}}}}
@keyframes latido{{50%{{transform:scale(1.2)}}}}
.br{{animation:barrido 7s ease-in-out infinite}}
.tr{{animation:paso 3.6s ease infinite}}
.nd{{transform-box:fill-box;transform-origin:center;animation:latido 3.6s ease infinite;animation-delay:.9s}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
</style>
<rect x="26" y="32" width="{W - 52}" height="{H - 40}" rx="26" fill="#000" fill-opacity=".25"/>
<g clip-path="url(#tarjeta)">
<rect x="20" y="20" width="{W - 40}" height="{H - 40}" fill="url(#bg)"/>
<rect x="20" y="20" width="{W - 40}" height="{H - 40}" fill="url(#puntos)"/>
<rect x="20" y="20" width="400" height="{H - 40}" fill="url(#lado)"/>
<line x1="420" y1="20" x2="420" y2="{H - 20}" stroke="#fff" stroke-opacity=".07"/>
<rect x="20" y="20" width="{W - 40}" height="4" fill="url(#oro)"/>
'''
# Lado izquierdo: logo grande, nombre corto y rol
s += ('<g transform="translate(140 125) scale(2.5)">'
      '<path d="M46.97 20.30 A19 19 0 1 0 46.97 43.70 L41.46 39.39 A12 12 0 1 1 41.46 24.61 Z" fill="#eef1f5"/>'
      '<rect x="43" y="34" width="7" height="7" fill="#c9a04f"/></g>')
s += f'''<text x="220" y="380" class="sans" font-size="15" font-weight="600" fill="{MUTED}" text-anchor="middle" letter-spacing="4">CAMILO GARCÍA</text>
<rect x="138" y="400" width="164" height="32" rx="16" fill="{GOLD}" fill-opacity=".12" stroke="{GOLD}" stroke-opacity=".5"/>
<text x="220" y="421" class="mono" font-size="13" fill="{GOLD}" text-anchor="middle">Junior Developer</text>
<text x="220" y="520" class="mono" font-size="11" fill="{MUTED}" text-anchor="middle" fill-opacity=".7">automatización · bots · web</text>
'''
# Lado derecho: nombre, título y datos
s += f'''<text x="470" y="108" class="sans" font-size="40" font-weight="700" fill="{INK}" letter-spacing="-.5">Camilo Andrés García Almeida</text>
<text x="470" y="142" class="sans" font-size="17" fill="url(#oro)" font-weight="600">Técnico en Desarrollo de Software e Inteligencia Artificial</text>
<line x1="470" y1="170" x2="{W - 60}" y2="170" stroke="#fff" stroke-opacity=".08"/>
'''
for i, (k, v) in enumerate(DATOS):
    x = 470 + (i % 2) * 340
    y = 210 + (i // 2) * 62
    s += f'<text x="{x}" y="{y}" class="mono" font-size="10.5" fill="{TEAL}" letter-spacing="1.5">{esc(k)}</text>'
    s += f'<text x="{x}" y="{y + 24}" class="sans" font-size="15" fill="{INK}">{esc(v)}</text>'
s += f'<line x1="470" y1="405" x2="{W - 60}" y2="405" stroke="#fff" stroke-opacity=".08"/>'
for i, (ic, txt) in enumerate(CONTACTO):
    y = 445 + i * 36
    s += (f'<g transform="translate(470 {y - 16}) scale(.85)"><path d="{ICONOS[ic]}" fill="none" stroke="{GOLD}" '
          f'stroke-width="1.8" stroke-linejoin="round"/></g>')
    s += f'<text x="502" y="{y}" class="mono" font-size="14" fill="{INK}" fill-opacity=".88">{esc(txt)}</text>'

# Código QR al portafolio
q = qrcode.QRCode(border=0, error_correction=qrcode.constants.ERROR_CORRECT_M)
q.add_data(URL)
q.make()
m = q.get_matrix()
n = len(m)
tam, qx, qy = 128, W - 60 - 128 - 16, 412
celda = tam / n
s += f'<rect x="{qx - 10}" y="{qy - 10}" width="{tam + 20}" height="{tam + 20}" rx="12" fill="#f6f4ef"/>'
d = ''.join(f'M{qx + c * celda:.2f} {qy + r * celda:.2f}h{celda:.2f}v{celda:.2f}h-{celda:.2f}z'
            for r in range(n) for c in range(n) if m[r][c])
s += f'<path d="{d}" fill="#0a0e16"/>'
s += f'<text x="{qx + tam / 2}" y="{qy + tam + 30}" class="mono" font-size="10.5" fill="{MUTED}" text-anchor="middle">escanea · portafolio</text>'

s += f'</g><rect x="20.5" y="20.5" width="{W - 41}" height="{H - 41}" rx="26" fill="none" stroke="#fff" stroke-opacity=".1"/></svg>'

with open(os.path.join(OUT, 'tarjeta.svg'), 'w', encoding='utf-8') as f:
    f.write(s)
print('ok')
