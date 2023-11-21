import streamlit as st
import pandas as pd

global show_pago

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

    with st.form("inicio"):
        usuario = st.text_input("Ingrese su usuario:")
        contraseña = st.text_input("Ingrese su contraseña:",type='password')
        if st.form_submit_button('Iniciar sesión'):
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
    with st.form('busqueda'):
        origen = st.selectbox("Origen:", ciudades)
        destino = st.selectbox("Destino:", ciudades)
        personas = st.number_input("¿Cuántas personas viajan?", min_value=1, max_value=15, step=1)
        fecha = st.date_input("Selecciona la fecha:")
        if st.form_submit_button('Reserva Right Now'):
            if origen != destino:
                st.success("Viaje seleccionado con exito")
                return origen, destino, personas, fecha
            
            else:
                st.warning("El destino no puede ser igual al origen. Por favor, selecciona una ciudad diferente.")
    return None, None, None, None


            
def pagina_reserva(personas,origen,destino):
    global show_pago
    st.header("Reserva para personas:")

    # Verifica que 'personas' sea un número antes de continuar
    if not isinstance(personas, int):
        st.error("Error: El número de personas no es válido.")
        return
    reserva = False
    with st.form('reserva'):
        per = {}
        for i in range(personas):
            # Muestra los datos de las personas en las dos columnas
            st.write(f"Datos de la persona {i + 1}")       
            nombre = st.text_input(f"Nombre de la persona {i + 1}")
            cedula = st.text_input(f"Cédula de la persona {i + 1}")
            correo = st.text_input(f"Correo de la persona {i + 1}")
            equipaje = st.selectbox(f"¿Lleva equipaje la persona {i + 1}?", ["Si", "No"])

        if st.form_submit_button('Pagar'):
            reserva = True
            return reserva
    
    return reserva
            

