import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
enable = st.checkbox("Enable camera")
picture = st.camera_input("Take a picture", disabled=not enable)
if picture:
    st.image(picture)