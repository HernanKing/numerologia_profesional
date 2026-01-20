import streamlit as st
import unicodedata
from datetime import datetime

# --- 1. CONFIGURACIÓN DE DATOS ---
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

ARCHETYPES = {
    1: "La Iniciadora", 2: "La Tejedora", 3: "La Expresora",
    4: "La Arquitecta", 5: "La Exploradora", 6: "La Guardiana",
    7: "La Sabia", 8: "La Gestora", 9: "La Integradora",
}

MASTER_DESTINIES = {
    11: "Visionaria", 22: "Maestra", 33: "Compasiva"
}

REGALOS_DESC = {
    1: "El Don de la Iniciativa Tienes una chispa divina para empezar de cero. Tu regalo es la valentía y la originalidad. Nunca te faltarán ideas nuevas ni la fuerza para ser la primera en algo. Eres una líder nata por derecho divino.",
    2: "El Don de la Intuición Tienes el don de 'leer' a las personas y las situaciones. Tu regalo es la diplomacia y la sensibilidad. Eres el puente que une a los demás y tienes una capacidad natural para traer paz donde hay conflicto.",
    3: "El Don de la Palabra Naciste con el don de la comunicación y el optimismo. Tu presencia alegra los espacios. Tienes la facilidad de expresar ideas complejas de forma sencilla y creativa. Tu voz tiene poder.",
    4: "El Don de la Disciplina Tienes el don de la manifestación técnica. Tu regalo es la capacidad de dar forma a lo invisible. Eres confiable, organizada y capaz de construir estructuras que duran para siempre.",
    5: "El Don de la Versatilidad Tu regalo es la adaptabilidad absoluta. Tienes la bendición de aprender rápido y de sentirte en casa en cualquier lugar del mundo. Eres un imán para las nuevas experiencias y la libertad.",
    6: "El Don de la Armonía Tienes el don del 'toque sanador'. Tu regalo es crear belleza y bienestar a tu alrededor. La gente busca tu consejo porque emanas protección y equilibrio. Eres una sanadora del hogar.",
    7: "El Don de la Sabiduría Tienes acceso directo a la biblioteca del conocimiento universal. Tu regalo es una mente analítica y espiritual. Comprendes los misterios de la vida con una facilidad asombrosa. Eres una guía intelectual.",
    8: "El Don de la Proyección Tienes el don de la abundancia y el mando. Tu regalo es saber cómo generar recursos and cómo dirigir grandes proyectos. El universo te otorga autoridad natural para manejar el mundo material.",
    9: "El Don de la Compasión Tienes el don del amor universal. Tu regalo es una sabiduría que viene de vidas pasadas. Eres capaz de entender y perdonar a todos. Tu presencia eleva la frecuencia de cualquier grupo.",
    11: "El Don del Canal Eres un portal de luz. Tu regalo es la visión profética y la inspiración constante. No necesitas buscar respuestas, las respuestas te llegan a través de señales claras.",
    22: "El Don de la Materialización Tienes el don de 'bajar el cielo a la tierra'. Puedes convertir sueños utópicos en empresas o realidades tangibles para el beneficio de muchos."
}

# --- 2. LÓGICA DE REDUCCIÓN ---
def reducir(n):
    if n in [11, 22, 33]: return n
    while n > 9 and n not in [11, 22, 33]:
        n = sum(int(d) for d in str(n))
    return n

def normalizar(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t.upper()) if unicodedata.category(c) != 'Mn')

def generate_identity(alma, destino):
    alma_role = ARCHETYPES.get(alma, "Esencia")
    if destino in MASTER_DESTINIES:
        destiny_role = MASTER_DESTINIES[destino]
        return f"{alma_role} {destiny_role}"
    else:
        destiny_role = ARCHETYPES.get(destino, "Manifestación").replace("La ", "")
        return f"{alma_role} {destiny_role}"

