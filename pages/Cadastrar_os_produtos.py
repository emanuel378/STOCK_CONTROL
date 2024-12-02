import streamlit as st

with open("styles_produto.css") as f:
    st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True) 

if "itens" not in st.session_state:
    st.session_state["itens"] = []

st.title("Cadastro de produto")

with st.form(key="item_cliente"):
    codigo = st.text_input("Código")
    nome = st.text_input("Nome")
    tipo = st.selectbox("Categoria", ["Eletrônico", "Alimentos", "Medicamentos", "Vestuário"])
    quantidade = st.number_input('Quantidade', min_value=1, step=1)
    preço = st.number_input('Preço', min_value=0.01, step=0.01)
    fornecedor = st.text_input("Fornecedor")
    
    botão = st.form_submit_button("Cadastrar")
   

    if botão:
        if not nome.strip():
            st.error("Coloque o nome do produto!")
        else:
            item = {
            "codigo":codigo,
            "nome":nome,
            "tipo":tipo,
            "quantidade":quantidade,
            "preço":preço,
            "fornecedor":fornecedor
        }
            st.session_state["itens"].append(item)
            st.success(f"Item '{nome}' cadastrado com sucesso!")
            st.switch_page("pages/Produtos.py")












       
       

        
    