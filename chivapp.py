import streamlit as st
import pandas as pd
from deta import Deta
import numpy as np



# Almacenamos la key de la base de datos en una constante
DETA_KEY = "e0skmnn4jhv_2yYwrWbkXboW2WwmQw31yL71eUu63nS4"

# Creamos nuestro objeto deta para hacer la conexion a la DB
deta = Deta(DETA_KEY)

# Inicializa la base de datos para usuarios, gastos e ingresos
# y fondos comunes
db_users = deta.Base("usuarios")
db_reservas = deta.Base("reservas")

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

# Función para verificar credenciales
def verificar_credenciales(username, password):
    '''Esta funcion recibe como argumento el username y el password y verifica que
    sean inguales para permitir el ingreso al sistema
    '''
    # Busca el usuario en la base de datos
    user = db_users.fetch({"username": username, "password": password})
    
    if user.count > 0:
        return True, "Inicio de sesión exitoso."
    else:
        return False, "Credenciales incorrectas. Por favor, verifique su nombre de usuario y contraseña."

# Función para registrar un nuevo usuario
def registro(username, password, first_name, last_name, email, confirm_password):
    '''Esta funcion usa la libreria tinydb para registrar un usuario en un archivo llamado
    db_users
    '''
    # Verifica si el usuario ya existe en la base de datos
    users = db_users.fetch({"username": username})
    
    # Si hay algún resultado, significa que el usuario ya existe
    if users.count > 0:
        return False, "El usuario ya existe. Por favor, elija otro nombre de usuario."

    # Verifica si las contraseñas coinciden
    if password != confirm_password:
        return False, "Las contraseñas no coinciden. Por favor, vuelva a intentar."

    # Agrega el nuevo usuario a la base de datos
    db_users.put({'username': username, 'password': password, 'first_name': first_name, 'last_name': last_name, 'email': email})

    return True, "Registro exitoso. Ahora puede iniciar sesión."

def busqueda_de_viajes():
    ciudades = ["Medellin", "San Pedro", "Concepcion", "Abejorral", "La Ceja", "Venecia", "Rionegro"]

    st.title("¡Bienvenido a tu Agencia de Viajes!")
    st.write("Selecciona tu origen y destino para encontrar tu próximo viaje.")
    with st.form('busqueda'):
        origen = st.selectbox("Origen:", ciudades)
        destino = st.selectbox("Destino:", ciudades)
        personas = st.number_input("¿Cuántas personas viajan?", min_value=1, max_value=15, step=1)
        fecha = st.date_input("Selecciona la fecha:")
        correo_r = st.text_input("Correo de quien Reserva")
        if st.form_submit_button('Reserva Right Now'):
            if origen != destino:
                pago = 0
                per=[]
                st.success("Viaje seleccionado con exito")
                numero_reserva = np.random.randint(10**7, 10**8)
                db_reservas.put({'numero_reserva':numero_reserva,'correo':str(correo_r),'origen':origen,'destino':destino, 'personas': str(personas), 'viajeros': list(per), 'costo':int(pago)})
                
                st.success(f'Reserva Guardada con exito con el numero {numero_reserva}')
                st.warning('Conserva el numero de la reserva, en caso de perderlo, deberas contactarte con el area tecnica')
                st.warning('Recuerda ir a la seccion de Detalles de la reserva para acceder a los detalles de esta')
                return origen, destino, personas, fecha,correo_r
            
            else:
                st.warning("El destino no puede ser igual al origen. Por favor, selecciona una ciudad diferente.")
    return None, None, None, None,None


            
