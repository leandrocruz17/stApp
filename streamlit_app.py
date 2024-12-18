import streamlit as st
from streamlit_option_menu import option_menu

# Configurações da página 
st.set_page_config(page_title="FIRENZE")
st.title("FIRENZE - Registro de Entradas e Saídas")
st.write(
    "Registre uma foto do comprovante de Entrega ou Recebimento."
)

# Menu lateral
with st.sidebar:
    selected = option_menu(
        "Menu",
        ["Cadastros", "Suprimentos", "Vendas", "Finanças", "RH"],
        icons=["person", "box", "cart", "currency-dollar", "people"],
        menu_icon="cast",
        default_index=0,
    )

# Incluir CSS para criar o submenu ao passar o mouse 
st.markdown(""" <style> /* Esconder inicialmente os submenus */ 
            nav[data-testid="stSidebarNav"] 
            ul div:nth-child(2) > ul { display: none; } 
            /* Mostrar o submenu ao passar o mouse */ 
            nav[data-testid="stSidebarNav"] 
            ul div:nth-child(2):hover > ul 
            { display: block; position: absolute; 
            left: 250px; top: 0; background: white; 
            width: 200px; border: 1px solid #ccc; z-index: 1000; } 
            nav[data-testid="stSidebarNav"] ul div:nth-child(2) > ul > li 
            { padding: 10px; list-style: none; } </style> """, 
            unsafe_allow_html=True) 
# Adicionar submenus manualmente 
if selected == "Cadastros": 
    submenu = st.sidebar.radio( "Cadastros", ["Parceiros", "Produtos", "Vendedores"] )
# Opção de entrega ou recebimento 
option = st.selectbox("Selecione a operação:", ["Entrega", "Recebimento"]) 
# Campo de texto para informar o parceiro 
partner = st.text_input("Informe o parceiro:")
enable = st.checkbox("Habilitar Camera")
picture = st.camera_input("Registre uma foto", disabled=not enable)
if picture:
    #st.image(picture)
    from datetime import datetime 
    import pytz
    # Define o fuso horário para -3:00 (Brasília) 
    timezone = pytz.timezone('America/Sao_Paulo')
    # Captura a data e hora atual no fuso horário especificado 
    now = datetime.now(timezone) 
    # Formata a data e hora 
    formatted_now = now.strftime("%d/%m/%Y %H:%M:%S") 
    # Exibe a data e hora no Streamlit 
    st.write(f"Registro de {option}: {partner.upper()} efetuado em {formatted_now}!")

st.write("Desenvolvido por [@Leandro Cruz](https://github.com/leandrocruz17)")