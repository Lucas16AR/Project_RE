#MENU
MENU = '''
    |-------------------------------------------------------------------|
    |                 Bienvenido/as a RE SOFTWARE                       |
    |                                                                   |
    |                      Elija una opcion                             |
    |                                                                   |
    | 1. Listar todas las sesiones por ID                               |
    | 2. Listar los inicios de session en un periodo de tiempo          |
    | 3. Tiempo total de la sesion de un usuario                        |
    | 4. Mac de un usuario y cantidad de veces que se uso               |
    | 5. Mac de un usuario y a que dispositivo se conecto               |
    | 6. Listar usuarios conectados a una AP con un rango de fechas     |
    | 7. Listar usuarios conectados a una AP en una fecha determinada   |
    | 8. Salir                                                          |
    |-------------------------------------------------------------------|

    '''

#REGEX
DATETIME_REGEX = r'\d{2}/\d{2}/\d{4}\s\d{2}:\d{2}:\d{2}'

#PATHS
PATH_TXT = r"../docs/usuarios.txt"
FULLPATH_TXT = r"/home/lucas1608/Universidad/Project-RE/docs/usuarios.txt"
PATH_XLSX = r"../docs/usuarios.xlsx"
FULLPATH_XLSX = r"/home/lucas1608/Universidad/Project-RE/docs/usuarios.xlsx"
USERS_SESSIONS = r"/home/lucas1608/Universidad/Project-RE/files/Users_Sessions_ID.xlsx"
USERS_SESSIONS_DATE = r"/home/lucas1608/Universidad/Project-RE/files/User_Sessions_Date.xlsx"
TOTAL_SESSION_TIME = r"/home/lucas1608/Universidad/Project-RE/files/Total_Session_Time.xlsx"
MAC_USER = r"/home/lucas1608/Universidad/Project-RE/files/Mac_User.xlsx"
MAC_USER_INFO = r"/home/lucas1608/Universidad/Project-RE/files/Mac_User_Info.xlsx"
MAC_AP_RANGE = r"/home/lucas1608/Universidad/Project-RE/files/Mac_AP_Range.xlsx"
MAC_AP_DATE = r"/home/lucas1608/Universidad/Project-RE/files/Mac_AP_Date.xlsx"

#INPUTS
QUESTION_RET = "Volver a menu principal? (Y/n) "
INP_SHOW_DATA = "Ver informacion completa de las conexiones? (Y/n) "
UN_INP = "Nombre de Usuario: "
DATETIME_INPUT = "Ingrese la fecha, con el formato >>> DD/MM/YYYY HH:MM:SS: "
DATETIME_INPUT_1 = "Ingrese la fecha con este formato >>> DD/MM/YYYY HH:MM:SS : "
DATETIME_INPUT_2 = "Ingrese la fecha con este formato >>> DD/MM/YYYY HH:MM:SS : "
DATETIME_RANGE_INPUT = "Quiere usar un rango de tiempo para buscar? (Y/N) "
MAC_USER_INP = "Ingrese la MAC del Usuario para analizar: "
AP_INPUT = "Ingrese la MAC AP para buscar: "
SPECIFIC_DATE_INPUT = "Ingrese una fecha fija con este formato >>> DD/MM/YYYY HH:MM:SS :  "

#MESSAGES
RETURN_MENU = "Menu principal"
SEARCHING_DATA = "Buscando"
LOADING_DATA = "Cargando"
LOAD_DATA = "Carga correcta"
CLIENT_ADDED = "Cliente añadido"
DELETE_DATA = "Datos Borrados"
CLIENT_ATTENDED = "Todos los clientes ya han sido atendidos"
USER_NOT_FOUND = "No existe el usuario"
MAC_NOT_FOUND = "No existe la MAC"
WRONG_DT_1 = "Valores ingresados en formato incorrecto"
WRONG_DT_2 = "Valores ingresados en formato incorrecto"
INSC_FALSE = "No puede inscribirse."
INSC_TRUE = "Inscripcion correcta"
NOT_INT_DNI = "Ingrese el digito entero"
INP_FB = "Opcion elegida: "
INFO_HELP = "Testeo"
VALIDATE_CHECKING = "Validando"
VALIDATE_CORRECT = "Datos validados"
DATETIME_RANGE_MSG = "Ingrese un rango de fechas"
DT_RANGE_MSG = "Setee un rango de fechas"
TO_EXCEL = "Para mas detalles, vea el excel"
CHECK_XLSX = "Para mas detalles, vea el excel 'Usuarios WiFi'"

#STRINGS OPERATIONS
JUMP_LINE = "\n"

#EXIT
EXIT = "Saliendo. Hasta Luego"