'''
Codo a codo
INICIAL 2024 1C
Comisión 24084
Grupo 4

Integrantes:
            Elaine Amaya
            Gabriela Galmés
            Horacio Corpu
            Natalia Agüero
            Paola Tula

-------------------------------------------------------------------------------------------------------------------------------
Requisitos mínimos del proyecto:

El desarrollo del proyecto debe utilizar los elementos de Python vistos en clase, entre ellos
los siguientes:

● Variables y tipos simples: (OK)
● Listas y/o diccionarios: Emplear listas y/o diccionarios para almacenar datos de la aplicación.(OK)
● Entrada y salida por la Terminal:(OK)
● Condicionales: (OK)
● Bucles: (OK)
● Funciones:
            ● Validación de datos: Implementar alguna validación en la entrada de datos para
            minimizar los errores del usuario. (OK)
            
            ● Menú de opciones: El programa debe iniciar mostrando un menú con opciones y
            permitir al usuario elegir qué acción desea realizar. (OK)
            
            ● Agregar datos: Permitir al usuario ingresar nuevos datos a la colección con toda su
            información relevante.(OK)
            
            ● Eliminar datos: Dar la opción de eliminar datos de la colección.(OK)
            
            ● Listar datos: Mostrar todos los datos en la colección, con la opción de filtrar por
            diferentes criterios.(OK)
            
            ● Buscar datos: Permitir al usuario buscar un datos específico por su código o
            descripción.(OK)
            
            
-------------------------------------------------------------------------------------------------------------------------------
Sistema de Gestión de Stock para un Comercio 


Descripción General del Proyecto: (OK)
Este proyecto implica el desarrollo de un programa en Python diseñado para gestionar el stock de un comercio. 
El sistema estará equipado con un menú conmutador que permitirá a los usuarios navegar entre diferentes funcionalidades relacionadas 
con la manipulación y visualización de los datos (el inventario del comercio). 



Funcionalidades del Sistema: (OK)
Autenticación de Usuario: Acceso al sistema mediante un nombre de usuario y contraseña,
asegurando que solo el personal autorizado pueda gestionar el inventario.

Menú de Gestión de Productos: Una vez autenticados, los usuarios acceden a un menú que
ofrece las siguientes opciones:
                                ● Agregar Productos: Introducir nuevos productos en el sistema con todos sus detalles
                                relevantes. (OK)
                                
                                (*) Este inventario estará organizado en categorías de productos, cada una con atributos específicos como:
                                                                                        Categoría|
                                                                                                 |* Código de producto
                                                                                                 |* Nombre
                                                                                                 |* Cantidad en stock
                                                                                                 |* Precio
                                                                                                 |* Nacionalidad.
                                
                                ● Eliminar Productos: Remover productos del sistema que ya no se comercialicen (eliminación por lista->Código). (OK)
                                                                                        Eliminación|
                                                                                                   |*Listas stock categoría 1
                                                                                                   |*Listas stock categoría 2
                                                                                                   |*Listas stock categoría 3
                                                                                                   |*Listas stock categoría 4
                                                                                                                            |*Código del producto

                                ● Modificar Productos: Actualizar la información de cualquier producto, incluyendo cantidad en 
                                stock y precio. (OK)
                                                                                        Modificar|
                                                                                                 |*Modificar producto de la categoría 1
                                                                                                 |*Modificar producto de la categoría 2
                                                                                                 |*Modificar producto de la categoría 3
                                                                                                 |*Modificar producto de la categoría 4
                                                                                                                                       |*Modificar por Código
                                                                                                                                       |*Modificar por Nombre
                                                                                                                                       |*Listar para modificar
                                                                                                                                                              |*Modificar por Código
                                                                                                                                                                                                                               

                                ● Visualización del Stock (Un menú dedicado a la consulta de inventario permitiendo):
                                
                                                        * Información Detallada del Producto: Al buscar el Nambre del producto por su inicial,
                                                          se muestra una pantalla con todos los productos relacionados y los detalles del mismo. (OK)
                                                          
                                                        * Filtrar por Categoría (buscar o mostrar datos): Opción para visualizar productos según 
                                                          categorías  específicas. (OK)

                                                        * Ver Stock Total: Visualización de todos los productos en stock (listar datos).(OK)

                                                        
                                                        
                                                        
'''
#---------------------------------------------------------------------------------------------------------------------------------   
#---------------------------------------------------------------------------------------------------------------------------------   
# Bloque de la función Autentificación de usuario
def login():
    
    bandera1 = bool(False) # Inicialización de la variable
    
    while bandera1 == False: # se ejecuta mientras bandera1 == False 
        print() # Imprime para dejar espacio
        cadena = " Autentificación de Usuario "
        print(cadena.center(50,"*")) 
        print("-"*50)
        print("Nombre de Usuario: Ana / Contraseña: 1234")
        print("-"*50)
        nombre = input('Nombre de Usuario: ')
        clave = input('Contraseña: ')
        print("-"*50)
        if nombre == "Ana" and clave == "1234": # Clave de acceso
            bandera1 = bool(True) # Clave correcta: cierra el bucle
            global cat1 # Declaración como variable global  para su uso en todas las funciones (lista modificable)
            global cat2 # Declaración como variable global  para su uso en todas las funciones (lista modificable)
            global cat3 # Declaración como variable global  para su uso en todas las funciones (lista modificable)
            global cat4 # Declaración como variable global  para su uso en todas las funciones (lista modificable)
            cat1=[] #inicialización de la lista
            cat2=[] #inicialización de la lista
            cat3=[] #inicialización de la lista
            cat4=[] #inicialización de la lista
            menu_principal(cat1,cat2,cat3,cat4) # llama a la funcion y 
        else: # Clave incorrecta
            print ("Usuario o contraseña no válida.")
    
