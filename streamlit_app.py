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
    import pytz
    # Define o fuso horário para -3:00 (Brasília) 
    timezone = pytz.timezone('America/Sao_Paulo')
    # Captura a data e hora atual no fuso horário especificado 
    now = datetime.now(timezone) 
    # Formata a data e hora 
    formatted_now = now.strftime("%d/%m/%Y %H:%M:%S") 
    # Exibe a data e hora no Streamlit 
    st.write(f"Registro efetuado em {formatted_now}!")