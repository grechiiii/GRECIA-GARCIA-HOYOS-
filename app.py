import streamlit as st

# --- COLORES Y ESTILOS ---
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
    .evento-timeline {{
        border-left: 4px solid {celeste_suave};
        padding-left: 1rem;
        margin-bottom: 1rem;
    }}
    </style>
""", unsafe_allow_html=True)

# --- INFO PERSONAL ---
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

# --- GALERÍA DE FOTOS INTERACTIVA ---
imagenes = [
    ("https://i.imgur.com/YQx2CP1.jpeg", "Evento Huellitas 1"),
    ("https://i.imgur.com/CmdHRw2.jpeg", "Evento Huellitas 2"),
    ("https://i.imgur.com/jakXIXZ.jpeg", "Video en marcha PUCP")
]

st.markdown('<div class="seccion galeria">', unsafe_allow_html=True)
st.markdown('📸 <h2>Galería</h2>', unsafe_allow_html=True)

if 'foto_idx' not in st.session_state:
    st.session_state.foto_idx = 0

col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    if st.button("⬅️", key="prev_img"):
        st.session_state.foto_idx = (st.session_state.foto_idx - 1) % len(imagenes)
with col2:
    st.image(imagenes[st.session_state.foto_idx][0], caption=imagenes[st.session_state.foto_idx][1], use_container_width=True)
with col3:
    if st.button("➡️", key="next_img"):
        st.session_state.foto_idx = (st.session_state.foto_idx + 1) % len(imagenes)
st.markdown('</div>', unsafe_allow_html=True)

# --- CARRUSEL DE VIDEOS ---
videos = [
    ("https://www.tiktok.com/@huellitaspucp/video/7349278356820647173", "Video para Huellitas - TikTok"),
    ("https://www.instagram.com/reel/DJPZk9xpZaG/", "Video para redes - Instagram Reel")
]

st.markdown('<div class="seccion galeria">', unsafe_allow_html=True)
st.markdown('🎥 <h2>Carrusel de Videos</h2>', unsafe_allow_html=True)

if 'video_idx' not in st.session_state:
    st.session_state.video_idx = 0

vcol1, vcol2, vcol3 = st.columns([1, 6, 1])
with vcol1:
    if st.button("⬅️", key="prev_vid"):
        st.session_state.video_idx = (st.session_state.video_idx - 1) % len(videos)
with vcol2:
    st.markdown(f"[{videos[st.session_state.video_idx][1]}]({videos[st.session_state.video_idx][0]})", unsafe_allow_html=True)
    st.video(videos[st.session_state.video_idx][0])
with vcol3:
    if st.button("➡️", key="next_vid"):
        st.session_state.video_idx = (st.session_state.video_idx + 1) % len(videos)
st.markdown('</div>', unsafe_allow_html=True)

# --- MIS TRABAJOS CON ENLACES CLICABLES ---
st.markdown('<div class="seccion galeria">', unsafe_allow_html=True)
st.markdown('🎨 <h2>Mis trabajos</h2>', unsafe_allow_html=True)

trabajos = [
    {
        "imagen": "https://imgur.com/kXKetrq.png",
        "titulo": "Presentación Canva",
        "enlace": "https://www.canva.com/design/DAGDV5B6KKo/u8FHE7mouTrmOLrzhY8AUQ/view"
    },
    {
        "imagen": "https://imgur.com/m2b3Z0B.png",
        "titulo": "Video TikTok para Huellitas",
        "enlace": "https://vm.tiktok.com/ZMS9CDVTq/"
    },
    {
        "imagen": "https://imgur.com/EKxwuDo.png",
        "titulo": "Video Instagram para Huellitas",
        "enlace": "https://www.instagram.com/reel/DJPZk9xpZaG/"
    }
]

col1, col2, col3 = st.columns(3)
cols = [col1, col2, col3]
for i, trabajo in enumerate(trabajos):
    with cols[i]:
        st.markdown(f'''
            <a href="{trabajo["enlace"]}" target="_blank">
                <img src="{trabajo["imagen"]}" width="220px" style="border-radius:12px; box-shadow:0 5px 15px rgba(0,0,0,0.3);">
                <p style="text-align:center; color:{texto_claro};">{trabajo["titulo"]}</p>
            </a>
        ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- CV DESCARGABLE ---
st.markdown('<div class="seccion">', unsafe_allow_html=True)
st.markdown('📄 <h2>Mi CV</h2>', unsafe_allow_html=True)
st.markdown('[⬇️ Descargar CV (PDF)](https://drive.google.com/file/d/1UswU-ztMEpjFg6l4wJrIsG3NxWDTuQx3/view)')
st.markdown('</div>', unsafe_allow_html=True)

# --- LOGROS ---
st.markdown('<div class="seccion">', unsafe_allow_html=True)
st.markdown('🏆 <h2>Logros</h2>', unsafe_allow_html=True)
st.markdown("""
Ganadora del Concurso de Investigación Académica 2024-1  
[🔗 Monografía publicada](https://estudios-generales-letras.pucp.edu.pe/investigacion-academica-2024-1-monografias-ganadoras/)
""")
st.markdown("""
<div class="imagenes-logros">
    <img src="https://i.imgur.com/YQx2CP1.jpeg">
    <img src="https://i.imgur.com/OvFF2iU.jpeg">
</div>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- LÍNEA DE TIEMPO ---
st.markdown('<div class="seccion">', unsafe_allow_html=True)
st.markdown('🕒 <h2>Mi trayectoria</h2>', unsafe_allow_html=True)

timeline_events = [
    {"year": "2022", "title": "Egresé del colegio", "description": "Colegio Cristo Rey."},
    {"year": "2023", "title": "Inicié mis estudios en PUCP", "description": "Publicidad en PUCP, primer puesto de la promoción."},
    {"year": "Marzo 2024", "title": "Diseñadora en Huellitas", "description": "Diseñadora audiovisual en campañas."},
    {"year": "Marzo 2025", "title": "Coordinadora de Huellitas", "description": "Encargada de redes y estrategia digital."},
    {"year": "Mayo 2025", "title": "Ganadora de Concurso", "description": "Premio de Investigación Académica en EEGGLL."}
]

for event in timeline_events:
    st.markdown(f'''
        <div class="evento-timeline">
            <h4>{event["year"]} - {event["title"]}</h4>
            <p>{event["description"]}</p>
        </div>
    ''', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown('<footer>✨ Portafolio creado por Grecia García Hoyos ✨</footer>', unsafe_allow_html=True)