#---------------------------------------------------------------------------------------------------------------------------------          
#---------------------------------------------------------------------------------------------------------------------------------   
# Bloque de la función menú principal
def menu_principal(cat1,cat2,cat3,cat4): # Recibe como parametro las listas principales
    bandera2 = bool(False) # Inicialización de la variable
    while bandera2 == False: # se ejecuta mientras bandera2 == False 
        print() # Imprime para dejar espacio
        print("-"*50)
        cadena = " Menú de Gestión de Productos "
        print(cadena.center(50,"*")) 
        print("-"*50)
        opcion1 = input('''
        Elija una opción del menú principal:
        ● 1 - Agregar Producto.
        ● 2 - Eliminar Producto por Listas de Stock.
        ● 3 - Modificar Producto.
        ● 4 - Visualización del Menú de Stock.
        ● 5 - Salir
        :
        ''')
        
        match opcion1:
            case "1":
                agregar_producto(cat1,cat2,cat3,cat4) # llama a la función y para las listas
            case "2":
                eliminar_producto(cat1,cat2,cat3,cat4) # llama a la función y para las listas
            case "3":
                modificar_producto(cat1,cat2,cat3,cat4) # llama a la función y para las listasv
            case "4":
                menu_stock(cat1,cat2,cat3,cat4) # llama a la función y para las listas
            case "5":
                bandera2 = bool(True) # Cierra el bucle y sale
            case _:
                print ('Error al ingresar la opción.')
                
    print ('Fin del programa.') # salió e imprime
    return

# Bloque de la función Menú Principal-> Agregar Producto----------------------------------------------------------
def agregar_producto(cat1,cat2,cat3,cat4): # Recibe como parametro las listas principales
    categoria = []
    print() # Imprime para dejar espacio
    print("-"*50)
    cadena = " Agregar Producto "
    print(cadena.center(50,"*")) 
    print("-"*50)
    opcion3 = input('''
    Elija la categoría:
    ● 1 - Categoría 1.
    ● 2 - Categoría 2.
    ● 3 - Categoría 3.
    ● 4 - Categoría 4.
    ● 5 - Volver al Menú de Gestión de Productos
    :
    ''')
    match opcion3:
        case "1":
            categoria = cat1 # carga la lista en la variable
            carga(categoria) # llama a la función y pasa la variable lista
            cat1.append(nuevo_dic) # Pega a la lista el resultado retorno de función
            return cat1 # Retorna con la lista actualizada al menú principal
        case "2":
            categoria = cat2
            carga(categoria)
            cat2.append(nuevo_dic)
            return cat2
        case "3":
            categoria = cat3
            carga(categoria)
            cat3.append(nuevo_dic)
            return cat3
        case "4":
            categoria = cat4
            carga(categoria)
            cat4.append(nuevo_dic)
            return cat4
        case "5":
            return
        case _:
            print ('Error al ingresar la opción.')
            return # Retorna con la lista actualizada al menú principal
    