def pagina_reserva(numero,personas,origen,destino,correo_r):
    global show_pago
    st.header("Reserva para personas:")
    reserva_data = db_reservas.fetch({'key': numero})
    # Verifica que 'personas' sea un número antes de continuar
    if not isinstance(personas, int):
        st.error("Error: El número de personas no es válido.")
        return
    with st.form('reserva'):
        per = []
        for i in range(personas):
            res=[]
            # Muestra los datos de las personas en las dos columnas
            st.write(f"Datos de la persona {i + 1}")       
            nombre = st.text_input(f"Nombre de la persona {i + 1}")
            res.append(nombre)
            cedula = st.text_input(f"Cédula de la persona {i + 1}")
            res.append(cedula)
            correo = st.text_input(f"Correo de la persona {i + 1}")
            res.append(correo)
            equipaje = st.selectbox(f"¿Lleva equipaje la persona {i + 1}?", ["Si", "No"])
            res.append(equipaje)

            per.append(res)
            
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
        pago = pagar*personas
        if st.form_submit_button('Guardar Reserva'):
            db_reservas.update({'viajeros': per}, key=numero)
            db_reservas.update({'costo': pago}, key=numero)
            
            numero_reserva = reserva_data['numero_reserva']

            st.success(f'Reserva Guardada con exito con el numero {numero_reserva} , por un costo de {pago}')
            st.warning('Conserva el numero de la reserva, en caso de perderlo, deberas contactarte con el area tecnica')
            

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
            st.success(f'Viaje confirmado desde {origen} con destino a {destino}')
            st.warning('Acercate a nuestras taquillas para Recibir tus tiquetes')
            st.success('FELIZ VIAJE')
        
        
        if st.form_submit_button("Confirmación del viaje"):
            st.success('confirmado')
###db_data.put({'username': username, 'Fecha': str(fecha), 'Tipo': 'Gasto', 'Categoría': categoria_gastos, 'Monto': monto})


def confirmacion(origen, destino):
    st.title(f'Viaje confirmado desde {origen} con destino a {destino}')
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

# Obtener el nombre de usuario actual después del inicio de sesión
def get_current_user():
    '''Esta funcion obtiene el nombre del usuario actual despues del inicio de sesion
    '''
    return st.session_state.get('username', None)

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


if get_current_user() is not None:
    # Sidebar menu options for logged-in users
    menu_option = st.sidebar.selectbox("Menú", ["Pagina Principal",'Detalles de la reserva', 'Busqueda de viajes',
                                                'Busqueda de chiva Rumbera', 'Conductor',
                                                'Administrar chivas', 'Verificar pagos',
                                                'Administrar viajes'])
    

    if menu_option == 'Busqueda de viajes':
        origen, destino, personas, fecha, correo_r = busqueda_de_viajes()

        #if origen is not None:
            # Realizar acciones adicionales o llamar a otras funciones según sea necesario
            #pagina_reserva(personas,origen,destino,correo_r)

        #else:
            # Manejar el caso en el que no se selecciona un viaje
            #st.warning("Por favor, selecciona un viaje antes de continuar.")
    

    elif menu_option == 'Detalles de la reserva':
        numero = st.text_input('Ingerese el numero de la reserva tal y como se le dio')
        if st.button('Buscar'):
            try:
                # Fetch the data
                response = db_reservas.fetch({'key': numero})
                st.write('LO ENCONTRE')
                # Check if there are any items in the response
                if response.count > 0:
                    # Access the first item (assuming only one item is fetched)
                    item = next(response.items())

                    # Access the fields using the keys
                    correo = item['correo']
                    origen = item['origen']
                    destino = item['destino']
                    personas = int(item['personas'])
                    viajeros = item['viajeros']
                    costo = int(item['costo'])

                    # Call the function with the fetched data
                    pagina_reserva(numero, personas, origen, destino, correo)
                else:
                    st.warning('No se encontró la reserva con el número proporcionado.')

            except Exception as e:
                st.warning(f'Error: {e}')

    elif menu_option == 'Busqueda de chiva Rumbera':
        salida, ruta, personas, fecha = busqueda_de_chiva_rumbera()
        
        #if st.button('Reserva Right Now'):
            #pagina_reserva()c

        if st.button('Pagar'):
            pago()

    elif menu_option == 'Conductor':
        st.header('Sección de conductor')
        col1,col2 = st.columns(2)

        if col1.button('Ver itinerario'):
            cargar_ruta()

        if col2.button('Cargar incapacidad'):
            conductor()

    elif menu_option == 'Administrar chivas':
        st.header('ASIGNACIONES')
        administrar_chivas()


    elif menu_option == 'Verificar pagos':
        st.header('PAGOS')
        administrar_pagos()


    elif menu_option == 'Administrar viajes':
        st.header('ASIGNACIONES')
        administrar_viajes()
    

else:
    # Sidebar menu options for non-logged-in users
    menu_option = st.sidebar.selectbox("Menú", ["Inicio", "Inicio de Sesion", "Registro","Conversion de Moneda",
                                                "Calculadora de Préstamos"])

