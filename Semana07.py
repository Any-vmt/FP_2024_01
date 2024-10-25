import streamlit as st

def verificar_contrasena():
    st.title("Verificación de contraseña")


    #Variable para alamacenar la contraseña
    contrasena_correcta = "asdasd"

    #Inicializar variable de sesión para almacenar la entrada del usuario
    if "contraseña_ingresada" not in st.sesion_state:
        st.session_state.contrasena_ingresada = ""
    
    #Input de la contraseña
    contrasena_ingresada =st.text_input("Ingrese la constraseña", type="password")

    #Boton para verificar la contraseña
    if st.button("Verificar"):
        if contrasena_ingresada == contrasena_correcta:
            st.session_state.contrasena_ingresada = contrasena_ingresada
            st.success("Bienvenido")
        else:
            st.error("Contrasena incorrecta, intente de nuevo")

#Llamada a la función principal
if __name__ == "__main__":
    verificar_contrasena()