# Bloque de la función Menú Principal-> Agregar Producto -> carga
def carga(categoria): # recibe como parámetro una copia de la lista correspondiente
    global nuevo_dic # Declara como global la variable para sacarla fuera de la función
    nuevo_dic = {} # inicializa la variable
    codigo = len(categoria) # cuenta la cantidad de elementos en la lista
    codigo = codigo + 1 # suma el valor de código para el nuevo elemento
    literal_codigo = str(codigo) # conversión de la variable a literal
    print("Código: "+ literal_codigo) # nuestra el nuevo número de código para el producto agregado
    nombre = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad en stock: "))
    precio = float(input("Ingrese el precio en $: "))
    nacionalidad = input("Ingrese la nacionalidad del producto: ")
    
    nuevo_dic= {"Codigo":codigo,"Nombre":nombre,"Cantidad":cantidad,"Precio":precio,"Nacionalidad":nacionalidad} # genera al nuevo elemento y lo almacena

    print("Carga completada!")
    return nuevo_dic # Retorna con el diccionario para ser pegado en la lista correspondiente

# Bloque de la función Menú Principal-> Eliminar Producto por Listas de Stock.-------------------------------------------------
def eliminar_producto(cat1,cat2,cat3,cat4): # Recibe como parametro las listas principales
    categoria = [] # inicializa la variable
    print() # Imprime para dejar espacio
    print("-"*50)
    cadena = " Eliminar Producto por Lista de Stock "
    print(cadena.center(50,"*")) 
    print("-"*50)
    opcion4 = input('''
    Elija la opción de Ranking:
    ● 1 - Lista categoría 1.
    ● 2 - Lista categoría 2.
    ● 3 - Lista categoría 3.
    ● 4 - Lista Categoría 4.
    ● 5 - Volver al Menú de Gestión de Productos
    :
    ''')
    match opcion4:
        case "1":
            categoria = cat1 # carga la lista en la variable
            ranking(categoria) # llama a la función y pasa la variable lista
            categoria = cat1 # Actualiza la lista
            return cat1# Retorna con la lista actualizada al menú principal
        case "2":
            categoria = cat2
            ranking(categoria)
            categoria = cat2
            return cat2
        case "3":
            categoria = cat3
            ranking(categoria)
            categoria = cat3
            return cat3
        case "4":
            categoria = cat4
            ranking(categoria)
            categoria = cat4
            return cat4
        case "5":
            return
        case _:
            print ('Error al ingresar la opción.')
            return

# Bloque de la función Menú Principal-> Eliminar Producto por Listas de Stock -> Lista Cantidad - Código
def ranking(categoria): # recibe como parámetro una copia de la lista correspondiente
    lista_cantidades = [] # inicializa la variable
    cantidad_num = 0 # inicializa la variable
    filtro_vacio = len(categoria) # filro para listas vacia
    if filtro_vacio == None or filtro_vacio == 0: # se ejecuta si está vacia
        print()
        print("-"*50)
        cadena1 = " La categoría está vacia. "
        print(cadena1.center(50,"*")) 
        print("-"*50)
        return # retorna al menu de listas o ranking
    for i in range (len(categoria)): # bucle para recorrer toda la lista
        cantidad_num = categoria [i]["Cantidad"] # almacena el valor de la clave "cantidad"
        literal_cantidad = str(cantidad_num) # conversión a literal
        cod_num = categoria [i]["Codigo"]
        literal_codigo = str (cod_num)
        literal_orden = "Cantidad: "+ literal_cantidad + " - Código: " + literal_codigo # junta las variables en forma de literal
        lista_cantidades.append(literal_orden) # almacena las anteriores en una lista
    print() # Imprime para dejar espacio
    print("-"*50)
    cadena2 = " Listas de Stock "
    print(cadena2.center(50,"*")) 
    print("-"*50)
    for i in range (len(categoria)): # Bucle para "Acomodar" la lista
        salida = str(lista_cantidades[i])
        print(salida.center(50," "))
        print("-"*50)
    eliminar(categoria) # una vez mostrada la lista de referencia, llama a la función para la modificación de la lista
    print(categoria) # imprime la lista de retorno, ya modificada
    return categoria # retorna al menú y pasa la lista modificada

