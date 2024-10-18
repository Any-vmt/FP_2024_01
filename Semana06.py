import streamlit as st

#Ejercicio05: generar e imprimir los números pares entre 0 y 100
st.title ("Ejercicios de números pares")
st.subheader ("Ejercicio 05: Números pares entre 0 y 100")
pares_0_100 = [i for i in range(0,101) if i % 2 == 0]
st.write("Números pares entre 0 y 100:")
st.write(pares_0_100)

#Ejercicio05: con boton
st.markdown("""
    <style>)
    div.stButton > button{
    background-color: #8B0000;
    color: white;
    font-size:16x;
    padding;10px;
    border-radius: 10px;
    border: none;
}
    </style>
""", unsafe_allow_html=True)

if st.button("Mostrar números pares entre 0 y 100"):
    pares0a100={}