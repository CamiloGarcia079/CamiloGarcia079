"""Genera los SVG del README del perfil de CamiloGarcia079.

Paleta: tinta oscura, dorado como acento principal y verde agua como secundario.
Todo usa fuentes del sistema (GitHub no carga fuentes externas dentro de un <img>).
"""
import os
import sys
from xml.sax.saxutils import escape as esc

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)

BG0, BG1 = "#0a0e16", "#121a28"
INK = "#e8edf4"
MUTED = "#8b97a8"
GOLD = "#e8b04b"
TEAL = "#5eead4"
LINE = "#ffffff"

SANS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"

BASE_CSS = f"""
.sans{{font-family:{SANS}}}
.mono{{font-family:{MONO}}}
@keyframes rise{{from{{opacity:0;transform:translateY(8px)}}to{{opacity:1;transform:translateY(0)}}}}
@keyframes draw{{to{{stroke-dashoffset:0}}}}
@keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}
@keyframes pulse{{0%{{opacity:.7;transform:scale(1)}}100%{{opacity:0;transform:scale(3)}}}}
@keyframes shimmer{{from{{transform:translateX(-100%)}}to{{transform:translateX(100%)}}}}
@keyframes glow{{0%,100%{{opacity:.35}}50%{{opacity:1}}}}
.rise{{animation:rise .7s ease backwards}}
.cur{{animation:blink 1.1s steps(1) infinite}}
.ring{{transform-box:fill-box;transform-origin:center;animation:pulse 2s ease-out infinite}}
.glow{{animation:glow 2.4s ease-in-out infinite}}
@media (prefers-reduced-motion:reduce){{*{{animation:none!important}}}}
"""


def write(name, body):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(body)


def svg_open(w, h, title, desc=""):
    d = f'<desc id="d">{esc(desc)}</desc>' if desc else ""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img" aria-labelledby="t{" d" if desc else ""}"><title id="t">{esc(title)}</title>{d}')