# Bloque de la función Menú Principal-> Eliminar Producto por Listas de Stock -> Listas -> Eliminar
def eliminar(categoria): # función de eliminacion de producto por código
    cadena = " Eliminar del Stock "
    print(cadena.center(50,"*")) 
    print("-"*50)
    num_eliminado = int(input("Ingresar el número de código del producto a eliminar: ")) # pide al usuario que ingrese el código
    puntero = num_eliminado - 1
    eliminado = categoria.pop(puntero) # Elimina y muestra
    print() # Imprime para dejar espacio
    print("¡Eliminación exitosa!")
    print() # Imprime para dejar espacio
    print("Se eliminó: ", eliminado) # muestra al eliminado
    return categoria # retorna con la lista modificada

# Bloque de la función Menú Principal-> Modificar Producto------------------------------------------------------------------------
def modificar_producto(cat1,cat2,cat3,cat4): # función para la modificación de producto que recibe como parametro las listas
    print() # Imprime para dejar espacio
    print("-"*50)
    cadena = " Modificar Producto "
    print(cadena.center(50,"*")) 
    print("-"*50)
    opcion5 = input('''
    Elija la ubicación del producto a modificar:
    ● 1 - Modificar producto de la categoría 1.
    ● 2 - Modificar producto de la categoría 2.
    ● 3 - Modificar producto de la categoría 3.
    ● 4 - Modificar producto de la categoría 4.
    ● 5 - Volver al Menú de Gestión de Productos
    :
    ''')
    match opcion5:
        case "1":
            categoria = cat1 # carga la lista en la variable
            modo_modificar(categoria) # llama a la función y pasa la variable lista
            categoria = cat1 # Actualiza la lista
            return cat1 # Retorna con la lista actualizada al menú principal
        case "2":
            categoria = cat2
            modo_modificar(categoria)
            categoria = cat2
            return cat2
        case "3":
            categoria = cat3
            modo_modificar(categoria)
            categoria = cat3
            return cat3
        case "4":
            categoria = cat4
            modo_modificar(categoria)
            categoria = cat4
            return cat4
        case "5":
            return
        case _:
            print ('Error al ingresar la opción.')
            return
            
# Bloque de la función Menú Principal-> Modificar Producto-> Modificar en categoría
def modo_modificar(categoria): # función que recibe como parámetro una copia de la lista correspondiente a modificar
    filtro_vacio = len(categoria) # filro para listas vacia
    if filtro_vacio == None or filtro_vacio == 0: # condicional para la lista vacia
        print() # Imprime para dejar espacio
        print("-"*50)
        cadena1 = " La categoría está vacia. "
        print(cadena1.center(50,"*")) 
        print("-"*50)
        return # retorna al menú modificar
    print() # Imprime para dejar espacio
    print("-"*50)
    cadena = " Búsqueda del producto a modificar "
    print(cadena.center(50,"*")) 
    print("-"*50)
    opcion5 = input('''
    Seleccione el tipo de búsqueda para la modificación:
    ● 1 - Modificación ingresando el Código.
    ● 2 - Modificación ingresando el Nombre.
    ● 3 - Mostrar toda la categoría en lista y modificar.
    ● 4 - Volver al Menú de Gestión de Productos
    :
    ''')
    match opcion5:
        case "1":
            modificar_por_codigo(categoria) # llama a la función y pasa la lista
            categoria = cat1 # actualiza la lista
            return cat1 # retorna con la lista actualizada
        case "2":
            modificar_por_nombre(categoria)
            categoria = cat2
            return cat2
        case "3":
            modificar_lista(categoria)
            categoria = cat3
            return cat3
        case "4":
            return # retorna al menú de nodificación
        case _:
            print ('Error al ingresar la opción.')
            return # retorna al menú de nodificación

