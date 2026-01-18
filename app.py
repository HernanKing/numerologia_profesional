import streamlit as st
import unicodedata
from datetime import datetime

# 1. Configuración de la tabla de valores (Sistema Pitagórico)
MAPA_NUMEROLOGICO = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
    'J': 1, 'K': 2, 'L': 3, 'M': 4, 'N': 5, 'O': 6, 'P': 7, 'Q': 8, 'R': 9,
    'S': 1, 'T': 2, 'U': 3, 'V': 4, 'W': 5, 'X': 6, 'Y': 7, 'Z': 8
}

def normalizar_texto(texto):
    texto = texto.upper()
    texto = ''.join(c for c in unicodedata.normalize('NFD', texto)
                  if unicodedata.category(c) != 'Mn')
    return texto

def reducir_numero(n):
    if n == 0: return 0
    while n > 9 and n not in [11, 22, 33]:
        n = sum(int(digito) for digito in str(n))
    return n

def calcular_detalles_palabra(palabra):
    vocales_str = "AEIOU"
    v_sum, c_sum = 0, 0
    for letra in palabra:
        val = MAPA_NUMEROLOGICO.get(letra, 0)
        if letra in vocales_str:
            v_sum += val
        elif letra.isalpha():
            c_sum += val
    return v_sum, c_sum

def sumar_digitos_individuales(numero_u_objeto):
    s = str(numero_u_objeto)
    return sum(int(d) for d in s if d.isdigit())

# --- Estética Luxury Perfeccionada (Blanco y Dorado) ---
st.set_page_config(page_title="Mapa Vibracional Maestro", page_icon="✨", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: white; }
    
    /* Título Principal */
    h1 {
        color: #D4AF37 !important;
        font-family: 'Playfair Display', serif;
        font-size: 80px !important;
        text-align: center;
        font-weight: 900;
        margin-bottom: 0px;
    }
    
    /* Títulos de sección y alertas en Dorado */
    .gold-text {
        color: #B8860B !important;
        font-weight: bold !important;
        text-align: center;
    }
    
    .stMetric label { color: #B8860B !important; font-weight: bold !important; font-size: 1.3rem !important; }
    .stMetric div[data-testid="stMetricValue"] { color: #D4AF37 !important; font-size: 3.5rem !important; }
    
    /* Alertas Maestras */
    .master-alert {
        background-color: #FFFDF0;
        border: 2px solid #D4AF37;
        padding: 15px;
        border-radius: 12px;
        color: #B8860B;
        font-weight: bold;
        margin-bottom: 10px;
        text-align: center;
    }
    
    /* Ajuste para el mensaje de éxito final */
    .stSuccess {
        background-color: #FFFDF0 !important;
        color: #B8860B !important;
        border: 1px solid #D4AF37 !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>MAPA VIBRACIONAL</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #D4AF37; margin-top: -20px;'>NUMEROLOGÍA PROFESIONAL</h3>", unsafe_allow_html=True)

# --- Entradas ---
st.sidebar.header("⚜️ DATOS DE ENTRADA")
nombre_input = st.sidebar.text_input("Nombre Completo:")
fecha_nac = st.sidebar.date_input("Fecha de Nacimiento:", min_value=datetime(1900, 1, 1))
anio_manual = st.sidebar.number_input("Año para Año Personal:", value=2026)

if nombre_input:
    nombre_norm = normalizar_texto(nombre_input)
    palabras = nombre_norm.split()
    alertas = []
    
    v_total_nombre, c_total_nombre = 0, 0
    
    for p in palabras:
        v_p, c_p = calcular_detalles_palabra(p)
        total_p = v_p + c_p
        v_total_nombre += v_p
        c_total_nombre += c_p
        
        if reducir_numero(v_p) in [11, 22, 33]: alertas.append(f"Maestro {reducir_numero(v_p)} en Vocales de '{p}'")
        if reducir_numero(c_p) in [11, 22, 33]: alertas.append(f"Maestro {reducir_numero(c_p)} en Consonantes de '{p}'")
        if reducir_numero(total_p) in [11, 22, 33]: alertas.append(f"Maestro {reducir_numero(total_p)} en Total de '{p}'")

    dia, mes, anio = fecha_nac.day, fecha_nac.month, fecha_nac.year
    if reducir_numero(dia) in [11, 22, 33]: alertas.append(f"Día de Nacimiento Maestro: {reducir_numero(dia)}")
    if reducir_numero(mes) in [11, 22, 33]: alertas.append(f"Mes de Nacimiento Maestro: {reducir_numero(mes)}")
    
    suma_fecha_total = sumar_digitos_individuales(dia) + sumar_digitos_individuales(mes) + sumar_digitos_individuales(anio)
    camino_vida = reducir_numero(suma_fecha_total)
    if camino_vida in [11, 22, 33]: alertas.append(f"CAMINO DE VIDA MAESTRO: {camino_vida}")

    alma = reducir_numero(v_total_nombre)
    personalidad = reducir_numero(c_total_nombre)
    mision_vida = reducir_numero(v_total_nombre + c_total_nombre)
    destino = reducir_numero(alma + personalidad)
    
    suma_anio_pers = sumar_digitos_individuales(dia) + sumar_digitos_individuales(mes) + sumar_digitos_individuales(anio_manual)
    anio_personal = reducir_numero(suma_anio_pers)

    # Mostrar Alertas con título Dorado
    if alertas:
        st.markdown("<h3 class='gold-text'>🔱 ALERTAS DE FRECUENCIAS MAESTRAS</h3>", unsafe_allow_html=True)
        for a in list(dict.fromkeys(alertas)):
            st.markdown(f"<div class='master-alert'>{a}</div>", unsafe_allow_html=True)

    # --- RESULTADOS ---
    st.write("---")
    c1, c2, c3 = st.columns(3)
    c1.metric("MISIÓN DE VIDA", mision_vida)
    c2.metric("CAMINO DE VIDA", camino_vida)
    c3.metric("ALMA", alma)

    st.write("<br>", unsafe_allow_html=True)
    
    c4, c5, c6 = st.columns(3)
    c4.metric("PERSONALIDAD", personalidad)
    c5.metric("DESTINO", destino)
    c6.metric("AÑO PERSONAL", anio_personal)

    # Mensaje final en Dorado
    st.markdown(f"<h4 style='text-align: center; color: #B8860B; padding: 20px;'>✨ Mapa finalizado con éxito para: {nombre_input.upper()} ✨</h4>", unsafe_allow_html=True)
else:
    st.info("Esperando datos en la barra lateral...")