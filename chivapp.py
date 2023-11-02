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
    contraseña = st.text_input("Ingrese su contraseña:",type='password')
    if st.button('Iniciar sesión'):
        st.success('Inicio de sesión exitoso')
        audio_path = "corneta.mp3"
        audio_bytes = open(audio_path, "rb").read()
        st.audio(audio_bytes, format='audio/mp3', start_time=0)


    return usuario, contraseña

def registro():
    st.title("Registrarse")

    nombre = st.text_input("Ingrese su nombre:")
    apellidos = st.text_input("Ingrese sus apellidos:")
    usuario = st.text_input("Ingrese su usuario:")
    contraseña = st.text_input("Ingrese su contraseña:", type = 'password' )
    correo = st.text_input("Ingrese su correo:")

    if st.button('Registrarse'):
        st.success('Registro exitoso!')

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

def pago():
    st.header("Pago con codigo QR")
    st.title("Recuerda que si no cargas una foto, Se intuye que pagaras en efectivo en nuestras taquillas, y debe ser 4 horas antes del viaje")


    st.image("Qr_ChivApp.jpeg",caption="Consigna el valor de tu viaje aquí , Numero de cuenta : 912-210-16-772", use_column_width=True)
    st.title('Carga de Imágenes')

    uploaded_file = st.file_uploader("Selecciona una imagen", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Imagen seleccionada', use_column_width=True)
    
    
    st.button("Confirmación del viaje",on_click=confirmacion)


def confirmacion():
    st.title('Viaje confirmado con destino a Abejorral')
    st.write('Acercate a nuestras taquillas para Recibir tus tiquetes')
    st.success('FELIZ VIAJE')


def cargar_ruta():
    st.markdown('<h2 style="text-align: left; color: Black;">Revisar viajes</h2>',\
        unsafe_allow_html=True)
    st.image("Ruta.png",caption="Esta es su ruta: Medellín-Abejorral", use_column_width=True)
    
def conductor():
    uploaded_file = st.file_uploader("Selecciona una imagen", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Imagen seleccionada', use_column_width=True)
    st.button("Incapacidad recibida")
        


opciones = ['Inicio de sesion', 'Registrarse', 'Busqueda de viajes', 'Busqueda de chiva Rumbera', 'Conductor' ]

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
            st.button('Pagar',on_click=pago)
    else:
        st.warning("El destino no puede ser igual al origen. Por favor, selecciona una ciudad diferente.")

elif selected_option == 'Busqueda de chiva Rumbera':
    salida, ruta, personas, fecha = busqueda_de_chiva_rumbera()
    
    if st.button('Reserva Right Now'):
        pagina_reserva()

    if st.button('Pagar'):
        pago()

elif selected_option == 'Conductor':
    st.header('Sección de conductor')
    col1,col2 = st.columns(2)

    if col1.button('Ver itinerario'):
        cargar_ruta()

    if col2.button('Cargar incapacidad'):
        conductor()