# Bloque de la función Menú Principal-> Modificar Producto-> Modificar en categoría -> Modificar por Código
def modificar_por_codigo(categoria): # Funcion que recibe de parametro la lista
    encontrado = False # inicializacion de la variable
    indice = 0 # inicializacion de la variable
    num_codigo = int(input("Ingrese el número de codigo: "))
    while indice < len(categoria) and encontrado == False: # bucle para recorrer toda la lista para duscar el código
        if categoria[indice]["Codigo"] == num_codigo: # condicional que se cumple cuando encuentra el código buscado
            print("Producto a modificar:")
            print(f'Código: {categoria[indice]["Codigo"]} - Nombre: {categoria[indice]["Nombre"]} - Cantidad: {categoria[indice]["Cantidad"]} - Precio: {categoria[indice]["Precio"]} - Nacionalida: {categoria[indice]["Nacionalidad"]}')
            print() # Imprime para dejar espacio y comienza la carga de los nuevos parámetros
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad en stock: "))
            precio = float(input("Ingrese el precio en $: "))
            nacionalidad = input("Ingrese la nacionalidad del producto: ")
            categoria[indice]["Nombre"] = nombre # carga el nuevo parámetro
            categoria[indice]["Cantida"] = cantidad # carga el nuevo parámetro
            categoria[indice]["Precio"] = precio # carga el nuevo parámetro
            categoria[indice]["Nacionalidad"] = nacionalidad # carga el nuevo parámetro
            print("Producto modificado:")
            print(f'Código: {categoria[indice]["Codigo"]} - Nombre: {categoria[indice]["Nombre"]} - Cantidad: {categoria[indice]["Cantidad"]} - Precio: {categoria[indice]["Precio"]} - Nacionalida: {categoria[indice]["Nacionalidad"]}')
            print() # Imprime para dejar espacio
            encontrado = True # cierra el bucle y sale con parámetro encontrado
    if encontrado == False: # salió sin encontrar el parámetro
        print(f'El Código {num_codigo} no existe!')
        return # retorna sin modificar nada
    return categoria # retorna con la lista modificada

# Bloque de la función Menú Principal-> Modificar Producto-> Modificar en categoría -> Modificar por Nombre
def modificar_por_nombre(categoria): # deccripción IDEM al modificar por Código
    encontrado = False
    indice = 0
    nom_buscar =input("Ingrese el Nombre: ")
    while indice < len(categoria) and encontrado == False:
        if categoria[indice]["Nombre"] == nom_buscar:
            print("Producto a modificar:")
            print(f'Código: {categoria[indice]["Codigo"]} - Nombre: {categoria[indice]["Nombre"]} - Cantidad: {categoria[indice]["Cantidad"]} - Precio: {categoria[indice]["Precio"]} - Nacionalida: {categoria[indice]["Nacionalidad"]}')
            print()
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad en stock: "))
            precio = float(input("Ingrese el precio en $: "))
            nacionalidad = input("Ingrese la nacionalidad del producto: ")
            categoria[indice]["Nombre"] = nombre
            categoria[indice]["Cantida"] = cantidad
            categoria[indice]["Precio"] = precio
            categoria[indice]["Nacionalidad"] = nacionalidad
            print("Producto modificado:")
            print(f'Código: {categoria[indice]["Codigo"]} - Nombre: {categoria[indice]["Nombre"]} - Cantidad: {categoria[indice]["Cantidad"]} - Precio: {categoria[indice]["Precio"]} - Nacionalida: {categoria[indice]["Nacionalidad"]}')
            print() # Imprime para dejar espacio
            encontrado = True
    if encontrado == False:
        print(f'El Nombre {nom_buscar} no existe!')
        return
    return categoria
    
# Bloque de la función Menú Principal-> Modificar Producto-> Modificar en categoría -> Mostrar toda la categoría en lista y modificar
def modificar_lista(categoria): # Funcion que recibe la lista a modificar
    listar(categoria) # bloque de función perteneciente al menú de Stock, imprime una lista para tener una referencia del código del producto buscado
    modificar_por_codigo(categoria) # llama a la función correspondiente
    return categoria # retorna al menú con la lista modificada
    
    
#---------------------------------------------------------------------------------------------------------------------------------      
#---------------------------------------------------------------------------------------------------------------------------------  

