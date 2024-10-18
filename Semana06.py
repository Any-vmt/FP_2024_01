import streamlit as st

#Ejercicio05: generar e imprimir los números pares entre 0 y 100
st.title ("Ejercicios de números pares")
st.subheader ("Ejercicio 05: Números pares entre 0 y 100")
pares_0_100 = [i for in range(0,101) if i % 2 == 0]
st.write("Números pares entre 0 y 100:")
st.write(pares_0_100)

