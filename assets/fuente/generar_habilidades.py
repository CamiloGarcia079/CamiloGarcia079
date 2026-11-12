"""Genera habilidades.svg (habilidades blandas) con el mismo estilo del perfil.
Uso: python generar_habilidades.py carpeta_salida
"""
import os
import sys
from xml.sax.saxutils import escape as esc

OUT = sys.argv[1]
BG0, INK, MUTED, GOLD, TEAL = "#0a0e16", "#e8edf4", "#8b97a8", "#e8b04b", "#5eead4"
SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"

HABILIDADES = [
    ("M12 3l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.4 6.8 19.1l1-5.8L3.5 9.2l5.9-.9L12 3z",
     "Liderazgo y coordinación", "Organizo al equipo para que cada parte encaje y se entregue a tiempo.",
     "Coordiné la integración en el hackathon GUARDIAN."),
    ("M4 5h16v10H8l-4 4V5zM8 9h8M8 12h5",
     "Comunicación clara", "Explico lo técnico en palabras simples, sin importar quién escuche.",
     "Cada proyecto trae una guía fácil de seguir."),
    ("M8 11a3 3 0 1 0 0-6 3 3 0 0 0 0 6zm8 0a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM2 20c0-3 2.7-5 6-5s6 2 6 5M12 20c0-3 2.2-5 5-5 2.6 0 5 1.8 5 5",
     "Trabajo en equipo", "Me adapto a cómo trabaja el equipo y cuido los acuerdos.",
     "La mayoría de mis proyectos son en pareja o en equipo."),
    ("M12 4v16M4 12h16M7 7l10 10M17 7 7 17",
     "Aprendizaje rápido", "Aprendo herramientas nuevas por mi cuenta y las aplico pronto.",
     "En un año pasé de páginas web a sistemas seguros e IA."),
    ("M11 4a7 7 0 1 0 0 14 7 7 0 0 0 0-14zm9 16-4-4",
     "Resolución de problemas", "Cuando algo falla, busco la causa real y dejo escrita la solución.",
     "Resolví por qué DeliveryBot no guardaba los pedidos."),
    ("M5 12l4 4L19 6",
     "Responsabilidad y calidad", "Compruebo que lo que entrego funciona antes de darlo por listo.",
     "Más de 850 pruebas automáticas en mis proyectos."),
]


def wrap(texto, n):
    lineas, cur = [], ""
    for w in texto.split():
        if len(cur) + len(w) + 1 > n:
            lineas.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    lineas.append(cur)
    return lineas


W, cw, ch, gap = 1200, 388, 196, 18
H = ch * 2 + gap
s = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t d">'
     f'<title id="t">Habilidades blandas</title><desc id="d">{esc(". ".join(h[1] + ": " + h[2] for h in HABILIDADES))}</desc>'
     f'<style>.sans{{font-family:{SANS}}}.mono{{font-family:{MONO}}}'
     '@keyframes glow{0%,100%{opacity:.35}50%{opacity:1}}.gl{animation:glow 3s ease-in-out infinite}'
     '@media (prefers-reduced-motion:reduce){*{animation:none!important}}</style>')
for i, (icono, titulo, desc, ej) in enumerate(HABILIDADES):
    x = (i % 3) * (cw + (W - 3 * cw) / 2)
    y = (i // 3) * (ch + gap)
    acc = GOLD if i % 2 == 0 else TEAL
    s += f'<g transform="translate({x:.0f} {y})">'
    s += f'<rect x=".5" y=".5" width="{cw - 1}" height="{ch - 1}" rx="14" fill="{BG0}" stroke="#ffffff" stroke-opacity=".09"/>'
    s += f'<rect x="14" y="0" width="{cw - 28}" height="3" rx="1.5" fill="{acc}" class="gl" style="animation-delay:{i * .5}s"/>'
    s += f'<rect x="22" y="22" width="40" height="40" rx="10" fill="{acc}" fill-opacity=".13"/>'
    s += (f'<g transform="translate(32 32) scale(.84)"><path d="{icono}" fill="none" stroke="{acc}" stroke-width="2" '
          'stroke-linecap="round" stroke-linejoin="round"/></g>')
    s += f'<text x="76" y="48" class="sans" font-size="18" font-weight="700" fill="{INK}">{esc(titulo)}</text>'
    yy = 92
    for linea in wrap(desc, 44)[:2]:
        s += f'<text x="22" y="{yy}" class="sans" font-size="14.5" fill="{INK}" fill-opacity=".8">{esc(linea)}</text>'
        yy += 21
    s += f'<line x1="22" y1="142" x2="{cw - 22}" y2="142" stroke="#ffffff" stroke-opacity=".12" stroke-dasharray="4 4"/>'
    s += f'<text x="22" y="164" class="mono" font-size="10.5" fill="{TEAL}" letter-spacing="1">EJEMPLO REAL</text>'
    s += f'<text x="22" y="182" class="sans" font-size="13" fill="{MUTED}">{esc(ej)}</text>'
    s += '</g>'
s += '</svg>'
with open(os.path.join(OUT, 'habilidades.svg'), 'w', encoding='utf-8') as f:
    f.write(s)
print('ok')