# ---------------------------------------------------------------- banner
def banner():
    W, H = 1200, 420
    s = svg_open(W, H, "Camilo Andrés García Almeida, Junior Developer",
                 "Técnico en Desarrollo de Software e Inteligencia Artificial. Automatizaciones, bots y desarrollo web. "
                 "Próxima etapa productiva en Globant, diciembre de 2026.")
    s += f"""<defs>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG0}"/><stop offset="1" stop-color="{BG1}"/></linearGradient>
<linearGradient id="gold" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{GOLD}"/><stop offset="1" stop-color="{TEAL}"/></linearGradient>
<radialGradient id="halo" cx=".78" cy=".45" r=".5"><stop offset="0" stop-color="{TEAL}" stop-opacity=".12"/><stop offset="1" stop-color="{TEAL}" stop-opacity="0"/></radialGradient>
<radialGradient id="halo2" cx=".05" cy="1" r=".6"><stop offset="0" stop-color="{GOLD}" stop-opacity=".10"/><stop offset="1" stop-color="{GOLD}" stop-opacity="0"/></radialGradient>
<pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="{LINE}" fill-opacity=".06"/></pattern>
<clipPath id="clip"><rect width="{W}" height="{H}" rx="18"/></clipPath>
<clipPath id="type"><rect x="64" y="226" width="0" height="34"><animate attributeName="width" from="0" to="620" dur="2.2s" begin=".9s" fill="freeze" calcMode="spline" keySplines=".4 0 .2 1" keyTimes="0;1"/></rect></clipPath>
</defs>
<style>{BASE_CSS}
.flow{{stroke-dasharray:6 8;animation:dash 1.4s linear infinite}}
@keyframes dash{{to{{stroke-dashoffset:-28}}}}
</style>
<g clip-path="url(#clip)">
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<rect width="{W}" height="{H}" fill="url(#dots)"/>
<rect width="{W}" height="{H}" fill="url(#halo)"/>
<rect width="{W}" height="{H}" fill="url(#halo2)"/>
<rect x="18" y="0" width="{W - 36}" height="3" fill="url(#gold)"/>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="{LINE}" stroke-opacity=".08"/>

<!-- texto -->
<g class="rise" style="animation-delay:.1s">
<rect x="64" y="56" width="236" height="28" rx="14" fill="{GOLD}" fill-opacity=".10" stroke="{GOLD}" stroke-opacity=".45"/>
<circle cx="84" cy="70" r="4" fill="{GOLD}"/><circle cx="84" cy="70" r="4" fill="{GOLD}" class="ring"/>
<text x="98" y="75" class="mono" font-size="13" fill="{GOLD}" letter-spacing=".5">JUNIOR DEVELOPER · 2026</text>
</g>
<text x="62" y="146" class="sans rise" style="animation-delay:.3s" font-size="46" font-weight="700" fill="{INK}" letter-spacing="-.5">Camilo Andrés</text>
<text x="62" y="198" class="sans rise" style="animation-delay:.45s" font-size="46" font-weight="700" fill="url(#gold)" letter-spacing="-.5">García Almeida</text>
<g clip-path="url(#type)">
<text x="64" y="250" class="sans" font-size="20" fill="{INK}" fill-opacity=".92">Técnico en Desarrollo de Software e Inteligencia Artificial</text>
</g>
<text x="64" y="290" class="mono rise" style="animation-delay:2.9s" font-size="15" fill="{TEAL}">&gt; automatizaciones · bots · desarrollo web<tspan class="cur" fill="{TEAL}">_</tspan></text>
<g class="rise" style="animation-delay:3.2s">
<line x1="64" y1="326" x2="640" y2="326" stroke="{LINE}" stroke-opacity=".08"/>
<text x="64" y="358" class="mono" font-size="13" fill="{MUTED}">Bucaramanga, Colombia</text>
<text x="250" y="358" class="mono" font-size="13" fill="{MUTED}">Próximo paso:</text>
<text x="360" y="358" class="mono" font-size="13" fill="{INK}" font-weight="700">etapa productiva en Globant · dic 2026</text>
</g>

<!-- flujo de automatizacion -->
<g transform="translate(720,70)">
<rect x="0" y="0" width="420" height="280" rx="14" fill="#0d131e" fill-opacity=".85" stroke="{LINE}" stroke-opacity=".08"/>
<text x="20" y="30" class="mono" font-size="12" fill="{MUTED}">workflow / pedido_nuevo</text>
<circle cx="380" cy="26" r="4" fill="{TEAL}" class="glow"/>
<text x="350" y="30" class="mono" font-size="11" fill="{TEAL}" text-anchor="end">activo</text>
<line x1="0" y1="44" x2="420" y2="44" stroke="{LINE}" stroke-opacity=".06"/>
"""
    # nodos: (x, y, etiqueta, sub, color)
    nodes = [
        (30, 80, "Trigger", "webhook", GOLD),
        (230, 80, "Lógica", "código JS", TEAL),
        (30, 190, "API", "REST / LLM", TEAL),
        (230, 190, "Datos", "SQL / Sheets", GOLD),
    ]
    paths = [
        "M190 105 C210 105 210 105 230 105",
        "M310 130 C310 160 110 150 110 190",
        "M190 215 C210 215 210 215 230 215",
    ]
    for i, p in enumerate(paths):
        s += f'<path d="{p}" fill="none" stroke="{LINE}" stroke-opacity=".14" stroke-width="2"/>'
        s += f'<path id="p{i}" d="{p}" fill="none" stroke="{TEAL if i % 2 else GOLD}" stroke-opacity=".7" stroke-width="2" class="flow"/>'
    for i, (x, y, lab, sub, col) in enumerate(nodes):
        s += f"""<g class="rise" style="animation-delay:{.6 + i * .25:.2f}s">
<rect x="{x}" y="{y}" width="160" height="50" rx="10" fill="#141c2b" stroke="{col}" stroke-opacity=".55"/>
<rect x="{x}" y="{y}" width="4" height="50" rx="2" fill="{col}"/>
<text x="{x + 18}" y="{y + 22}" class="sans" font-size="15" font-weight="700" fill="{INK}">{esc(lab)}</text>
<text x="{x + 18}" y="{y + 40}" class="mono" font-size="11" fill="{MUTED}">{esc(sub)}</text>
<circle cx="{x + 142}" cy="{y + 25}" r="4" fill="{col}" class="glow" style="animation-delay:{i * .5:.1f}s"/>
</g>"""
    for i in range(3):
        col = TEAL if i % 2 else GOLD
        s += (f'<circle r="5" fill="{col}"><animateMotion dur="2.4s" begin="{i * .8:.1f}s" repeatCount="indefinite">'
              f'<mpath href="#p{i}"/></animateMotion></circle>')
    s += f"""<text x="20" y="266" class="mono" font-size="11" fill="{MUTED}">4 nodos · última ejecución: <tspan fill="{TEAL}">ok</tspan></text>
</g>
</g></svg>"""
    write("banner.svg", s)


