import streamlit as st

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

def pagina_reserva():
    st.header("Reserva para personas:")
    personas = st.session_state.personas

    for i in range(personas):
        # Muestra los datos de las personas en las dos columnas
        st.write(f"Datos de la persona {i + 1}")       
        nombre = st.text_input(f"Nombre de la persona {i + 1}")
        cedula = st.text_input(f"Cédula de la persona {i + 1}")
        correo = st.text_input(f"Correo de la persona {i + 1}")
        equipaje = st.selectbox(f"¿Lleva equipaje la persona {i + 1}?", ["Si", "No"])

    if st.button('Seguir con el pago'):
        st.write('melo')

def pago():
    st.header("Pago")
    metodo = st.selectbox("¿Lleva equipaje la persona?", ["Qr", "Efectivo"])

    if metodo == "Qr":
        st.image("Qr_ChivApp.jpeg",caption="Consigna el valor de tu viaje aquí", use_column_width=True)
        st.title('Carga de Imágenes')

        uploaded_file = st.file_uploader("Selecciona una imagen", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            st.image(uploaded_file, caption='Imagen seleccionada', use_column_width=True)
            st.button("Confirmación del viaje")

    else:
        st.write("Dirígete al punto de pago de nuestras oficinas 2 horas antes del viaje")


opciones = ['Inicio de sesion', 'Registrarse', 'Busqueda de viajes', 'Busqueda de chiva Rumbera' ]

st.sidebar.title('Tabla de Contenido')
selected_option = st.sidebar.selectbox(
    'Selecciona una opción:', opciones)

if selected_option == 'Inicio de sesion':
    usuario, contraseña = inicio_de_sesion()

    if st.button('Ingresar'):
            if True:
                st.success("Ingreso correcto")
            else:
                st.warning("Verifique su usuario y su contraseña")    

elif selected_option == 'Registrarse':
    nombre, apellidos, usuario, contraseña, correo = registro()

    if st.button('Registrarse'):
        if True:
            st.success("Registro Valido")
        else:
            st.warning("Credenciales incorrectos")

elif selected_option == 'Busqueda de viajes':
    origen, destino, personas, fecha = busqueda_de_viajes()
    
    if st.button('Reserva Right Now'):
        if origen != destino:
            pagina_reserva()
        else:
            st.warning("El destino no puede ser igual al origen. Por favor, selecciona una ciudad diferente.")

    if st.button('Pagar'):
        pago()

elif selected_option == 'Busqueda de chiva Rumbera':
    salida, ruta, personas, fecha = busqueda_de_chiva_rumbera()
    
    if st.button('Reserva Right Now'):
        pagina_reserva()

    if st.button('Pagar'):
        pago()
