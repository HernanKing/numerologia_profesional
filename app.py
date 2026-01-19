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
    
    /* Estilos específicos para la Misión Sagrada */
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
    
    mision_pre_suma = 0
    sum_total_vocales = 0
    sum_total_consonantes = 0
    
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
    alma = reducir(sum_total_vocales)
    mision = reducir(mision_pre_suma)
    pers = reducir(sum_total_consonantes)
    dest = reducir(alma + pers)
    camino = reducir(reducir(d) + reducir(m) + reducir(a))
    regalo = reducir(sum(int(x) for x in str(a)[-2:]))
    anio_p = reducir(reducir(d) + reducir(m) + reducir(anio_ref))

    t1, t2, t3, t4 = st.tabs(["🔱 MAPEO PRINCIPAL", "📖 SIGNIFICADO DE LOS NÚMEROS", "🌀 TRÍADA DE REALIZACIÓN", "✨ MISIÓN SAGRADA IDENTIDAD 11:11"])

    with t1:
        if alertas:
            st.markdown("<p style='color: #B8860B; font-weight: bold; text-align: center;'>⚠️ FRECUENCIAS MAESTRAS DETECTADAS</p>", unsafe_allow_html=True)
            for msg in alertas:
                st.markdown(f"<div class='alerta-maestra'>{msg}</div>", unsafe_allow_html=True)
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
        num_elementos = len(set([e_alma, e_pers, e_dest]))
        c8.metric("TRÍADA DE REALIZACIÓN", num_elementos)

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
        <b>✨ Regalos Maestros (Si los dos últimos dígitos son 11 o 22)</b><br>
        Nota: Es raro, pero ocurre (ej. alguien nacido en 1911 o 2011).<br>
        Regalo 11: {REGALOS_DESC.get(11)}<br>
        Regalo 22: {REGALOS_DESC.get(22)}<br><br>

        <b>ELEMENTOS</b><br>
        <b>🔥 FUEGO (1, 3, 9)</b><br>
        Fuerza, Acción, Intuición y Pasión.<br>
        Significado: Son personas que inician, que brillan y que tienen mucha energía vital.<br>
        En la tríada: Si alguien tiene muchos números de fuego, es una persona que difícilmente se queda quieta; necesita crear y liderar.<br><br>
        <b>🌱 TIERRA (4, 8, 22)</b><br>
        Estructura, Orden, Manifestación y Realidad.<br>
        Significado: Es la capacidad de concretar. Son personas realistas, ambiciosas en el buen sentido y muy trabajadoras.<br>
        En la tríada: Si predomina la tierra, la persona es el "ancla" de su familia o empresa. El 22 es el grado más alto de tierra (el constructor maestro).<br><br>
        <b>💨 AIRE (5, 7, 11)</b><br>
        Intelecto, Libertad, Comunicación y Análisis.<br>
        Significado: Es el mundo de las ideas. El 5 busca libertad, el 7 busca sabiduría y el 11 busca visión.<br>
        En la tríada: Predomina la mente sobre la emoción. Son grandes estrategas y pensadores.<br><br>
        <b>💧 AGUA (2, 6, 33)</b><br>
        Emoción, Empatía, Servicio y Sensibilidad.<br>
        Significado: Es el mundo del sentimiento. Son los sanadores, los que cuidan, los que sienten profundamente.<br>
        En la tríada: Si predomina el agua, la persona toma decisiones basadas en cómo se siente o cómo hará sentir a los demás. El 33 es el grado máximo de agua (amor universal).
        </div>
        """, unsafe_allow_html=True)

    with t3:
        st.markdown("<p style='color: #B8860B; font-weight: bold; font-size: 1.4rem;'>🌀 DIAGNÓSTICO DE TU TRÍADA</p>", unsafe_allow_html=True)
        st.markdown(f"""
        <div style='background-color: #FFFDF5; padding: 15px; border-radius: 10px; border: 1px solid #D4AF37; margin-bottom: 20px; color: #B8860B;'>
        <b>Composición de tu Tríada:</b><br>
        💎 ALMA: {alma} ({e_alma})<br>
        🎭 PERSONALIDAD: {pers} ({e_pers})<br>
        🏁 DESTINO: {dest} ({e_dest})
        </div>
        """, unsafe_allow_html=True)

        conteo = [e_alma, e_pers, e_dest]
        if e_alma == e_pers == e_dest:
            diag = f"Tienes una coherencia total. Tu alma, tu imagen y tu misión vibran en la misma frecuencia ({e_alma}), lo que te hace una persona extremadamente clara y directa."
        elif "FUEGO" in conteo and "TIERRA" in conteo:
            diag = "Tienes la pasión para empezar (fuego) y la disciplina para terminar (tierra). Eres una emprendedora nata."
        elif "TIERRA" not in conteo:
            diag = "Tienes grandes ideas y emociones, pero tu reto es aterrizarlas. Mi sistema Identidad 11:11 te ayudará a crear la estructura que te falta."
        else:
            diag = "Posees una mezcla equilibrada de energías elementales para tu desarrollo."
        st.markdown(f"<div class='luxury-box'>{diag}</div>", unsafe_allow_html=True)

    with t4:
        # 1. LÓGICA DE CLASIFICACIÓN (DETERMINACIÓN DE EJE Y ENFOQUE)
        eje_titulo, mision_txt, enfoque, frase, advertencia, consejo = "", "", "", "", "", ""
        elem_camino = ELEMENTOS.get(camino)
        
        # Clasificar Camino de Vida por grupos de la petición
        if camino in [11, 22, 33]: grupo_camino = "MAESTRO"
        elif elem_camino in ["FUEGO", "AIRE"]: grupo_camino = "FA"
        else: grupo_camino = "TA"

        if dest == 11:
            eje_titulo = "🔱 Eje 1: El Canal Visionario (DESTINO 11)"
            mision_txt = "Inspirar, canalizar ideas elevadas y despertar consciencias."
            if grupo_camino == "FA":
                enfoque = "Comunicación masiva, conferencias disruptivas, liderazgo de opinión digital o innovación tecnológica con propósito."
                frase = "'Uso mi magnetismo y mi mente aguda para encender la chispa del despertar en las masas.'"
                advertencia = "Cuidado con el mesianismo o la dispersión mental. Puedes querer salvar al mundo y olvidar pagar tus facturas."
                consejo = "Busca un socio de 'Tierra' que aterrice tus visiones. Tu valor es la idea, no la logística."
            elif grupo_camino == "TA":
                enfoque = "Arquitectura sagrada, centros de sanación física, diseño de marcas de bienestar de lujo o psicología transpersonal aplicada."
                frase = "'Bajo la luz del espíritu a la materia, creando refugios que sanan y armonizan el mundo físico.'"
                advertencia = "La hipersensibilidad. El ruido del mundo físico puede agotarte y hacer que te encierres."
                consejo = "Crea un entorno de trabajo silencioso y estético. Tu productividad depende de tu paz emocional."
            else: # MAESTRO
                enfoque = "Guía de guías, autor de textos sagrados modernos, consultoría de alta intuición para líderes o escuelas de misterio."
                frase = "'Soy el puente puro entre dimensiones; mi palabra es el mapa que guía a las almas hacia su verdad.'"
                advertencia = "La soberbia espiritual o el aislamiento. Sentir que 'nadie te entiende'."
                consejo = "Simplifica tu mensaje. Para guiar a otros, debes hablar el lenguaje de los hombres, no solo el de los ángeles."

        elif dest in [1, 5, 8]:
            eje_titulo = "🚀 Eje 2: Expansión y Poder (DESTINO 1, 5, 8)"
            mision_txt = "Liderar, innovar y manifestar abundancia material."
            if grupo_camino == "FA":
                enfoque = "Startups tecnológicas, agencias de marketing de alto impacto, inversiones de riesgo o marcas personales de alto perfil."
                frase = "'Nací para abrir caminos donde otros ven muros, capitalizando la innovación con valentía y rapidez.'"
                advertencia = "La tiranía o el agotamiento (burnout). Querer resultados para ayer."
                consejo = "Aprende a delegar. Tu negocio crecerá cuando dejes de ser el cuello de botella de todas las decisiones."
            elif grupo_camino == "TA":
                enfoque = "Franquicias de lujo, bienes raíces premium, gerencia de empresas con propósito social o banca ética."
                frase = "'Construyo imperios con bases inquebrantables, uniendo la ambición con la lealtad y el orden.'"
                advertencia = "La rigidez o el miedo a perder lo construido. El exceso de control asfixia la innovación."
                consejo = "Invierte en tecnología y automatización. Tu estructura es fuerte, ahora dale velocidad."
            else: # MAESTRO
                enfoque = "Estrategia corporativa global, fundaciones de gran escala, educación financiera espiritual o diplomacia económica."
                frase = "'Dirijo el flujo de la riqueza mundial hacia propósitos elevados, manifestando abundancia con visión universal.'"
                advertencia = "El uso del poder para beneficio puramente egoísta, lo que genera una caída rápida."
                consejo = "Mantén una causa social vinculada a tus ingresos. Tu riqueza está protegida cuando compartes el éxito."

        elif dest in [2, 6, 9, 33]:
            eje_titulo = "🕊️ Eje 3: Servicio y Sanación (DESTINO 2, 6, 9, 33)"
            mision_txt = "Equilibrar, proteger, educar y sanar."
            if grupo_camino == "FA":
                enfoque = "Coaching motivacional masivo, marcas de alimentación saludable funcional, activismo social mediático o moda ética."
                frase = "'Uso mi fuerza y mi intelecto para proteger a la humanidad y abrir espacios de justicia y bienestar.'"
                advertencia = "El sacrificio excesivo. Dar tanto a los demás que te quedas vacío o resentido."
                consejo = "Pon límites claros. El servicio es tu misión, pero el negocio debe ser rentable para seguir sirviendo."
            elif grupo_camino == "TA":
                enfoque = "Interiorismo gourmet, repostería de autor, educación familiar, centros de estética orgánica o cuidado infantil de lujo."
                frase = "'Mi éxito es la paz que genero en mi entorno; mi don de cuidar es mi fuente infinita de riqueza.'"
                advertencia = "La codependencia o el miedo al conflicto. Evitar decisiones difíciles por no herir sentimientos."
                consejo = "No personalices las críticas. Tu emprendimiento es una extensión de tu amor, pero requiere disciplina profesional."
            else: # MAESTRO
                enfoque = "Mentoría espiritual para élites, centros de retiro exclusivos, medicina integrativa o arte sanador universal."
                frase = "'Soy el bálsamo de amor y sabiduría para las almas; enseño a través de la presencia consciente y la compasión.'"
                advertencia = "Cargar con el dolor del mundo. La angustia existencial por los problemas ajenos."
                consejo = "Practica el desapego. Guía a las personas hacia su propia fuerza en lugar de intentar salvarlas tú mismo."

        else: # DESTINO 3, 4, 7, 22
            eje_titulo = "🏗️ Eje 4: Estructura y Manifestación (DESTINO 3, 4, 7, 22)"
            mision_txt = "Construir, analizar, comunicar técnicamente y dejar legado."
            if grupo_camino == "FA":
                enfoque = "Publicidad creativa técnica, joyería industrial de vanguardia, ingeniería en telecomunicaciones o producción audiovisual."
                frase = "'Transformo la chispa de una idea audaz en una realidad técnica que el mundo admira por su precisión.'"
                advertencia = "El perfeccionismo paralizante. No lanzar un proyecto porque 'aún no es perfecto'."
                consejo = "Aplica la ley del 80/20. Lo que para ti es un 80%, para el mundo ya es excelente. ¡Lánzalo!."
            elif grupo_camino == "TA":
                enfoque = "Ebanistería de lujo, restauración de arte, contabilidad estratégica, logística global o marroquinería artesanal."
                frase = "'La perfección de mi ejecución es mi firma divina; mi orden construye la estabilidad de mi legado.'"
                advertencia = "El estancamiento en la zona de confort. Hacer las cosas 'como siempre se han hecho'."
                consejo = "Actualiza tus herramientas de trabajo. Tu maestría es innegable, pero necesitas herramientas modernas para escalar."
            else: # MAESTRO
                enfoque = "Ciberseguridad, desarrollo de software avanzado, investigación científica privada o auditoría de sistemas místico-técnicos."
                frase = "'Ordeno el conocimiento profundo para revelar la verdad, construyendo las estructuras intelectuales del futuro.'"
                advertencia = "El escepticismo o la frialdad mental. Perder el contacto con la magia de la vida por exceso de análisis."
                consejo = "Incluye siempre el factor humano en tus sistemas. La tecnología más fría necesita un corazón que la dirija."

        # 2. RENDERIZADO CON COLORES LUXURY CORREGIDOS
        st.markdown(f"""
        <div class='mision-container'>
            <div class='mision-header'>{eje_titulo}</div>
            <div class='luxury-text-block' style='background-color: white; border: none;'>
                <span style='color: #D4AF37; font-weight: bold;'>MISIÓN:</span> {mision_txt}<br><br>
                <span style='color: #D4AF37; font-weight: bold;'>ENFOQUE:</span> {enfoque}<br><br>
                <div style='background-color: #D4AF37; color: white; padding: 15px; border-radius: 8px; font-style: italic; text-align: center; margin: 15px 0;'>
                    FRASE DE PODER: {frase}
                </div>
                <span style='color: #8B0000; font-weight: bold;'>⚠️ ADVERTENCIA DE SOMBRA:</span> {advertencia}<br><br>
                <div style='border: 1px dashed #D4AF37; padding: 15px; border-radius: 8px; background-color: #FFFDF5;'>
                    <span style='color: #D4AF37; font-weight: bold;'>💡 CONSEJO DE EMPRENDIMIENTO:</span> {consejo}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown(f"<div class='param-box'>DESTINO: {dest} (Determina tu Eje)</div>", unsafe_allow_html=True)
        with col_b:
            st.markdown(f"<div class='param-box'>CAMINO DE VIDA: {camino} ({elem_camino})</div>", unsafe_allow_html=True)

    st.markdown(f"<p style='text-align: center; color: #D4AF37; margin-top: 50px;'>✨ Identidad 11:11 - {nombre_raw.upper()} ✨</p>", unsafe_allow_html=True)