def pago(personas,origen,destino):

    with st.form('pago'):
        st.header("Pago con codigo QR")
        if origen == "Medellin":
            if destino == "San Pedro":
                pagar= 13000
            elif destino == "Concepcion":
                pagar= 12500
            elif destino == "Abejorral":
                pagar= 20000
            elif destino == "La Ceja":
                pagar= 12000
            elif destino == "Venecia":
                pagar= 12000
            elif destino == "Rionegro": 
                pagar= 12000
        elif origen == "San Pedro":
            if destino == "Medellin":
                pagar= 13000
            elif destino == "Concepcion":
                pagar= 32000
            elif destino == "Abejorral":
                pagar= 20000
            elif destino == "La Ceja":
                pagar= 32000
            elif destino == "Venecia":
                pagar= 50000
            elif destino == "Rionegro": 
                pagar= 30000
        elif origen == "Concepcion":
            if destino == "San Pedro":
                pagar= 32000
            elif destino == "Medellin":
                pagar= 13000
            elif destino == "Abejorral":
                pagar= 34000
            elif destino == "La Ceja":
                pagar= 20000
            elif destino == "Venecia":
                pagar= 34000
            elif destino == "Rionegro": 
                pagar= 12000
        elif origen == "Abejorral":
            if destino == "San Pedro":
                pagar= 30000
            elif destino == "Concepcion":
                pagar= 12000
            elif destino == "Medellin":
                pagar= 13000
            elif destino == "La Ceja":
                pagar= 12700
            elif destino == "Venecia":
                pagar= 23200
            elif destino == "Rionegro": 
                pagar= 14750
        elif origen =="La Ceja" :
            if destino == "San Pedro":
                pagar= 22340
            elif destino == "Concepcion":
                pagar= 15450
            elif destino == "Abejorral":
                pagar= 12000
            elif destino == "Medellin":
                pagar= 23000
            elif destino == "Venecia":
                pagar= 11000
            elif destino == "Rionegro": 
                pagar= 12300
        elif origen =="Venecia":
            if destino == "San Pedro":
                pagar= 12400
            elif destino == "Concepcion":
                pagar= 15000
            elif destino == "Abejorral":
                pagar= 25000
            elif destino == "La Ceja":
                pagar= 23000
            elif destino == "Medellin":
                pagar= 23000
            elif destino == "Rionegro": 
                pagar= 12000
        elif origen == "Rionegro":
            if destino == "San Pedro":
                pagar= 12000
            elif destino == "Concepcion":
                pagar= 13000
            elif destino == "Abejorral":
                pagar= 12000
            elif destino == "La Ceja":
                pagar= 24000
            elif destino == "Venecia":
                pagar= 34000
            elif destino == "Medellin": 
                pagar= 32000

        st.write(f'El pago a efectuar es por el monto de {pagar*personas}')
        st.title("Recuerda que si no cargas una foto, Se intuye que pagaras en efectivo en nuestras taquillas, y debe ser 4 horas antes del viaje")


        st.image("Qr_ChivApp.jpeg",caption="Consigna el valor de tu viaje aquí , Numero de cuenta : 912-210-16-772", use_column_width=True)
        st.title('Carga de Imágenes')

        uploaded_file = st.file_uploader("Selecciona una imagen", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            st.image(uploaded_file, caption='Imagen seleccionada', use_column_width=True)
        
        
        if st.form_submit_button("Confirmación del viaje"):
            confirmacion(origen,destino)


def confirmacion(origen, destino):
    st.title(f'Viaje confirmado desde{origen} con destino a {destino}')
    st.write('Acercate a nuestras taquillas para Recibir tus tiquetes')
    st.success('FELIZ VIAJE')



def administrar_pagos():
    user_data = pd.read_csv('datos.csv')
    df = pd.DataFrame(user_data)
    st.write(df)


def cargar_ruta():
    st.markdown('<h2 style="text-align: left; color: Black;">Revisar viajes</h2>',\
        unsafe_allow_html=True)
    st.image("Ruta.png",caption="Esta es su ruta: Medellín-Abejorral", use_column_width=True)
    
def conductor():
    uploaded_file = st.file_uploader("Selecciona una imagen", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption='Imagen seleccionada', use_column_width=True)
    st.button("Incapacidad recibida")
        
def administrar_chivas():
        st.header("Administrar chivas y conductores")
        with st.form("registrar_gasto_form"):
            # Cambiar el campo de texto por un menú desplegable para la categoría
            vehiculos = st.selectbox("Seleccione la chiva:", ["ABC123", "DEF456", "GHI789", "JKL012", "MNO345", "PQR678", "STU901", "VWX234", "YZA567"])
            conductores = st.selectbox("Seleccione el conductor:",
    ["Don Ramón", "Chapulín Colorado", "La Chilindrina", "El Chavo del 8", "Doña Florinda", "El Profesor Jirafales", "Quico", "Ñoño"]
)
            if st.form_submit_button("Registrar"):
                st.success("Asigancion exitosa.")

def administrar_viajes():
        st.header("Administrar viajes")
        with st.form("registrar_gasto_form"):
            # Cambiar el campo de texto por un menú desplegable para la categoría
            origen = st.selectbox("Seleccione el origen:", ["Medellin", "San Pedro", "Concepcion", "Abejorral", "La Ceja", "Venecia", "Rionegro"])
            destino = st.selectbox("Seleccione el destino:",
    ["Medellin", "San Pedro", "Concepcion", "Abejorral", "La Ceja", "Venecia", "Rionegro"]
)
            if st.form_submit_button("Registrar"):
                st.success("Asigancion exitosa.")


opciones = ['Inicio de sesion', 'Registrarse', 'Busqueda de viajes', 'Busqueda de chiva Rumbera', 'Conductor' ,'Administrar chivas', 'Administrar viajes','Verificar pagos']

st.sidebar.title('Tabla de Contenido')
selected_option = st.sidebar.selectbox(
    'Selecciona una opción:', opciones)
if selected_option == 'Inicio de sesion':
    inicio_de_sesion()

if selected_option == 'Registrarse':
    registro()


elif selected_option == 'Busqueda de viajes':
    origen, destino, personas, fecha = busqueda_de_viajes()

    if origen is not None:
        # Realizar acciones adicionales o llamar a otras funciones según sea necesario
        pagina_reserva(personas,origen,destino)
        pago(personas,origen,destino)

    else:
        # Manejar el caso en el que no se selecciona un viaje
        st.warning("Por favor, selecciona un viaje antes de continuar.")


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

elif selected_option == 'Administrar chivas':
    st.header('ASIGNACIONES')
    administrar_chivas()


elif selected_option == 'Verificar pagos':
    st.header('PAGOS')
    administrar_pagos()


elif selected_option == 'Administrar viajes':
    st.header('ASIGNACIONES')
    administrar_viajes()


