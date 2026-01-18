import streamlit as st
import unicodedata
from datetime import datetime

# --- 1. DICCIONARIOS DE DATOS (Corregidos y Completos) ---
MAPA_VALORES = {
    'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,
    'J':1,'K':2,'L':3,'M':4,'N':5,'O':6,'P':7,'Q':8,'R':9,
    'S':1,'T':2,'U':3,'V':4,'W':5,'X':6,'Y':7,'Z':8
}

ELEMENTOS = {
    1: "FUEGO", 3: "FUEGO", 9: "FUEGO",
    4: "TIERRA", 8: "TIERRA", 22: "TIERRA",
    5: "AIRE", 7: "AIRE", 11: "AIRE",
    2: "AGUA", 6: "AGUA", 33: "AGUA"
}

REGALOS_DESC = {
    1: "El Don de la Iniciativa: Tienes una chispa divina para empezar de cero. Tu regalo es la valentía y la originalidad.",
    2: "El Don de la Intuición: Tienes el don de leer a las personas. Eres el puente que une a los demás.",
    3: "El Don de la Palabra: Naciste con el don de la comunicación y el optimismo. Tu voz tiene poder.",
    4: "El Don de la Disciplina: Tienes el don de la manifestación técnica. Capacidad de dar forma a lo invisible.",
    5: "El Don de la Versatilidad: Tu regalo es la adaptabilidad absoluta. Imán para nuevas experiencias.",
    6: "El Don de la Armonía: Tienes el don del toque sanador. Eres una sanadora del hogar.",
    7: "El Don de la Sabiduría: Acceso directo a la biblioteca del conocimiento universal.",
    8: "El Don de la Proyección: Tienes el don de la abundancia y el mando natural.",
    9: "El Don de la Compasión: Tienes el don del amor universal y sabiduría de vidas pasadas.",
    11: "El Don del Canal: Eres un portal de luz. Tu regalo es la visión profética.",
    22: "El Don de la Materialización: Tienes el don de bajar el cielo a la tierra."
}

# --- 2. FUNCIONES LÓGICAS ---
def normalizar(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t.upper()) if unicodedata.category(c) != 'Mn')

def reducir(n, maestro=True):
    if n == 0: return 0
    if maestro:
        while n > 9 and n not in [11, 22, 33]:
            n = sum(int(d) for d in str(n))
    else:
        while n > 9:
            n = sum(int(d) for d in str(n))
    return n

def calc_letras(palabra):
    v_s, c_s = 0, 0
    for l in palabra:
        v = MAPA_VALORES.get(l, 0)
        if l in "AEIOU": v_s += v
        elif l.isalpha(): c_s += v
    return v_s, c_s