# Bloque de la función Menú Principal -> Menú de Stock
def menu_stock(cat1,cat2,cat3,cat4): # Función que recibe como parámetro las listas principales
    bandera3 = bool(False) # inicializacion de la variable
    while bandera3 == False:
        print() # Imprime para dejar espacio
        print("-"*50)
        cadena = " Menú de Stock "
        print(cadena.center(50,"*")) 
        print("-"*50)
        opcion6 = input('''
        Elija una opción del menú de Stock:
        ● 1 - Información Detallada del Producto por búsqueda de inicial.
        ● 2 - Filtrar lista de Stock por Categoría.
        ● 3 - Ver listas de Stock de todas las categorías.
        ● 4 - Vover al Menú Principal
        :
        ''')
        match opcion6:
            case "1":
                detalles_producto(cat1,cat2,cat3,cat4) # Función que recibe como parámetro las listas principales
            case "2":
                filtrar_categoria(cat1,cat2,cat3,cat4) # Función que recibe como parámetro las listas principales
            case "3":
                categoria = cat1 # carga la lista en la variable
                print() # Imprime para dejar espacio
                print("Resultado del listado de la Categoría 1: ")
                listar(categoria) # Función correspondiente que pasa argumento de la lista
                if vacio == True: # condicional que se cumple si volvió de la funcion sin resultados
                    print("***LISTA VACIA***")
                categoria = cat2
                print() # Imprime para dejar espacio
                print("Resultado del listado de la Categoría 2: ")
                listar(categoria)
                if vacio == True:
                    print("***LISTA VACIA***")
                categoria = cat3
                print() # Imprime para dejar espacio
                print("Resultado del listado de la Categoría 3: ")
                listar(categoria)
                if vacio == True:
                    print("***LISTA VACIA***")
                categoria = cat4
                print() # Imprime para dejar espacio
                print("Resultado del listado de la Categoría 4: ")
                listar(categoria)
                if vacio == True:
                    print("***LISTA VACIA***")
            case "4":
                bandera3 = bool(True)
                return # retorna al menú principal
            case _:
                print ('Error al ingresar la opción.')
                


# Bloque de la función Menú Principal -> Menú de Stock -> Información Detallada del Producto ->Buscar por inicial
def detalles_producto(cat1,cat2,cat3,cat4): # Función que recibe como parámetro las listas principales
    categoria = [] # inicialización de la variable
    num_cat = 0 # inicialización de la variable
    letra1 = "" # inicialización de la variable
    print() # Imprime para dejar espacio
    inicial = input("Ingrese la inicial del producto a buscar: ")
    letra1 = inicial[0].lower() # selecciona la primera letra ingresada y la convierte en minúscula (condiciones que facilitan la búsqueda)
    vacio_cat1 = False # inicialización de la variable
    vacio_cat2 = False # inicialización de la variable
    vacio_cat3= False # inicialización de la variable
    vacio_cat4 = False # inicialización de la variable
    categoria = cat1 # carga la lista en la variable
    num_cat = 1 # carga el valor de la categoria en la variable (valor de referencia)
    encontrar(categoria,letra1,num_cat) # llama a la función y pasa los cuatro argumentos necesarios
    vacio_cat1 = vacio1 # almacena el valor la variable global de retorno de la función
    categoria =cat2
    num_cat = 2
    encontrar(categoria,letra1,num_cat)
    vacio_cat2 = vacio1
    categoria =cat3
    num_cat = 3
    encontrar(categoria,letra1,num_cat)
    vacio_cat3 = vacio1
    categoria =cat4
    num_cat = 4
    encontrar(categoria,letra1,num_cat)
    vacio_cat4 = vacio1
    if vacio_cat1 == True and vacio_cat2 == True and vacio_cat3 == True and vacio_cat4 == True: # condicional que se cumple cuando no encontro valor de búsqueda
        print() # Imprime para dejar espacio
        print("*** No se encontro resultado para la búsqueda. ***")
    
    
