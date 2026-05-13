import streamlit as st
import base64

# CONFIGURAÇÃO DA PÁGINA
st.set_page_config(page_title="Perfil", layout="wide")

# FUNÇÃO PARA CONVERTER IMAGEM EM BASE64
def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# IMAGENS DO REPOSITÓRIO
img_base64 = get_base64_image("gucci.empresa.webp")
zap_base64 = get_base64_image("ZAP.png")

# TOPO COM IMAGEM CLICÁVEL
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 50px;">
            <a href="https://www.ifpb.edu.br/" target="_blank">
                <img src="data:image/webp;base64,{img_base64}"
                     width="320"
                     style="border-radius:12px;">
            </a>
        </div>
    """, unsafe_allow_html=True)

# LAYOUT PRINCIPAL
col_left, col_right = st.columns([3, 1])

with col_left:

    # NOME
    st.markdown("""
    <div style='margin-bottom:30px; font-size:30px;'>
        <b>Joana Silva</b>
    </div>
    """, unsafe_allow_html=True)

    # SUBCOLUNAS
    subcol1, subcol2 = st.columns([1, 4])

    # FOTO DE PERFIL
    with subcol1:

        st.markdown("""
        <div style="
            display:flex;
            justify-content:center;
            align-items:center;
            height:100%;
        ">
        """, unsafe_allow_html=True)

        st.image("foto.png.jpeg", width=250)

        st.markdown("</div>", unsafe_allow_html=True)

    # TEXTO
    with subcol2:

        st.markdown("""
        <div style="
            text-align: justify;
            font-size: 20px;
            line-height: 2.0;
            width: 100%;
        ">
            <b>Sobre Joana:</b><br><br>

            Joana Silva é estudante apaixonada por tecnologia,
            criatividade e inovação. Atualmente dedica seu tempo
            ao aprendizado de programação, desenvolvimento web
            e design digital.

            Gosta de participar de projetos acadêmicos,
            desenvolver novas habilidades e explorar soluções
            tecnológicas que possam impactar positivamente a sociedade.

            Seu objetivo é crescer profissionalmente na área de
            tecnologia e construir uma carreira voltada para
            desenvolvimento de sistemas e inovação digital.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='margin-top:30px;'>", unsafe_allow_html=True)

    # BOTÃO
    st.link_button(
        "Visitar Site",
        "https://www.gucci.com/pl/en_gb/"
    )

    st.markdown("</div>", unsafe_allow_html=True)

with col_right:
    st.empty()

# BOTÃO WHATSAPP
st.markdown(f"""
    <div style="text-align:center; margin-top:30px;">
        <a href="https://wa.me/5583998234415" target="_blank">
            <img src="data:image/png;base64,{zap_base64}" width="100">
        </a>
    </div>
""", unsafe_allow_html=True)
