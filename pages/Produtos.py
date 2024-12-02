import streamlit as st

with open("styles_produtosok.css") as f:
    st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html=True)


st.title("📦 Produtos Cadastrados")


if "itens" not in st.session_state:
    st.session_state["itens"] = [
        {"codigo": "P001", "nome": "Teclado", "tipo": "Eletrônico", "quantidade": 10, "preço": 150.00, "fornecedor": "Tech Supplies"},
        {"codigo": "P002", "nome": "Mouse", "tipo": "Eletrônico", "quantidade": 20, "preço": 75.00, "fornecedor": "Tech Supplies"},
    ]


if st.session_state["itens"]:
    for index, item in enumerate(st.session_state["itens"]):
        st.subheader(f"🛒 {item['nome']} (Código: {item['codigo']})")

        
        col = st.columns(1)[0] 
        with col:
            
            st.markdown(f"**Tipo:** {item['tipo']}")
            st.markdown(f"**Fornecedor:** {item['fornecedor']}")
            st.markdown(f"**Quantidade Disponível:** {item['quantidade']}")
            st.markdown(f"**Preço Unitário:** R$ {item['preço']:.2f}")

           
            quantidade_retirar = st.number_input(
                f"Quantidade a retirar de '{item['nome']}'",
                min_value=0,
                max_value=item["quantidade"],
                step=1,
                key=f"QuantidadeRetirar_{index}"
            )

            
            if st.button("🚚 Retirar", key=f"Retira_{index}"):
                if quantidade_retirar > 0:
                    item["quantidade"] -= quantidade_retirar
                    if item["quantidade"] == 0:
                        st.session_state["itens"].pop(index)
                        st.success(f"Item '{item['nome']}' foi totalmente retirado.")
                    else:
                        st.success(f"Retirado {quantidade_retirar} de '{item['nome']}'. Restam {item['quantidade']}.")
                else:
                    st.warning("Insira uma quantidade válida para retirada.")

           
            quantidade_adicionar = st.number_input(
                f"Quantidade a adicionar no estoque de '{item['nome']}'",
                min_value=0,
                step=1,
                key=f"QuantidadeAdicionar_{index}"
            )

            
            if st.button("➕ Adicionar Estoque", key=f"Adiciona_{index}"):
                if quantidade_adicionar > 0:
                    item["quantidade"] += quantidade_adicionar
                    st.success(f"Adicionado {quantidade_adicionar} ao estoque de '{item['nome']}'. Total: {item['quantidade']}.")
                else:
                    st.warning("Insira uma quantidade válida para adicionar.")

            st.divider() 
else:
    st.write("🔍 Nenhum item cadastrado.")