# Bloque de la función Menú Principal -> Menú de Stock -> Información Detallada del Producto ->Buscar por inicial -> Búsqueda
def encontrar(categoria,letra1,num_cat): # función que recibe los cuatro parámetros
    global vacio1  # declaración de la variable global para utilizarla fuera de la función
    lista_encontrados = [] # inicialización de la variable
    dic_encontrado = {} # inicialización de la variable
    filtra1 = len(categoria) # variable para filtrar la lista vacia
    if filtra1 == None or filtra1 == 0: # condicional que se cumple si la lista está vacia
        vacio1 = True
        return vacio1
    else: # condicional que se cumple si la lista no está vacia
        for i in range(len(categoria)): # bucle de búsqueda por inicial de la clave "Nombre"
            letra2 = str(categoria[i]["Nombre"]) # carga en la variable el valor de "Nombre"
            letra2 = letra2[0] # Filtra y almacena la primera letra
            letra2 = letra2.lower() # convierte a la letra en minúscula
            if letra1 == letra2: # condicional que compara la letra de búsqueda con la interada, se cumple si son iguales
                dic_encontrado = categoria[i] # carga la en la variable dicionario
                dic_encontrado["Cat"] = num_cat # integra y suma a la vez en la última posición del diccionario
                lista_encontrados.append(dic_encontrado) # a medida que va encontrando coincidencias, pega los elementos en la variable lista
        filtra2 = len(lista_encontrados) # filtro de lista vacia
        
        if filtra2 > 0: # condicional que se cumple cuando la lista de búsqueda no esta vacia
            imprimir_encontrados(lista_encontrados)
            vacio1 = False
            return vacio1
        else:  # condicional que se cumple cuando la lista de búsqueda esta vacia
            vacio1 = True
            return     
            
# Bloque de la función Menú Principal -> Menú de Stock -> Información Detallada del Producto ->Buscar por inicial -> Búsqueda -> Imprimir encontrados    
def imprimir_encontrados(lista_encontrados): # Función de impresión que recibe como parámetro la lista de productos encontrados en la búsqueda
    print() # Imprime para dejar espacio
    print("Resultados de la búsqueda: ")
    print("+","-"*10,"+","-"*10,"+","-"*60,"+","-"*20,"+","-"*20,"+","-"*30,"+") # Línea divisoria
    encabezado_categoria = "Categoria"
    encabezado_codigo = "Código"
    encabezado_nombre = "Nombre"
    encabezado_cantidad = "Cantidad"
    encabezado_precio = "Precio"
    encabezado_nacionalidad = "Nacionalidad"
    print("|",encabezado_categoria.center(10," "),"|",encabezado_codigo.center(10," "),"|",encabezado_nombre.center(60," "),"|",encabezado_cantidad.center(20," "),"|",encabezado_precio.center(20," "),"|", encabezado_nacionalidad.center(30," "),"|")
    print("+","-"*10,"+","-"*10,"+","-"*60,"+","-"*20,"+","-"*20,"+","-"*30,"+") # Línea divisoria
    indice = 0
    while indice < len(lista_encontrados):
        literal_categoria = str(lista_encontrados[indice]["Cat"])
        literal_codigo = str(lista_encontrados[indice]["Codigo"])
        literal_nombre = str(lista_encontrados[indice]["Nombre"]).capitalize()
        literal_cantidad = str(lista_encontrados[indice]["Cantidad"])
        literal_precio = str(lista_encontrados[indice]["Precio"])
        literal_nacionalidad = str(lista_encontrados[indice]["Nacionalidad"]).capitalize()
        print("|",literal_categoria.center(10," "),"|",literal_codigo.center(10," "),"|",literal_nombre.center(60," "),"|",literal_cantidad.center(20," "),"|",literal_precio.center(20," "),"|", literal_nacionalidad.center(30," "),"|")
        print("+","-"*10,"+","-"*10,"+","-"*60,"+","-"*20,"+","-"*20,"+","-"*30,"+") # Línea divisoria
        indice = indice + 1
    return   
    