# --- 3. ESTILOS LUXURY ---
st.set_page_config(page_title="Identidad 11:11", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #FFFFFF !important; }
    .titulo-vibracional { color: #D4AF37 !important; font-family: 'serif'; font-size: 70px !important; text-align: center; font-weight: 900; margin-bottom: 0px !important; }
    .subtitulo-profesional { color: #D4AF37 !important; font-size: 16px !important; text-align: center; letter-spacing: 7px; margin-bottom: 30px !important; }
    .stTabs [data-baseweb="tab"] { color: #D4AF37 !important; font-weight: bold !important; font-size: 1.1rem; }
    .stTabs [aria-selected="true"] { border-bottom: 4px solid #D4AF37 !important; color: #B8860B !important; }
    [data-testid="stMetricValue"] { color: #D4AF37 !important; font-weight: 900 !important; font-size: 3.5rem !important; }
    [data-testid="stMetricLabel"] p { color: #B8860B !important; font-weight: 800 !important; font-size: 0.85rem !important; text-transform: uppercase; }
    .alerta-maestra { border: 2px solid #D4AF37; border-radius: 8px; color: #B8860B; padding: 10px; margin: 5px; font-weight: bold; text-align: center; background-color: #FFFDF5; }
    .luxury-box { background: linear-gradient(135deg, #D4AF37 0%, #B8860B 100%); padding: 25px; border-radius: 12px; color: #FFFFFF !important; text-align: center; margin: 10px 0px; }
    .luxury-text-block { color: #2F2F2F; background-color: #FAFAFA; padding: 30px; border-radius: 10px; border-left: 5px solid #D4AF37; line-height: 1.8; font-size: 1.05rem; }
    .mision-container { border: 2px solid #D4AF37; padding: 30px; border-radius: 15px; background-color: #FFFFFF; }
    .mision-header { color: #D4AF37; font-size: 2rem; font-weight: bold; margin-bottom: 20px; border-bottom: 2px solid #D4AF37; padding-bottom: 10px; }
    .param-box { background-color: #D4AF37; color: white; padding: 15px; border-radius: 8px; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<p class='titulo-vibracional'>MAPA VIBRACIONAL</p>", unsafe_allow_html=True)
st.markdown("<p class='subtitulo-profesional'>NUMEROLOGÍA PROFESIONAL</p>", unsafe_allow_html=True)

# --- 4. PANEL LATERAL ---
st.sidebar.markdown("### ✨ DATOS DE ENTRADA")
nombre_raw = st.sidebar.text_input("Nombre Completo:")
fecha_nac = st.sidebar.date_input("Fecha de Nacimiento:", value=datetime(1981, 7, 25), min_value=datetime(1900, 1, 1), max_value=datetime(2026, 12, 31))
anio_ref = st.sidebar.number_input("Año de Consulta:", value=2026)

if nombre_raw:
    nombre = normalizar(nombre_raw)
    palabras = nombre.split()
    alertas = []
    mision_pre_suma, sum_total_vocales, sum_total_consonantes = 0, 0, 0
    
    for p in palabras:
        v_pal = sum(MAPA_VALORES.get(l, 0) for l in p)
        v_voc = sum(MAPA_VALORES.get(l, 0) for l in p if l in "AEIOU")
        v_con = sum(MAPA_VALORES.get(l, 0) for l in p if l.isalpha() and l not in "AEIOU")
        p_reducida = reducir(v_pal)
        mision_pre_suma += p_reducida
        if p_reducida in [11, 22, 33]: alertas.append(f"✨ Maestro {p_reducida} en Nombre/Apellido: {p}")
        if reducir(v_voc) in [11, 22, 33]: alertas.append(f"🕊️ Alma Maestra {reducir(v_voc)} en: {p}")
        if reducir(v_con) in [11, 22, 33]: alertas.append(f"🎭 Personalidad Maestra {reducir(v_con)} en: {p}")
        sum_total_vocales += v_voc
        sum_total_consonantes += v_con

    d, m, a = fecha_nac.day, fecha_nac.month, fecha_nac.year
    alma, mision = reducir(sum_total_vocales), reducir(mision_pre_suma)
    pers, dest = reducir(sum_total_consonantes), reducir(reducir(sum_total_vocales) + reducir(sum_total_consonantes))
    camino = reducir(reducir(d) + reducir(m) + reducir(a))
    regalo = reducir(sum(int(x) for x in str(a)[-2:]))
    anio_p = reducir(reducir(d) + reducir(m) + reducir(anio_ref))

    t1, t2, t3, t4, t5 = st.tabs(["🔱 MAPEO PRINCIPAL", "📖 SIGNIFICADO DE LOS NÚMEROS", "🌀 TRÍADA DE REALIZACIÓN", "✨ MISIÓN SAGRADA", "💎 REVELACIÓN GENERAL"])

    with t1:
        if alertas:
            st.markdown("<p style='color: #B8860B; font-weight: bold; text-align: center;'>⚠️ FRECUENCIAS MAESTRAS DETECTADAS</p>", unsafe_allow_html=True)
            for msg in alertas: st.markdown(f"<div class='alerta-maestra'>{msg}</div>", unsafe_allow_html=True)
        st.write("---")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("MISIÓN DE VIDA", mision)
        c2.metric("CAMINO DE VIDA", camino)
        c3.metric("ALMA", alma)
        c4.metric("REGALO DIVINO", regalo)
        c5, c6, c7, c8 = st.columns(4)
        c5.metric("PERSONALIDAD", pers)
        c6.metric("DESTINO", dest)
        c7.metric("AÑO PERSONAL", anio_p)
        e_alma, e_pers, e_dest = ELEMENTOS.get(alma), ELEMENTOS.get(pers), ELEMENTOS.get(dest)
        c8.metric("TRÍADA DE REALIZACIÓN", len(set([e_alma, e_pers, e_dest])))

    with t2:
        st.markdown(f"""
        <div class='luxury-text-block'>
        <b>🧮SIGNIFICADO DE LOS NÚMEROS</b><br>
        <b>🟢 Los Números Base (Del 1 al 9) NUMEROLOGÍA</b><br>
        1 - El Líder / El Iniciador: Es la energía del "Yo Soy". Representa independencia, originalidad y el impulso para comenzar cosas nuevas. En desequilibrio: puede ser autoritario o egoísta.<br>
        2 - El Mediador / El Diplomático: Es la energía del "Nosotros". Busca la paz, el equilibrio y la cooperación. Es intuitivo y sensible. En desequilibrio: puede ser dependiente o indeciso.<br>
        3 - El Comunicador / El Artista: Es la energía de la autoexpresión. Representa la alegría, la creatividad, la palabra y la sociabilidad. En desequilibrio: puede ser superficial o disperso.<br>
        4 - El Constructor / La Estructura: Es la energía del orden. Representa el trabajo duro, la lealtad, la organización y las bases sólidas. En desequilibrio: puede ser rígido o testarudo.<br>
        5 - El Aventurero / La Libertad: Es la energía del cambio. Representa la curiosidad, el movimiento, los viajes y la adaptabilidad. En desequilibrio: puede ser impaciente o irresponsable.<br>
        6 - El Protector / El Sanador: Es la energía del amor y la familia. Representa la responsabilidad, la armonía, la belleza y el servicio a los demás. En desequilibrio: puede ser perfeccionista o entrometido.<br>
        7 - El Sabio / El Analista: Es la energía de la introspección. Busca la verdad, el conocimiento profundo, la espiritualidad y la soledad necesaria. En desequilibrio: puede ser frío o cínico.<br>
        8 - El Estratega / El Poder: Es la energía de la abundancia material. Representa el éxito, la autoridad, la justicia y la capacidad de manifestar riqueza. En desequilibrio: puede ser ambicioso en exceso o materialista.<br>
        9 - El Humanista / El Guía: Es la energía del cierre de ciclos. Representa la compasión universal, el idealismo y la entrega desinteresada. En desequilibrio: puede ser dramático o vivir en el pasado.<br>
        <b>✨ Los Números Maestros (No se reducen)</b><br>
        11 - El Mensajero / El Visionario: (Tu número y el de tu marca). Es un canal de luz. Tiene una intuición aguda y su misión es inspirar y elevar la consciencia de los demás. Es el "Puente" entre mundos.<br>
        22 - El Arquitecto Maestro: (Tu día de nacimiento). Es el número más poderoso. Tiene la visión del 11 pero la capacidad práctica del 4. Puede construir proyectos gigantescos que beneficien a la humanidad.<br>
        33 - El Guía Espiritual: Es la vibración del "Amor Incondicional". Su misión es la sanación a gran escala y la enseñanza a través del ejemplo de sacrificio y servicio puro.<br><br>

        <b>🕊️ Guía Espiritual y Angelical de los Números</b><br>
        <b>1 - El Rayo de la Creación</b><br>
        Espiritual: Representa la unidad con la Fuente. Es el "Yo Soy" manifestado. Simboliza que tus pensamientos son semillas de realidad.<br>
        Angelical: Los ángeles te dicen: "Mantente positivo. Tus intenciones se están manifestando instantáneamente. Enfócate en tus deseos, no en tus miedos".<br>
        <b>2 - La Dualidad Sagrada</b><br>
        Espiritual: Representa el equilibrio, la paciencia y el principio femenino de la recepción. Es la fe en que todo llega en el tiempo divino.<br>
        Angelical: "Ten fe. Tus oraciones están siendo escuchadas y trabajadas detrás de escena. No te rindas justo antes de que ocurra el milagro".<br>
        <b>3 - La Santísima Trinidad</b><br>
        Espiritual: Representa la expansión y la conexión con los Maestros Ascendidos. Es la unión de mente, cuerpo y espíritu.<br>
        Angelical: "Los Maestros Ascendidos están cerca de ti, respondiendo a tus peticiones y ayudándote a encontrar tu alegría creativa".<br>
        <b>4 - La Protección de la Tierra</b><br>
        Espiritual: Representa el orden divino y la presencia de los elementos. Es el número de los cimientos espirituales.<br>
        Angelical: "¡No estás solo! Los ángeles te rodean para darte seguridad y apoyo. Pide ayuda para organizar tu vida y tus ideas".<br>
        <b>5 - La Alquimia del Cambio</b><br>
        Espiritual: Representa la evolución del alma a través de la experiencia. Es el número de la libertad y el aprendizaje por el movimiento.<br>
        Angelical: "Un cambio importante y positivo viene hacia ti. Suelta lo viejo con gratitud para permitir que lo nuevo transforme tu vida".<br>
        <b>6 - La Armonía del Corazón</b><br>
        Espiritual: Representa el equilibrio entre lo material y lo espiritual. Es el servicio basado en el amor incondicional.<br>
        Angelical: "Equilibra tus pensamientos entre el cielo y la tierra. Deja tus preocupaciones materiales en nuestras manos y enfócate en el amor y la gratitud".<br>
        <b>7 - La Iluminación Sagrada</b><br>
        Espiritual: Es el número de la perfección divina y el misticismo. Representa el camino del buscador que encuentra la verdad en su interior.<br>
        Angelical: "¡Felicidades! Estás en el camino correcto. Sigue confiando en tu intuición, pues estás alineado con tu propósito divino".<br>
        <b>8 - El Infinito y la Justicia</b><br>
        Espiritual: Representa el flujo infinito de energía (karma y dharma). Lo que das, vuelve a ti multiplicado. Es la ley de causa y efecto.<br>
        Angelical: "La abundancia fluye hacia ti. Confía en que el universo es infinito. Usa tu poder y tus recursos para el bien común".<br>
        <b>9 - La Consciencia Crística</b><br>
        Espiritual: Representa el amor universal y la culminación del viaje del alma. Es el número del "Trabajador de la Luz".<br>
        Angelical: "Es hora de ponerte a trabajar en tu misión de vida sin demora. El mundo necesita tu luz. Cierra ciclos para empezar tu labor sagrada".<br><br>

        <b>✨ Los Números Maestros (Frecuencias Angélicas Superiores)</b><br>
        <b>11 - El Portal de Luz (Tu Marca)</b><br>
        Espiritual: Es el portal de la iluminación. Representa a los "Mensajeros de la Nueva Era". Es la conexión directa con la sabiduría del alma.<br>
        Angelical: "Presta mucha atención a tus ideas repetitivas; son las respuestas a tus oraciones. Estás siendo llamado a guiar a otros con tu ejemplo".<br>
        <b>22 - El Arquitecto del Cielo en la Tierra</b><br>
        Espiritual: Representa la capacidad de manifestar los sueños más elevados en la realidad física. Es la maestría sobre la materia.<br>
        Angelical: "Mantén la visión a largo plazo. Tienes la protección divina para construir algo grande que servirá a muchas personas. Actúa con disciplina".<br>
        <b>33 - El Avatar del Amor</b><br>
        Espiritual: Es la frecuencia de la compasión absoluta. Representa la energía del Maestro que enseña a través del amor puro.<br>
        Angelical: "Tu vibración está elevando la de quienes te rodean. Tu presencia es una blessing. Enfócate en sanar a través de tu bondad".<br><br>

        <b>🎁 Significado del Regalo Divino (Dones de Nacimiento)</b><br>
        Regalo 1: {REGALOS_DESC.get(1)}<br>
        Regalo 2: {REGALOS_DESC.get(2)}<br>
        Regalo 3: {REGALOS_DESC.get(3)}<br>
        Regalo 4: {REGALOS_DESC.get(4)}<br>
        Regalo 5: {REGALOS_DESC.get(5)}<br>
        Regalo 6: {REGALOS_DESC.get(6)}<br>
        Regalo 7: {REGALOS_DESC.get(7)}<br>
        Regalo 8: {REGALOS_DESC.get(8)}<br>
        Regalo 9: {REGALOS_DESC.get(9)}<br>
        <b>✨ Regalos Maestros</b><br>
        Regalo 11: {REGALOS_DESC.get(11)}<br>
        Regalo 22: {REGALOS_DESC.get(22)}<br><br>

        <b>ELEMENTOS</b><br>
        <b>🔥 FUEGO (1, 3, 9)</b><br>
        Fuerza, Acción, Intuición y Pasión. Son personas que inician y lideran.<br><br>
        <b>🌱 TIERRA (4, 8, 22)</b><br>
        Estructura, Orden y Manifestación. Es la capacidad de concretar.<br><br>
        <b>💨 AIRE (5, 7, 11)</b><br>
        Intelecto, Libertad y Análisis. El mundo de las ideas y la visión.<br><br>
        <b>💧 AGUA (2, 6, 33)</b><br>
        Emoción, Empatía y Sensibilidad. Son los sanadores y cuidadores.
        </div>
        """, unsafe_allow_html=True)

    with t3:
        st.markdown("<p style='color: #B8860B; font-weight: bold; font-size: 1.4rem;'>🌀 DIAGNÓSTICO DE TU TRÍADA</p>", unsafe_allow_html=True)
        st.markdown(f"<div style='background-color: #FFFDF5; padding: 15px; border-radius: 10px; border: 1px solid #D4AF37; margin-bottom: 20px; color: #B8860B;'><b>Composición:</b><br>💎 ALMA: {alma} ({e_alma})<br>🎭 PERSONALIDAD: {pers} ({e_pers})<br>🏁 DESTINO: {dest} ({e_dest})</div>", unsafe_allow_html=True)
        conteo = [e_alma, e_pers, e_dest]
        if e_alma == e_pers == e_dest: diag = f"Coherencia total en frecuencia {e_alma}."
        elif "FUEGO" in conteo and "TIERRA" in conteo: diag = "Pasión para empezar y disciplina para terminar."
        elif "TIERRA" not in conteo: diag = "Grandes ideas, pero reto en aterrizarlas."
        else: diag = "Mezcla equilibrada de energías elementales."
        st.markdown(f"<div class='luxury-box'>{diag}</div>", unsafe_allow_html=True)

    with t4:
        eje_titulo, mision_txt, enfoque, frase, advertencia, consejo = "", "", "", "", "", ""
        elem_camino = ELEMENTOS.get(camino)
        grupo_camino = "MAESTRO" if camino in [11, 22, 33] else ("FA" if elem_camino in ["FUEGO", "AIRE"] else "TA")

        if dest == 11:
            eje_titulo, mision_txt = "🔱 Eje 1: El Canal Visionario (DESTINO 11)", "Inspirar y despertar consciencias."
            if grupo_camino == "FA": enfoque, frase, advertencia, consejo = "Comunicación masiva e innovación.", "'Enciendo la chispa del despertar.'", "Mesianismo o dispersión.", "Busca un socio de Tierra."
            elif grupo_camino == "TA": enfoque, frase, advertencia, consejo = "Arquitectura sagrada y sanación.", "'Bajo la luz del espíritu a la materia.'", "Hipersensibilidad.", "Entorno silencioso."
            else: enfoque, frase, advertencia, consejo = "Guía de guías.", "'Soy el puente puro entre dimensiones.'", "Soberbia espiritual.", "Simplifica tu mensaje."
        elif dest in [1, 5, 8]:
            eje_titulo, mision_txt = "🚀 Eje 2: Expansión y Poder (DESTINO 1, 5, 8)", "Liderar y manifestar abundancia."
            if grupo_camino == "FA": enfoque, frase, advertencia, consejo = "Startups y marketing de impacto.", "'Abro caminos donde otros ven muros.'", "Tiranía o burnout.", "Aprende a delegar."
            elif grupo_camino == "TA": enfoque, frase, advertencia, consejo = "Bienes raíces y banca ética.", "'Construyo imperios inquebrantables.'", "Rigidez.", "Invierte en tecnología."
            else: enfoque, frase, advertencia, consejo = "Estrategia global.", "'Dirijo riqueza hacia propósitos elevados.'", "Uso egoísta del poder.", "Causa social vinculada."
        elif dest in [2, 6, 9, 33]:
            eje_titulo, mision_txt = "🕊️ Eje 3: Servicio y Sanación (DESTINO 2, 6, 9, 33)", "Equilibrar y sanar."
            if grupo_camino == "FA": enfoque, frase, advertencia, consejo = "Coaching y marcas saludables.", "'Protejo a la humanidad.'", "Sacrificio excesivo.", "Pon límites claros."
            elif grupo_camino == "TA": enfoque, frase, advertencia, consejo = "Interiorismo y educación de lujo.", "'Mi éxito es la paz que genero.'", "Codependencia.", "Disciplina profesional."
            else: enfoque, frase, advertencia, consejo = "Mentoría para élites.", "'Soy el bálsamo de amor.'", "Cargar dolor ajeno.", "Practica el desapego."
        else:
            eje_titulo, mision_txt = "🏗️ Eje 4: Estructura y Manifestación (DESTINO 3, 4, 7, 22)", "Construir y dejar legado."
            if grupo_camino == "FA": enfoque, frase, advertencia, consejo = "Ingeniería y producción creativa.", "'Transformo ideas en realidades técnicas.'", "Perfeccionismo.", "Aplica ley 80/20."
            elif grupo_camino == "TA": enfoque, frase, advertencia, consejo = "Restauración y logística.", "'Mi orden construye estabilidad.'", "Zona de confort.", "Actualiza herramientas."
            else: enfoque, frase, advertencia, consejo = "Ciberseguridad e investigación.", "'Ordeno conocimiento para revelar la verdad.'", "Frialdad mental.", "Incluye factor humano."

        st.markdown(f"<div class='mision-container'><div class='mision-header'>{eje_titulo}</div><div class='luxury-text-block' style='background:white; border:none;'><span style='color:#D4AF37; font-weight:bold;'>MISIÓN:</span> {mision_txt}<br><br><span style='color:#D4AF37; font-weight:bold;'>ENFOQUE:</span> {enfoque}<br><br><div style='background:#D4AF37; color:white; padding:15px; border-radius:8px; font-style:italic; text-align:center;'>FRASE: {frase}</div><br><span style='color:#8B0000; font-weight:bold;'>⚠️ SOMBRA:</span> {advertencia}<br><br><div style='border:1px dashed #D4AF37; padding:15px; border-radius:8px; background:#FFFDF5;'><span style='color:#D4AF37; font-weight:bold;'>💡 CONSEJO:</span> {consejo}</div></div></div>", unsafe_allow_html=True)

    with t5:
        identidad_final = generate_identity(alma, dest).upper()
        st.markdown(f"""
            <div style="text-align: center; padding: 50px; border: 3px double #D4AF37; border-radius: 20px; background-color: #FFFFFF; margin-top: 20px;">
                <p style="color: #B8860B; letter-spacing: 7px; font-size: 14px; font-weight: bold; margin-bottom: 20px;">IDENTIDAD 11:11 DETECTADA</p>
                <h1 style="color: #D4AF37; font-family: 'serif'; font-size: 50px; font-weight: 900; margin-bottom: 10px; line-height: 1.2;">{identidad_final}</h1>
                <div style="width: 150px; height: 2px; background-color: #D4AF37; margin: 0 auto 30px auto;"></div>
                <p style="color: #2F2F2F; font-size: 20px; font-style: italic; max-width: 700px; margin: 0 auto; line-height: 1.8;">"Cuando alineas tu estructura interna con tu misión, <br> la materia comienza a ordenarse."</p>
                <div style="margin-top: 50px; display: flex; justify-content: center; gap: 60px;">
                    <div style="text-align: center;"><p style="color: #B8860B; font-size: 13px; font-weight: bold; text-transform: uppercase;">Esencia (Alma)</p><p style="color: #2F2F2F; font-size: 18px;">{ARCHETYPES.get(alma)}</p></div>
                    <div style="text-align: center;"><p style="color: #B8860B; font-size: 13px; font-weight: bold; text-transform: uppercase;">Manifestación (Destino)</p><p style="color: #2F2F2F; font-size: 18px;">{MASTER_DESTINIES.get(dest) if dest in MASTER_DESTINIES else ARCHETYPES.get(dest).replace('La ', '')}</p></div>
                </div>
                <div style="margin-top: 60px; border-top: 1px solid #EEE; padding-top: 20px;"><p style="color: #B8860B; font-weight: bold; font-size: 15px; letter-spacing: 3px;">DESIGNACIÓN OFICIAL</p><p style="color: #555; font-size: 14px;">Frecuencia maestra unificada para la manifestación consciente.</p></div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown(f"<p style='text-align: center; color: #D4AF37; margin-top: 50px;'>✨ Identidad 11:11 - {nombre_raw.upper()} ✨</p>", unsafe_allow_html=True)
