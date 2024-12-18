import streamlit as st

st.title("FIRENZE - Registro de Entradas e Saídas")
st.write(
    "Registre uma foto do comprovante de Entrega ou Recebimento."
)
enable = st.checkbox("Habilitar Camera")
picture = st.camera_input("Registre uma foto", disabled=not enable)
if picture:
    #st.image(picture)
    from datetime import datetime 
    # Captura a data e hora atual 
    now = datetime.now() 
    # Formata a data e hora 
    formatted_now = now.strftime("%d/%m/%Y %H:%M:%S") 
    # # Exibe a data e hora no Streamlit 
    st.write(f"Registro efetuado em {formatted_now}!")