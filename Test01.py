import streamlit as st
#Titulo de la Aplicación
st.title("Introducción a variables y tipo de datos en Python")

#Creando 1era descripción inicial
st.write("Python es un lenguaje de programacion dinámico donde...")

#Sección para varibale de tipo entero
st.header("Ejemplo 01: Enteros")
st.write("En python, un entero (integer) es un número sin decimales")

#Definir una variable entera
int_variable = 42
st.code(f"int_variable = (int_variable)# tipo: (type(int_variable))")