# --- 3. ESTILOS LUXURY (ORO Y BLANCO) ---
st.set_page_config(page_title="Identidad 11:11", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF !important; }
    
    .titulo-vibracional {
        color: #D4AF37 !important;
        font-family: 'Playfair Display', serif;
        font-size: 80px !important;
        text-align: center;
        font-weight: 900;
        margin-bottom: -50px !important;
    }
    .subtitulo-profesional {
        color: #D4AF37 !important;
        font-size: 18px !important;
        text-align: center;
        letter-spacing: 7px;
        margin-bottom: 30px;
    }

    [data-testid="stMetricValue"] { color: #D4AF37 !important; font-size: 3.5rem !important; font-weight: 900 !important; }
    [data-testid="stMetricLabel"] p { color: #B8860B !important; font-weight: 800 !important; font-size: 1rem !important; }
    
    .stTabs [data-baseweb="tab"] { color: #B8860B !important; font-weight: bold !important; font-size: 1.2rem; }
    .stTabs [aria-selected="true"] { border-bottom: 4px solid #D4AF37 !important; }

    /* CUADRO DORADO CON LETRA BLANCA (Sustituye al rosado) */
    .luxury-box {
        background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%);
        padding: 25px;
        border-radius: 15px;
        color: #FFFFFF !important;
        font-weight: 600;
        font-size: 1.2rem;
        border: 1px solid #B8860B;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        margin: 20px 0px;
    }
    
    .luxury-text { color: #4F4F4F; line-height: 1.8; font-size: 1.1rem; }
    .gold-sub { color: #B8860B; font-weight: bold; font-size: 1.4rem; border-bottom: 2px solid #D4AF37; margin-top: 25px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<p class='titulo-vibracional'>MAPA VIBRACIONAL</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitulo-profesional'>NUMEROLOGÍA PROFESIONAL</p>", unsafe_allow_html=True)

# --- 4. ENTRADA ---
nombre_raw = st.sidebar.text_input("Nombre Completo:")
fecha_nac = st.sidebar.date_input("Fecha de Nacimiento:", value=datetime(1981, 7, 25))
anio_ref = st.sidebar.number_input("Año de Consulta:", value=2026)

if nombre_raw:
    nombre = normalizar(nombre_raw)
    palabras = nombre.split()
    v_t, c_t = 0, 0
    for p in palabras:
        vs, cs = calc_letras(p)
        v_t += vs; c_t += cs

    # Cálculos Numerológicos
    d, m, a = fecha_nac.day, fecha_nac.month, fecha_nac.year
    alma = reducir(v_t)
    pers = reducir(c_t)
    dest = reducir(alma + pers)
    mision = reducir(v_t + c_t)
    
    s_dir = reducir(sum(int(x) for x in (str(d)+str(m)+str(a))))
    s_grp = reducir(reducir(d) + reducir(m) + reducir(a))
    num_camino = max(s_dir, s_grp)
    txt_camino = f"{num_camino}/{reducir(num_camino,False)}" if num_camino in [11,22,33] else str(num_camino)
    
    regalo = reducir(sum(int(x) for x in str(a)[-2:]))
    anio_p = reducir(sum(int(x) for x in (str(d)+str(m)+str(anio_ref))))

    # Análisis de Tríada
    e_alma = ELEMENTOS.get(alma, "N/A")
    e_pers = ELEMENTOS.get(pers, "N/A")
    e_dest = ELEMENTOS.get(dest, "N/A")
    conteo = [e_alma, e_pers, e_dest]
    
    # --- PESTAÑAS ---
    t1, t2, t3 = st.tabs(["🔱 MAPEO PRINCIPAL", "📖 SIGNIFICADO DE LOS NÚMEROS", "🌀 TRIADA DE REALIZACIÓN"])

    with t1:
        st.write("---")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("🏹 MISIÓN DE VIDA", mision)
        c2.metric("👣 CAMINO DE VIDA", txt_camino)
        c3.metric("💎 ALMA", alma)
        c4.metric("🎁 REGALO DIVINO", regalo)
        
        st.write("<br>", unsafe_allow_html=True)
        c5, c6, c7, c8 = st.columns(4)
        c5.metric("🎭 PERSONALIDAD", pers)
        c6.metric("🏁 DESTINO", dest)
        c7.metric("📅 AÑO PERSONAL", anio_p)
        c8.metric("⚛️ TRIADA DE REALIZACIÓN", f"{len(set(conteo))} Elem.")

    with t2:
        st.markdown(f"""
        <div class='luxury-text'>
            <p class='gold-sub'>🟢 Los Números Base (Del 1 al 9)</p>
            <b>1 - El Líder / El Iniciador:</b> Energía del "Yo Soy". Representa independencia y originalidad. <br>
            <b>2 - El Mediador / El Diplomático:</b> Energía del "Nosotros". Busca la paz y cooperación. <br>
            <b>3 - El Comunicador / El Artista:</b> Energía de la autoexpresión y alegría creativa. <br>
            <b>4 - El Constructor / La Estructura:</b> Energía del orden y bases sólidas. <br>
            <b>5 - El Aventurero / La Libertad:</b> Energía del cambio y la curiosidad. <br>
            <b>6 - El Protector / El Sanador:</b> Energía del amor, familia y responsabilidad. <br>
            <b>7 - El Sabio / El Analista:</b> Energía de la introspección y búsqueda de la verdad. <br>
            <b>8 - El Estratega / El Poder:</b> Energía de la abundancia material y éxito. <br>
            <b>9 - El Humanista / El Guía:</b> Energía del cierre de ciclos y compasión universal. <br>
            
            <p class='gold-sub'>✨ Los Números Maestros</p>
            <b>11 - El Mensajero / El Visionario:</b> Canal de luz. Misión de inspirar y elevar. <br>
            <b>22 - El Arquitecto Maestro:</b> Visión elevada con capacidad práctica de construir. <br>
            <b>33 - El Guía Espiritual:</b> Vibración de Amor Incondicional y sanación. <br>
        </div>
        """, unsafe_allow_html=True)
        
        # EL REGALO DIVINO EN CUADRO DORADO
        st.markdown(f"""
        <div class='luxury-box'>
            🎁 Tu Regalo Divino es el {regalo}: <br>
            {REGALOS_DESC.get(regalo, "Un talento que el Universo te otorgó para que nunca camines a oscuras.")}
        </div>
        """, unsafe_allow_html=True)

    with t3:
        st.markdown("<p class='gold-sub'>🌀 Diagnóstico de tu Tríada de Realización</p>", unsafe_allow_html=True)
        
        # Lógica de diagnóstico (Basada en tus parámetros)
        if e_alma == e_pers == e_dest:
            diag = f"Tienes una coherencia total. Tu alma, tu imagen y tu misión vibran en la misma frecuencia ({e_alma}), lo que te hace una persona extremadamente clara y directa."
        elif "FUEGO" in conteo and "TIERRA" in conteo:
            diag = "Tienes la pasión para empezar (fuego) y la disciplina para terminar (tierra). Eres una emprendedora nata."
        elif "TIERRA" not in conteo:
            diag = "Tienes grandes ideas y emociones, pero tu reto es aterrizarlas. Mi sistema Identidad 11:11 te ayudará a crear la estructura que te falta."
        else:
            diag = "Posees una mezcla equilibrada de elementos. Tu camino es integrar tu visión con tu capacidad de sentir."
            
        st.markdown(f"<div class='luxury-box'>{diag}</div>", unsafe_allow_html=True)
        
        st.markdown("<p class='gold-sub'>🔥 Elementos en tu Mapa</p>", unsafe_allow_html=True)
        st.markdown(f"1. **Alma:** {e_alma} | 2. **Personalidad:** {e_pers} | 3. **Destino:** {e_dest}")

    st.markdown(f"<p style='text-align: center; color: #D4AF37; margin-top: 40px; font-weight: bold;'>✨ Mapa Generado para: {nombre_raw.upper()} ✨</p>", unsafe_allow_html=True)
else:
    st.info("Por favor, ingresa los datos en la barra lateral para ver tu Mapa Vibracional.")