# ---------------------------------------------------------------- section headers
def section(fname, num, title, hint):
    W, H = 1200, 76
    s = svg_open(W, H, title)
    tw = 40 + len(title) * 14.5
    s += f"""<defs><linearGradient id="g" gradientUnits="userSpaceOnUse" x1="{42 + tw}" y1="0" x2="{W - 50 - len(hint) * 8}" y2="0"><stop offset="0" stop-color="{GOLD}"/><stop offset="1" stop-color="{TEAL}" stop-opacity=".15"/></linearGradient></defs>
<style>{BASE_CSS}
.ln{{stroke-dasharray:1200;stroke-dashoffset:1200;animation:draw 1.6s ease .2s forwards}}
</style>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="12" fill="{BG0}" stroke="{LINE}" stroke-opacity=".08"/>
<rect x="0" y="18" width="4" height="40" rx="2" fill="{GOLD}"/>
<text x="24" y="46" class="mono rise" font-size="15" fill="{GOLD}">{num}</text>
<text x="60" y="47" class="sans rise" style="animation-delay:.1s" font-size="26" font-weight="700" fill="{INK}">{esc(title)}</text>
<text x="{W - 24}" y="46" class="mono rise" style="animation-delay:.4s" font-size="13" fill="{MUTED}" text-anchor="end">{esc(hint)}</text>
<line x1="{42 + tw}" y1="40" x2="{W - 50 - len(hint) * 8}" y2="40" stroke="url(#g)" stroke-width="1.5" class="ln"/>
<circle r="3" fill="{TEAL}"><animateMotion dur="4s" repeatCount="indefinite" path="M{42 + tw} 40 H{W - 50 - len(hint) * 8}"/></circle>
</svg>"""
    write(fname, s)


# ---------------------------------------------------------------- project cards
def wrap(text, n):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > n:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    lines.append(cur)
    return lines


def card(fname, tag, title, desc, metric, chips, accent, role=None):
    W, H = 600, 250
    s = svg_open(W, H, f"{title}: {desc}")
    s += f"""<defs>
<linearGradient id="a" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{accent}"/><stop offset="1" stop-color="{accent}" stop-opacity=".1"/></linearGradient>
<linearGradient id="sh" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".55"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<radialGradient id="gl" cx="1" cy="0" r=".8"><stop offset="0" stop-color="{accent}" stop-opacity=".16"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient>
<clipPath id="c"><rect width="{W}" height="{H}" rx="14"/></clipPath>
</defs>
<style>{BASE_CSS}
.sh{{animation:shimmer 3.5s ease-in-out infinite}}
</style>
<g clip-path="url(#c)">
<rect width="{W}" height="{H}" fill="{BG0}"/>
<rect width="{W}" height="{H}" fill="url(#gl)"/>
<rect width="{W}" height="3" fill="url(#a)"/>
<rect width="{W}" height="3" fill="url(#sh)" class="sh"/>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="14" fill="none" stroke="{LINE}" stroke-opacity=".09"/>
<text x="26" y="40" class="mono" font-size="12" fill="{accent}" letter-spacing="1">{esc(tag)}</text>
<text x="{W - 26}" y="40" class="mono" font-size="12" fill="{MUTED}" text-anchor="end">ver repositorio &#8594;</text>
<text x="26" y="78" class="sans" font-size="25" font-weight="700" fill="{INK}">{esc(title)}</text>
"""
    y = 106
    for ln in wrap(desc, 62)[:2]:
        s += f'<text x="26" y="{y}" class="sans" font-size="15" fill="{INK}" fill-opacity=".78">{esc(ln)}</text>'
        y += 22
    if role:
        s += f'<text x="26" y="{y + 2}" class="sans" font-size="13" fill="{MUTED}" font-style="italic">{esc(role)}</text>'
    s += f'<text x="26" y="178" class="mono" font-size="12.5" fill="{TEAL}">{esc(metric)}</text>'
    x = 26
    for c in chips:
        w = 18 + len(c) * 7.4
        s += (f'<g><rect x="{x}" y="198" width="{w:.0f}" height="28" rx="7" fill="{LINE}" fill-opacity=".05" stroke="{LINE}" stroke-opacity=".10"/>'
              f'<text x="{x + w / 2:.0f}" y="217" class="mono" font-size="12" fill="{INK}" fill-opacity=".85" text-anchor="middle">{esc(c)}</text></g>')
        x += w + 8
    s += "</g></svg>"
    write(fname, s)


