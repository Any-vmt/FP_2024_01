import streamlit as st
import math

def calcular_area (area):
    return math.pi*(radio**2) 

def calcular_perimetro(radio):
    return 2*math.pi*radio

def main():
    st.title("Cálculo del área y perímetro de una circunferencia")

    radio = st.number_input("Ingrese el radio de la circunferencia:", min_value=0.0, step=0.1)

    if radio > 0:
        area = calcular_area(radio)

        st.write(f"Área:{area:.2f}")
        st.write(f"Perímetro:{perimetro:.2f}")
    else:
        st.write("Por favor, ingrese un radio mayor a cero.")
if __name__=="__main__":
    main()