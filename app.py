import streamlit as st

# --- CONFIGURACIÓN Y COLORES ---
fondo_oscuro = "#0A192F"
texto_claro = "#FFFFFF"
celeste_suave = "#A8DADC"
azul_hover = "#0ab2b8"

st.set_page_config(page_title="Portafolio de Grecia", layout="wide")

# --- CSS PERSONALIZADO ---
st.markdown(f"""
    <style>
    body, .stApp {{
        background-color: {fondo_oscuro};
        color: {texto_claro};
    }}
    .titulo-principal {{
        font-size: 2.8rem;
        font-weight: 900;
        background: linear-gradient(90deg, {celeste_suave}, {azul_hover});
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 1rem;
    }}
    .foto-perfil {{
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.4);
        max-width: 140px;
        margin: 0 auto;
    }}
    h2 {{
        color: {celeste_suave} !important;
        border-bottom: 3px solid {azul_hover};
        padding-bottom: 0.3rem;
    }}
    .seccion {{
        background-color: #112240;
        border-radius: 12px;
        padding: 1.5rem 2rem;
        margin-bottom: 2rem;
    }}
    p, li, h3, h4, a {{
        color: {texto_claro};
        font-size: 1.1rem;
        line-height: 1.5;
    }}
    footer {{
        text-align: center;
        color: {celeste_suave};
        margin-top: 3rem;
        font-weight: 600;
    }}
    .galeria img, .imagenes-logros img {{
        border-radius: 10px;
        max-width: 100%;
        box-shadow: 0 5px 15px rgba(100, 255, 218, 0.2);
        transition: transform 0.3s ease;
    }}
    .galeria img:hover, .imagenes-logros img:hover {{
        transform: scale(1.05);
    }}
    .evento-timeline {{
        border-left: 4px solid {celeste_suave};
        padding-left: 1rem;
        margin-bottom: 1rem;
    }}
    </style>
""", unsafe_allow_html=True)

# --- INFORMACIÓN ---
info = {
    "Full_Name": "Grecia García Hoyos",
    "Intro": "Estudiante de Publicidad y apasionada por la comunicación creativa con impacto social",
    "About": """Hola, soy Grecia García Hoyos, estudiante de Publicidad en la PUCP. Me destaco por ser una persona productiva, puntual y con habilidades de liderazgo y organización. 
Siempre busco aprender, colaborar y crear impacto desde la comunicación.""",
    "Medium": "https://www.linkedin.com/in/grecia-garcia-hoyos-44997933a/",
    "City": "Lima, Perú",
    "Photo": "https://i.imgur.com/Noy3lNI.jpg",
    "Email": "a20234861@pucp.edu.pe"
}

# --- CABECERA ---
st.markdown('<div class="seccion">', unsafe_allow_html=True)
col_foto, col_texto = st.columns([1, 3])
with col_foto:
    st.markdown(f'<img src="{info["Photo"]}" class="foto-perfil">', unsafe_allow_html=True)
with col_texto:
    st.markdown(f'<h1 class="titulo-principal">Portafolio de {info["Full_Name"]}</h1>', unsafe_allow_html=True)
    st.markdown(f'<h3>{info["Intro"]}</h3>', unsafe_allow_html=True)
    st.markdown(f'<p>{info["About"]}</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- CONTACTO ---
st.markdown('<div class="seccion">', unsafe_allow_html=True)
st.markdown('📬 <h2>Contacto</h2>', unsafe_allow_html=True)
st.markdown(f'📧 {info["Email"]}  \n📍 {info["City"]}  \n[🔗 LinkedIn]({info["Medium"]})')
st.markdown('</div>', unsafe_allow_html=True)

# --- MIS TRABAJOS ---
st.markdown('<div class="seccion galeria">', unsafe_allow_html=True)
st.markdown('🎨 <h2>Mis trabajos</h2>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://imgur.com/kXKetrq.png", caption="Presentación Canva", use_column_width=True)
    st.markdown('[🔗 Ver presentación](https://www.canva.com/design/DAGDV5B6KKo/u8FHE7mouTrmOLrzhY8AUQ/view)')
with col2:
    st.image("https://imgur.com/m2b3Z0B.png", caption="Video TikTok", use_column_width=True)
    st.markdown('[▶️ Ver video](https://vm.tiktok.com/ZMS9CDVTq/)')
with col3:
    st.image("https://imgur.com/EKxwuDo.png", caption="Video hablando", use_column_width=True)
    st.markdown('[🎥 Ver en Instagram](https://www.instagram.com/reel/DJPZk9xpZaG/)')

st.markdown('</div>', unsafe_allow_html=True)

# --- CV ---
st.markdown('<div class="seccion">', unsafe_allow_html=True)
st.markdown('📄 <h2>Mi CV</h2>', unsafe_allow_html=True)
st.markdown('[⬇️ Descargar CV (PDF)](https://drive.google.com/file/d/1UswU-ztMEpjFg6l4wJrIsG3NxWDTuQx3/view)')
st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown('<footer>✨ Portafolio creado por Grecia García Hoyos✨</footer>'),