# ---------------------------------------------------------------- stack
def stack():
    groups = [
        ("Backend", GOLD, ["Java 21", "Spring Boot", "Spring Security · JWT", "Node.js · Express", "Python"]),
        ("Automatización e IA", TEAL, ["n8n", "Telegram Bot API", "LangChain", "Gemini", "Agentes con tools"]),
        ("Frontend", GOLD, ["JavaScript", "TypeScript", "React", "HTML", "CSS"]),
        ("Datos", TEAL, ["MySQL", "PostgreSQL", "Flyway", "Google Sheets", "JPA · JDBC"]),
        ("Calidad y entrega", GOLD, ["JUnit 5", "pytest", "Docker", "Postman · Swagger", "Git · GitHub"]),
    ]
    W = 1200
    rowh = 62
    H = 30 + rowh * len(groups)
    s = svg_open(W, H, "Tecnologías",
                 "Backend: Java, Spring Boot, Spring Security con JWT, Node.js con Express y Python. "
                 "Automatización e IA: n8n, Telegram Bot API, LangChain, Gemini y agentes con herramientas. "
                 "Frontend: JavaScript, TypeScript, React, HTML y CSS. Datos: MySQL, PostgreSQL, Flyway, Google Sheets, JPA y JDBC. "
                 "Calidad: JUnit 5, pytest, Docker, Postman, Swagger, Git y GitHub.")
    s += f"<style>{BASE_CSS}</style>"
    s += f'<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="14" fill="{BG0}" stroke="{LINE}" stroke-opacity=".08"/>'
    for gi, (name, col, items) in enumerate(groups):
        y = 20 + gi * rowh
        d = gi * .15
        s += f'<g class="rise" style="animation-delay:{d:.2f}s">'
        s += f'<rect x="24" y="{y + 12}" width="4" height="30" rx="2" fill="{col}"/>'
        s += f'<text x="40" y="{y + 33}" class="sans" font-size="16" font-weight="700" fill="{INK}">{esc(name)}</text>'
        x = 260
        for it in items:
            w = 26 + len(it) * 8
            s += (f'<rect x="{x}" y="{y + 10}" width="{w:.0f}" height="34" rx="8" fill="{col}" fill-opacity=".07" stroke="{col}" stroke-opacity=".35"/>'
                  f'<text x="{x + w / 2:.0f}" y="{y + 32}" class="mono" font-size="13" fill="{INK}" text-anchor="middle">{esc(it)}</text>')
            x += w + 10
        s += "</g>"
        if gi < len(groups) - 1:
            s += f'<line x1="24" y1="{y + rowh - 2}" x2="{W - 24}" y2="{y + rowh - 2}" stroke="{LINE}" stroke-opacity=".05"/>'
    s += "</svg>"
    write("stack.svg", s)


