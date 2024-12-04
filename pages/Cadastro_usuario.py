import streamlit as st

with open("styles.css") as f:
    st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True) 





if "inicio" not in st.session_state:
    st.session_state.inicio = 1
   

def cadastro():
    st.title("Seu cadastro")
    nome = st.text_input('Nome')
    email = st.text_input('Email', type='default')
    senha = st.text_input('Senha', type="password")
    

    if st.button("Cadastrar"):
        if not nome.strip():
            st.error("Coloque seu nome!")
        if "@gmail.com"not in email:
            st.error("O e-mail deve conter o formato @gmail.com")
       
        else:
            st.session_state.nome = nome
            st.session_state.email = email
            st.session_state.senha = senha
            st.session_state.inicio = 2  
            st.success("Cadastro realizado com sucesso,clique novante para sua informações")





      
      

def informacoes_usuario():
    st.title('Suas Informações')
    st.write(f"Nome: {st.session_state.nome}")
    st.write(f"Email: {st.session_state.email}")
    st.write(f"Senha: {st.session_state.senha}")
    st.success("Cadastro realizado com sucesso!")
   

    if st.button('Voltar para o cadastro'):
        st.session_state.inicio = 1 


if st.session_state.inicio == 1:
    cadastro()  
elif st.session_state.inicio == 2:
    informacoes_usuario()  

