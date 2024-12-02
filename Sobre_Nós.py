import streamlit as st

with open("styles_sobrenos.css") as f:
    st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True) 

col1, col2 = st.columns([1, 3])  


with col1:
    st.image("pages/img2.jpeg", width=150)



with col2:
    st.title("Sobre Nós")
    st.write(
        "Bem-vindo à Stock.Control, a sua parceira em soluções inteligentes para gestão de estoque! "
        "Fundada com a missão de transformar a maneira como empresas gerenciam seus inventários, "
        "nossa empresa une tecnologia avançada com experiência prática para proporcionar um controle "
        "de estoque eficiente, preciso e fácil de usar."
    )


st.subheader("Por que Escolher a Stock.Control?")
st.write(
    "Com uma plataforma intuitiva e recursos avançados, possibilitamos que você tenha total controle "
    "sobre seu estoque, minimizando erros e facilitando a tomada de decisões. Seja qual for o seu segmento, "
    "estamos prontos para oferecer soluções personalizadas que acompanhem o crescimento da sua empresa."
)


if st.button("Fazer seu cadastro"):
    st.switch_page("pages/Cadastro_usuario.py")
    