# ---------------------------------------------------------------- enfoque (como trabajo una automatizacion)
def enfoque():
    W, H = 1200, 200
    steps = [
        ("01", "Entender el proceso", "qué se hace a mano hoy"),
        ("02", "Definir el disparador", "mensaje, formulario o evento"),
        ("03", "Programar la lógica", "código simple y probado"),
        ("04", "Integrar y registrar", "APIs, base de datos, avisos"),
    ]
    s = svg_open(W, H, "Cómo abordo una automatización",
                 "Cuatro pasos: entender el proceso, definir el disparador, programar la lógica e integrar y registrar.")
    s += f"""<defs><linearGradient id="g" gradientUnits="userSpaceOnUse" x1="80" y1="0" x2="1120" y2="0"><stop offset="0" stop-color="{GOLD}"/><stop offset="1" stop-color="{TEAL}"/></linearGradient></defs>
<style>{BASE_CSS}
.ln{{stroke-dasharray:1100;stroke-dashoffset:1100;animation:draw 2.4s ease .3s forwards}}
</style>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="14" fill="{BG0}" stroke="{LINE}" stroke-opacity=".08"/>
<line x1="80" y1="70" x2="1120" y2="70" stroke="{LINE}" stroke-opacity=".08" stroke-width="2"/>
<line x1="80" y1="70" x2="1120" y2="70" stroke="url(#g)" stroke-width="2" class="ln"/>
<circle r="5" fill="{TEAL}"><animateMotion dur="5s" repeatCount="indefinite" path="M80 70 H1120"/></circle>
"""
    for i, (n, t, sub) in enumerate(steps):
        cx = 150 + i * 300
        col = GOLD if i % 2 == 0 else TEAL
        s += f"""<g class="rise" style="animation-delay:{.3 + i * .35:.2f}s">
<circle cx="{cx}" cy="70" r="22" fill="#141c2b" stroke="{col}" stroke-width="2"/>
<text x="{cx}" y="75" class="mono" font-size="13" fill="{col}" text-anchor="middle" font-weight="700">{n}</text>
<text x="{cx}" y="128" class="sans" font-size="17" font-weight="700" fill="{INK}" text-anchor="middle">{esc(t)}</text>
<text x="{cx}" y="152" class="mono" font-size="12.5" fill="{MUTED}" text-anchor="middle">{esc(sub)}</text>
</g>"""
    s += "</svg>"
    write("enfoque.svg", s)


# ---------------------------------------------------------------- buttons
def button(fname, label, sub, col):
    W, H = 220, 54
    s = svg_open(W, H, label)
    s += f"""<style>{BASE_CSS}</style>
<rect x="1" y="1" width="{W - 2}" height="{H - 2}" rx="12" fill="{BG0}" stroke="{col}" stroke-opacity=".6"/>
<rect x="1" y="1" width="6" height="{H - 2}" rx="3" fill="{col}"/>
<text x="24" y="25" class="sans" font-size="15" font-weight="700" fill="{INK}">{esc(label)}</text>
<text x="24" y="42" class="mono" font-size="11" fill="{MUTED}">{esc(sub)}</text>
<text x="{W - 20}" y="33" class="mono" font-size="16" fill="{col}" text-anchor="end">&#8594;</text>
</svg>"""
    write(fname, s)


# ---------------------------------------------------------------- footer
def footer():
    W, H = 1200, 150
    s = svg_open(W, H, "Abierto a construir y automatizar. Camilo García, Junior Developer.")
    s += f"""<defs>
<linearGradient id="g" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{GOLD}"/><stop offset="1" stop-color="{TEAL}"/></linearGradient>
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{BG0}"/><stop offset="1" stop-color="{BG1}"/></linearGradient>
<pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="{LINE}" fill-opacity=".06"/></pattern>
</defs>
<style>{BASE_CSS}</style>
<rect width="{W}" height="{H}" rx="18" fill="url(#bg)"/>
<rect width="{W}" height="{H}" rx="18" fill="url(#dots)"/>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="18" fill="none" stroke="{LINE}" stroke-opacity=".08"/>
<rect x="0" y="{H - 3}" width="{W}" height="3" fill="url(#g)"/>
<text x="{W / 2}" y="68" class="sans" font-size="26" font-weight="700" fill="{INK}" text-anchor="middle">Si un proceso se repite, se puede automatizar.</text>
<text x="{W / 2}" y="104" class="mono" font-size="14" fill="{MUTED}" text-anchor="middle">Camilo García · Junior Developer · Bucaramanga, Colombia<tspan class="cur" fill="{TEAL}"> _</tspan></text>
</svg>"""
    write("footer.svg", s)