# Si el usuario elige "Cerrar Sesión", restablecer la variable de sesión a None
if menu_option == "Cerrar Sesión":
    st.session_state.username = None
    st.success("Sesión cerrada con éxito. Por favor, inicie sesión nuevamente.")

# Si el usuario ya ha iniciado sesión, mostrar los botones
if get_current_user() is not None:
    username = st.session_state.username

    if menu_option == "Inicio de Sesion":
        st.write(f'<h4 style="font-size: 26px; font-weight: bold; text-align: center;">Hola {username}!</h4>', unsafe_allow_html=True)
        st.write("Bienvenido al inicio de la aplicación.")

        # Campos de inicio de sesión
        username = st.text_input("Nickname:")
        password = st.text_input("Contraseña:", type="password")
        
        colum1, colum2 = st.columns(2)
        if colum1.button("Iniciar Sesión"):
            login_successful, message = verificar_credenciales(username, password)
            if login_successful:
                st.success(message)
                # Almacenar el nombre de usuario en la sesión
                st.session_state.username = username  

            elif not login_successful:
                st.error(message)

else:
    if menu_option == "Inicio de Sesion":
        st.write("Bienvenido al inicio de la aplicación.")

        # Campos de inicio de sesión
        username = st.text_input("Nickname:")
        password = st.text_input("Contraseña:", type="password")
        
        colum1, colum2 = st.columns(2)
        if colum1.button("Iniciar Sesión"):
            login_successful, message = verificar_credenciales(username, password)
            if login_successful:
                st.success(message)
                # Almacenar el nombre de usuario en la sesión
                st.session_state.username = username  

            elif not login_successful:
                st.error(message)
        
        elif colum2.button("Olvidaste la contraseña"):
            try:
                if username is not None:
                    #user_info = db_users.get(User.username == username)

                    #email_recuperar = user_info['email']
                    #contraseña_recuperar = user_info['password']
                    #nombre = user_info['first_name']
                    #destinatario = email_recuperar  
                    #asunto = 'Recuperacion de Contraseña'
                    #cuerpo = (f'Hola {nombre} ,  Te enviamos este correo para recordarte la contraseña\n\n Usuario : {username} \n\n Contraseña : {contraseña_recuperar}  ')

                    st.success('Mensaje enviado con exito al correo registrado')

            except:
                if username is None:
                    st.warning('Ingresa el nombre del usuario')

                else:
                    st.warning('Debes registrarte')

    elif menu_option == "Registro":
        st.write("Registro de Usuario")

        # Campos de registro,
        first_name = st.text_input("Nombre del Usuario:")
        last_name = st.text_input("Apellidos del Usuario:")
        email = st.text_input("Correo electronico del Usuario:")
        new_username = st.text_input("Nickname:")
        new_password = st.text_input("Nueva Contraseña:", type = "password")
        confirm_password = st.text_input("Confirmar contraseña:", type = "password")

        # Crear dos columnas para los botones
        col1, col2 = st.columns(2)
        # Casilla de verificación para aceptar la política de datos personales
        # Inicializa la variable aceptar_politica
        
        # Variable de estado para rastrear si el usuario ha visto la política
        if 'politica_vista' not in st.session_state:
            st.session_state.politica_vista = False

        # Botón para abrir la ventana emergente en la segunda columna
        if col2.button("Ver Política de Tratamiento de Datos"):
            with open("politica_datos.txt", "r") as archivo:
                politica = archivo.read()
                with st.expander("Política de Tratamiento de Datos",expanded=True):
                    st.write(politica)
                    st.session_state.politica_vista = True
                # Casilla de verificación para aceptar la política
        aceptar_politica = st.checkbox("Acepta la política de datos personales")

        # Botón de registro de usuario en la primera columna
        if col1.button("Registrarse") and aceptar_politica and st.session_state.politica_vista:
            registration_successful, message = registro(new_username, new_password, first_name, last_name, email, confirm_password)
            if registration_successful:
                st.success(message)
                
            else:
                st.error(message)

        if not aceptar_politica:
            st.warning("Por favor, acepta la política de datos personales antes de registrarte.")

        if not st.session_state.politica_vista:
            st.warning("Por favor, ve la política de datos personales antes de registrarte.")




