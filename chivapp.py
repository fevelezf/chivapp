import streamlit as st

global show_pago

def busqueda_de_viajes():
    ciudades = ["Medellin", "San Pedro", "Concepcion", "Abejorral", "La Ceja", "Venecia", "Rionegro"]

    st.title("¡Bienvenido a tu Agencia de Viajes!")
    st.write("Selecciona tu origen y destino para encontrar tu próximo viaje.")

    origen = st.selectbox("Origen:", ciudades)
    destino = st.selectbox("Destino:", ciudades)
    personas = st.number_input("¿Cuántas personas viajan?", min_value=1, max_value=15, step=1)
    fecha = st.date_input("Selecciona la fecha:")

    return origen, destino, personas, fecha

def busqueda_de_chiva_rumbera():
    salida = ['Mall de la Mota' , 'CC La Central', 'Carlos E']
    recorridos = ["Las Palmas", "San Antonio de Pereira", "Alumbrados del Río", "Guatapé"]

    st.title("¡Bienvenido a tu Agencia de Viajes!")
    st.write("Selecciona el lugar de salida y tu ruta para tu chiva rumbera.")

    salida = st.selectbox("Salida:", salida)
    ruta = st.selectbox("Selecciona la ruta", recorridos)
    personas = st.number_input("¿Cuántas personas viajan?", min_value=15, max_value=30, step=1)
    fecha = st.date_input("Selecciona la fecha:")

    return salida, ruta, personas, fecha

def inicio_de_sesion():
    st.title("Inicio de sesión")

    usuario = st.text_input("Ingrese su usuario:")
    contraseña = st.text_input("Ingrese su contraseña:")

    return usuario, contraseña

def registro():
    st.title("Registrarse")

    nombre = st.text_input("Ingrese su nombre:")
    apellidos = st.text_input("Ingrese sus apellidos:")
    usuario = st.text_input("Ingrese su usuario:")
    contraseña = st.text_input("Ingrese su contraseña:")
    correo = st.text_input("Ingrese su correo:")

    return nombre, apellidos, usuario, contraseña, correo

def busqueda_de_viajes():
    

    ciudades = ["Medellin", "San Pedro", "Concepcion", "Abejorral", "La Ceja", "Venecia", "Rionegro"]

    st.title("¡Bienvenido a tu Agencia de Viajes!")
    st.write("Selecciona tu origen y destino para encontrar tu próximo viaje.")

    origen = st.selectbox("Origen:", ciudades)
    destino = st.selectbox("Destino:", ciudades)
    personas = st.number_input("¿Cuántas personas viajan?", min_value=1, max_value=15, step=1)
    fecha = st.date_input("Selecciona la fecha:")

    return origen, destino, personas, fecha

def pagina_reserva(personas):
    global show_pago
    st.header("Reserva para personas:")

    for i in range(personas):
        # Muestra los datos de las personas en las dos columnas
        st.write(f"Datos de la persona {i + 1}")       
        nombre = st.text_input(f"Nombre de la persona {i + 1}")
        cedula = st.text_input(f"Cédula de la persona {i + 1}")
        correo = st.text_input(f"Correo de la persona {i + 1}")
        equipaje = st.selectbox(f"¿Lleva equipaje la persona {i + 1}?", ["Si", "No"])

        st.button('Seguir con el pago', on_click=pago)


def qr():
    st.image("Qr_ChivApp.jpeg", caption="Consigna el valor de tu viaje aquí", use_column_width=True)
    st.title('Carga de Imágenes')
    uploaded_file = st.file_uploader("Selecciona una imagen", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Imagen seleccionada', use_column_width=True)
        st.button("Confirmación del viaje")

def efectivo():
    st.write("Dirígete al punto de pago de nuestras oficinas 2 horas antes del viaje")

def pago():
    st.header("Pago")
    
    st.title("Selecciona un método de pago")
    
    col1, col2 = st.columns(2)
    
    with col1:
        qr()

    with col2:
        efectivo()


opciones = ['Inicio de sesion', 'Registrarse', 'Busqueda de viajes', 'Busqueda de chiva Rumbera' ]

st.sidebar.title('Tabla de Contenido')
selected_option = st.sidebar.selectbox(
    'Selecciona una opción:', opciones)
if selected_option == 'Inicio de sesion':
    inicio_de_sesion()

if selected_option == 'Registrarse':
    registro()


elif selected_option == 'Busqueda de viajes':
    origen, destino, personas, fecha = busqueda_de_viajes()
    if origen != destino:
        st.success("Selección de origen y destino correcta")
        if st.button('Reserva Right Now'):
            pagina_reserva(personas)
    else:
        st.warning("El destino no puede ser igual al origen. Por favor, selecciona una ciudad diferente.")

elif selected_option == 'Busqueda de chiva Rumbera':
    salida, ruta, personas, fecha = busqueda_de_chiva_rumbera()
    
    if st.button('Reserva Right Now'):
        pagina_reserva()

    if st.button('Pagar'):
        pago()
