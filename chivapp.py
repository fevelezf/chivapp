import streamlit as st

class AplicacionViajes:
    def pagina_inicio(self):
        ciudades = ["Medellin", "San Pedro", "Concepcion", "Abejorral", "La Ceja", "Venecia", "Rionegro"]

        st.title("¡Bienvenido a tu Agencia de Viajes!")
        st.write("Selecciona tu origen y destino para encontrar tu próximo viaje.")

        self.origen = st.selectbox("Origen:", ciudades)
        self.destino = st.selectbox("Destino:", ciudades)
        self.personas = st.number_input("¿Cuántas personas viajan?", min_value=1, max_value=15, step=1)

    def pagina_reserva(self):
        st.header("Reserva para personas:")
        for i in range(self.personas):
            st.subheader(f"Datos de la persona {i + 1}")
            nombre = st.text_input(f"Nombre de la persona {i + 1}")
            cedula = st.text_input(f"Cédula de la persona {i + 1}")
            correo = st.text_input(f"Correo de la persona {i + 1}")

def main():
    app = AplicacionViajes()
    opcion = st.sidebar.radio("Navegación", ["Inicio", "Reserva"])

    if opcion == "Inicio":
        app.pagina_inicio()
    elif opcion == "Reserva":
        app.pagina_reserva()

if __name__ == "__main__":
    main()