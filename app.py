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
    .galeria img {{
        border-radius: 10px;
        max-width: 100%;
        box-shadow: 0 5px 15px rgba(100, 255, 218, 0.2);
        transition: transform 0.3s ease;
    }}
    .galeria img:hover {{
        transform: scale(1.05);
    }}
    .imagenes-logros img {{
        border-radius: 10px;
        max-width: 100%;
        margin: 10px;
        transition: transform 0.3s ease;
        box-shadow: 0 5px 15px rgba(100, 255, 218, 0.2);
    }}
    .imagenes-logros img:hover {{
        transform: scale(1.05);
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

endorsements = [
    "https://i.imgur.com/YQx2CP1.jpeg",
    "https://i.imgur.com/CmdHRw2.jpeg",
    "https://i.imgur.com/jakXIXZ.jpeg"
]

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

# --- GALERÍA (con flechas) ---
st.markdown('<div class="seccion galeria">', unsafe_allow_html=True)
st.markdown('📸 <h2>Galería</h2>', unsafe_allow_html=True)

if 'galeria_idx' not in st.session_state:
    st.session_state.galeria_idx = 0

col_a, col_img, col_b = st.columns([1, 6, 1])
with col_a:
    if st.button("⬅️", key="prev_img"):
        st.session_state.galeria_idx = (st.session_state.galeria_idx - 1) % len(endorsements)
with col_img:
    st.image(endorsements[st.session_state.galeria_idx], use_container_width=True)
with col_b:
    if st.button("➡️", key="next_img"):
        st.session_state.galeria_idx = (st.session_state.galeria_idx + 1) % len(endorsements)
st.markdown('</div>', unsafe_allow_html=True)

# --- SOBRE GRECIA ---
st.markdown('<div class="seccion">', unsafe_allow_html=True)
st.markdown('🌟 <h2>Sobre Grecia</h2>', unsafe_allow_html=True)
st.markdown('Grecia García Hoyos es estudiante de Publicidad en la PUCP, apasionada por la comunicación creativa con impacto social. Se destaca por ser productiva, puntual y con habilidades de liderazgo y organización.')
st.markdown('</div>', unsafe_allow_html=True)

# --- EXPERIENCIA Y METAS ---
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="seccion">', unsafe_allow_html=True)
    st.markdown('💼 <h2>Experiencia</h2>', unsafe_allow_html=True)
    st.markdown("""
    - Voluntariado ambiental en el colegio  
    - Coordinadora de redes sociales en Huellitas PUCP  
    - Fortaleció creatividad, comunicación digital y trabajo en equipo
    """)
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="seccion">', unsafe_allow_html=True)
    st.markdown('🎯 <h2>Metas</h2>', unsafe_allow_html=True)
    st.markdown("Desarrollarse profesionalmente en comunicación y publicidad, creando proyectos con impacto social.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- HABILIDADES Y CERTIFICACIONES ---
col3, col4 = st.columns(2)
with col3:
    st.markdown('<div class="seccion">', unsafe_allow_html=True)
    st.markdown('🛠️ <h2>Habilidades</h2>', unsafe_allow_html=True)
    st.markdown("""
    - Edición de video (CapCut)  
    - Diseño gráfico (Canva)  
    - Comunicación digital  
    - Liderazgo y trabajo en equipo  
    - Creatividad  
    - Inglés C1 (PUCP)
    """)
    st.markdown('</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="seccion">', unsafe_allow_html=True)
    st.markdown('📜 <h2>Certificaciones</h2>', unsafe_allow_html=True)
    st.markdown("Inglés nivel C1 certificado por Idiomas PUCP.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- HOBBIES ---
st.markdown('<div class="seccion">', unsafe_allow_html=True)
st.markdown('🎾 <h2>Hobbies</h2>', unsafe_allow_html=True)
st.markdown("""
- Grabar y editar videos  
- Practicar tenis de campo  
- Escuchar música y aprender cosas nuevas
""")
st.markdown('</div>', unsafe_allow_html=True)

# --- MIS TRABAJOS ---
st.markdown('<div class="seccion galeria">', unsafe_allow_html=True)
st.markdown('🎨 <h2>Mis trabajos</h2>', unsafe_allow_html=True)

with st.container():
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.image("https://imgur.com/kXKetrq.png", caption="Presentación Canva", width=220)
        st.markdown('[🔗 Ver presentación](https://www.canva.com/design/DAGDV5B6KKo/u8FHE7mouTrmOLrzhY8AUQ/view)')
    with col2:
        st.image("https://imgur.com/m2b3Z0B.png", caption="Video TikTok para huellitas", width=220)
        st.markdown('[▶️ Ver video](https://vm.tiktok.com/ZMS9CDVTq/)')
    with col3:
        st.image("https://imgur.com/EKxwuDo.png", caption="Video Instagram para huellitas", width=220)
        st.markdown('[🎥 Ver en Instagram](https://www.instagram.com/reel/DJPZk9xpZaG/)')

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
    {"year": "2023", "title": "Inicié mis estudios en PUCP", "description": "Inicié la carrera de publicidad en PUCP, mis buenas notas me llevaron a ocupar el primer puesto de la promoción."},
    {"year": "Marzo 2024", "title": "Diseñadora en Huellitas", "description": "Ingresé a Huellitas en el puesto de diseñadora audiovisual."},
    {"year": "Marzo 2025", "title": "Coordinadora de Huellitas", "description": "Pasé a coordinar el área de comunicaciones, encargándome de las redes sociales y campañas."},
    {"year": "Mayo 2025", "title": "Ganadora de Concurso", "description": "Gané el concurso de Investigación Académica de Estudios Generales Letras."}
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
