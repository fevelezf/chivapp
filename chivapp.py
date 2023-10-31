import streamlit as st

# Lista de opciones para los menús desplegables de origen y destino
ciudades = ["Ciudad A", "Ciudad B", "Ciudad C", "Ciudad D"]  # Puedes agregar más ciudades

st.title("¡Bienvenido a tu Agencia de Viajes!")
st.write("Selecciona tu origen y destino para encontrar tu próximo viaje.")

origen = st.selectbox("Origen:", ciudades)
destino = st.selectbox("Destino:", ciudades)

if st.button("Buscar vuelos"):
    if origen == destino:
        st.warning("El origen y el destino no pueden ser iguales. Por favor, selecciona ciudades diferentes.")
    else:
        st.success(f"Buscando vuelos desde {origen} a {destino}. ¡Pronto tendrás opciones disponibles!")
