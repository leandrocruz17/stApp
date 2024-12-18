import streamlit as st

st.title("FIRENZE - Registro de Entradas e Saídas")
st.write(
    "Registre uma foto do comprovante de Entrega ou Recebimento."
)
enable = st.checkbox("Habilitar Camera")
picture = st.camera_input("Registre uma foto", disabled=not enable)
if picture:
    st.image(picture)