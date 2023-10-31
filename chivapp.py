import streamlit as st

def pagina_inicio():
    ciudades = ["Medellin", "San Pedro", "Concepcion", "Abejorral", "La Ceja", "Venecia", "Rionegro"]

    st.title("¡Bienvenido a tu Agencia de Viajes!")
    st.write("Selecciona tu origen y destino para encontrar tu próximo viaje.")

    origen = st.selectbox("Origen:", ciudades)
    destino = st.selectbox("Destino:", ciudades)
    personas = st.number_input("¿Cuántas personas viajan?", min_value=1, max_value=15, step=1)

    if st.button("Busca Tu Viaje"):
        if origen == destino:
            st.warning("El origen y el destino no pueden ser iguales. Por favor, selecciona ciudades diferentes.")
            
        else:
            st.success(f"Buscando vuelos desde {origen} a {destino}. ¡Pronto tendrás opciones disponibles!")
            return origen, destino, personas
            

def pagina_reserva(origen, destino, personas):
    st.header("Reserva para personas:")
    for i in range(personas):
        st.subheader(f"Datos de la persona {i + 1}")
        nombre = st.text_input(f"Nombre de la persona {i + 1}")
        cedula = st.text_input(f"Cédula de la persona {i + 1}")
        correo = st.text_input(f"Correo de la persona {i + 1}")

def main():
    opcion = st.selectbox("Navegación", ["Inicio", "Reserva"])

    if opcion == "Inicio":
        origen, destino, personas = pagina_inicio()
        pagina_reserva(origen, destino, personas)
        
    elif opcion == "Reserva":
        pagina_reserva(origen, destino, personas)

if __name__ == "__main__":
    main()