banner()
section("sec-perfil.svg", "01", "Sobre mí", "perfil")
section("sec-enfoque.svg", "02", "En qué me enfoco", "automatización")
section("sec-proyectos.svg", "03", "Proyectos destacados", "código real")
section("sec-stack.svg", "04", "Tecnologías", "usadas en proyectos")
section("sec-experiencia.svg", "05", "Formación y experiencia", "trayectoria")
section("sec-contacto.svg", "06", "Contacto", "hablemos")
enfoque()
stack()
footer()

card("card-vitalroute.svg", "AGENTE IA · TIEMPO REAL", "VitalRoute",
     "Triaje de emergencias y despacho a la clínica adecuada, con un centro de mando que se actualiza en vivo.",
     "agente con tools · Socket.IO · mapa en vivo", ["TypeScript", "Node.js", "React", "MySQL"], TEAL,
     "En pareja. Mi parte: API gateway, WebSockets, panel y agente.")
card("card-mindconnect.svg", "JAVA · ARQUITECTURA HEXAGONAL", "MindConnect API",
     "Backend para una plataforma de salud mental: historias clínicas, consultas, tratamientos y consentimientos.",
     "52 tablas · más de 600 pruebas · JWT por roles", ["Java 21", "Spring Boot", "PostgreSQL", "Flyway"], GOLD)
card("card-renta.svg", "JAVA · SPRING BOOT", "Renta de Herramientas",
     "Alquiler de maquinaria: reservas por fechas, pagos con IVA, devoluciones con mora y reporte de daños.",
     "113 pruebas · 3 roles · Docker Compose", ["Java 21", "Spring Boot", "MySQL", "JWT"], GOLD)
card("card-aduana.svg", "AGENTE IA · COTIZACIÓN", "Aduana-Copilot",
     "Cotiza la importación de medicamentos y dice la fuente de cada cifra. El modelo nunca hace las cuentas.",
     "agente + motor de cálculo probado con pytest", ["TypeScript", "React", "Python", "FastAPI"], TEAL,
     "En pareja. Mi parte: agente, gateway e interfaz.")
card("card-deliverybot.svg", "AUTOMATIZACIÓN · BOT", "DeliveryBot",
     "Bot de Telegram que toma pedidos de una cafetería, calcula el total y avisa a cocina y al cliente.",
     "39 nodos en n8n · Google Sheets como backend", ["n8n", "JavaScript", "Telegram", "Sheets"], TEAL)
card("card-cv.svg", "PYTHON · IA", "Analizador de CVs",
     "Sube un CV en PDF, escribe el puesto y un modelo de lenguaje evalúa qué tan bien encaja el candidato.",
     "salida validada con Pydantic · más de 60 pruebas", ["Python", "LangChain", "Gemini", "Streamlit"], GOLD)
card("card-tribuna.svg", "PYTHON · IA", "Tribuna Global",
     "Chatbot que guarda opiniones de aficionados sobre futbolistas y las clasifica por sentimiento.",
     "más de 70 pruebas sin gastar API · escritura atómica", ["Python", "LangChain", "Gemini", "Streamlit"], GOLD)
card("card-banco.svg", "JAVASCRIPT · WEB", "Banco ACME",
     "Banca web sin frameworks: transferencias, pagos, metas de ahorro y tasas de cambio en un Web Worker.",
     "módulos ES · clave dinámica · certificado imprimible", ["JavaScript", "HTML", "CSS", "Web Workers"], TEAL,
     "En equipo con Andrés Felipe Guerra.")

button("btn-linkedin.svg", "LinkedIn", "perfil profesional", TEAL)
button("btn-correo.svg", "Correo", "escríbeme", GOLD)
button("btn-portafolio.svg", "Portafolio", "sitio web", TEAL)
button("btn-cv.svg", "Hoja de vida", "PDF · español e inglés", GOLD)
print("ok")
