import streamlit as st

def pagina_inicio():
    ciudades = ["Medellin", "San Pedro", "Concepcion", "Abejorral", "La Ceja", "Venecia", "Rionegro"]

    st.title("¡Bienvenido a tu Agencia de Viajes!")
    st.write("Selecciona tu origen y destino para encontrar tu próximo viaje.")

    origen = st.selectbox("Origen:", ciudades)
    destino = st.selectbox("Destino:", ciudades)
    personas = st.number_input("¿Cuántas personas viajan?", min_value=1, max_value=15, step=1)

    return origen, destino, personas

def pagina_reserva():
    st.header("Reserva para personas:")
    personas = st.session_state.personas
    for i in range(personas):
        st.subheader(f"Datos de la persona {i + 1}")
        nombre = st.text_input(f"Nombre de la persona {i + 1}")
        cedula = st.text_input(f"Cédula de la persona {i + 1}")
        correo = st.text_input(f"Correo de la persona {i + 1}")

def main():
    st.session_state.pagina_actual = "Inicio"
    
    if st.session_state.pagina_actual == "Inicio":
        origen, destino, personas = pagina_inicio()
        st.session_state.origen = origen
        st.session_state.destino = destino
        st.session_state.personas = personas
        
        if st.button('Reserva Right Now'):
            if st.session_state.origen != st.session_state.destino:
                st.session_state.pagina_actual = "Reserva"
            else:
                st.warning("El destino no puede ser igual al origen. Por favor, selecciona una ciudad diferente.")

    if st.session_state.pagina_actual == "Reserva":
        pagina_reserva()

if __name__ == "__main__":
    main()