# Bloque de la función Menú Principal -> Menú de Stock -> Filtrar por Categoría
def filtrar_categoria(cat1,cat2,cat3,cat4): # Función que recibe como parámetro las listas principales
    print() # Imprime para dejar espacio
    print("-"*50)
    cadena = " Filtrar Menú de Stock por Categoría "
    print(cadena.center(50,"*")) 
    print("-"*50)
    opcion5 = input('''
    Elija la ubicación del producto a modificar:
    ● 1 - Visualizar Menú de Stock categoría 1.
    ● 2 - Visualizar Menú de Stock categoría 2.
    ● 3 - Visualizar Menú de Stock categoría 3.
    ● 4 - Visualizar Menú de Stock categoría 4.
    ● 5 - Volver al Menú de Gestión de Productos
    :
    ''')
    match opcion5:
        case "1":
            categoria = cat1 # carga en la variable la lista correspondiente
            print() # Imprime para dejar espacio
            print("Resultado del listado de la Categoría 1: ")
            listar(categoria) # llamado a la función de impresión al pasarle el parámetro de lista
            if vacio == True: # Condicional que se cumple cuando la funcion no encontró elementos en la lista
                print("***LISTA VACIA***")
            return
        case "2":
            categoria = cat2
            print() # Imprime para dejar espacio
            print("Resultado del listado de la Categoría 2: ")
            listar(categoria)
            if vacio == True:
                print("***LISTA VACIA***")
            return
        case "3":
            categoria = cat3
            print() # Imprime para dejar espacio
            print("Resultado del listado de la Categoría 3: ")
            listar(categoria)
            if vacio == True:
                print("***LISTA VACIA***")
            return
        case "4":
            categoria = cat4
            print() # Imprime para dejar espacio
            print("Resultado del listado de la Categoría 4: ")
            listar(categoria)
            if vacio == True:
                print("***LISTA VACIA***")
            return # retorna al menú de Stock
        case "5":
            return# retorna al menú de Stock
        case _:
            print ('Error al ingresar la opción.')
            return# retorna al menú de Stock
        
# Bloque de la función Menú Principal -> Menú de Stock -> Ver Stock Total
def listar(categoria): # Función de impresión que recibe como parámetro la lista de productos encontrados en la búsqueda
    global vacio # declaración de la variable global para usarla fuera de la función
    vacio = False # inicialización de la variable
    filtro_vacio = len(categoria) # variable para filtrar la lista vacia
    if filtro_vacio == None or filtro_vacio == 0: # condicional que se cumple si la lista esta vacia
        vacio = True
        return vacio # retorna al menú de stock con el valor de lista vacia
    
    print() # Imprime para dejar espacio y comenzar la impresión
    print("+","-"*10,"+","-"*60,"+","-"*20,"+","-"*20,"+","-"*30,"+") # Línea divisoria
    encabezado_codigo = "Código"
    encabezado_nombre = "Nombre"
    encabezado_cantidad = "Cantidad"
    encabezado_precio = "Precio"
    encabezado_nacionalidad = "Nacionalidad"
    print("|",encabezado_codigo.center(10," "),"|",encabezado_nombre.center(60," "),"|",encabezado_cantidad.center(20," "),"|",encabezado_precio.center(20," "),"|", encabezado_nacionalidad.center(30," "),"|")
    print("+","-"*10,"+","-"*60,"+","-"*20,"+","-"*20,"+","-"*30,"+") # Línea divisoria
    indice = 0
    while indice < len(categoria):
        literal_codigo = str(categoria[indice]["Codigo"])
        literal_nombre = str(categoria[indice]["Nombre"]).capitalize()
        literal_cantidad = str(categoria[indice]["Cantidad"])
        literal_precio = str(categoria[indice]["Precio"])
        literal_nacionalidad = str(categoria[indice]["Nacionalidad"]).capitalize()
        print("|",literal_codigo.center(10," "),"|",literal_nombre.center(60," "),"|",literal_cantidad.center(20," "),"|",literal_precio.center(20," "),"|", literal_nacionalidad.center(30," "),"|")
        print("+","-"*10,"+","-"*60,"+","-"*20,"+","-"*20,"+","-"*30,"+") # Línea divisoria
        indice = indice + 1
    return categoria

    
#---------------------------------------------------------------------------------------------------------------------------------  
#---------------------------------------------------------------------------------------------------------------------------------  
# Bloque de la función principal
def main():
    login()
#---------------------------------------------------------------------------------------------------------------------------------  
#---------------------------------------------------------------------------------------------------------------------------------  

# Bloque del programa principal
main()
#---------------------------------------------------------------------------------------------------------------------------------  
#---------------------------------------------------------------------------------------------------------------------------------  
