import numpy as np 


peliculas = []
valor_entrada = 2500
asientos_ocupados = 44
contador = 0

def lista_asientos():

    lista = np.zeros((20,10))
    return lista

def agregar_peliculas():
    nombre = input("Ingrese pelicula: ")
    descripcion = input("Ingrese la descripcion de la pelicula: ")
    categoria = input("Ingrese su categoria: ")
    peliculas.append({"nombre": nombre, "descripcion": descripcion, "categoria": categoria })

def boucher(mensaje):
    archivo=open("Boletas.txt","w")
    archivo.write(str(mensaje)+"\n")
    archivo.close()

def seleccion_peliculas():
    for x in range(len(peliculas)):
        print(f"[{x+1}] {peliculas[x]}")

    n = int(input("Seleccione que pelicula quiere ver: "))
    n -= 1
    cartelera = (f"pelicula: {peliculas[n]}")
    print(cartelera)
    return cartelera

def cartelera_peliculas():
    for n in range(len(peliculas)):
        cartelera = (f"[{n+1}] Pelicula: {peliculas[n]}")
        print(cartelera)
    return cartelera
   
def menu__():
    print("---Menu---")
    menu = ["Nueva pelicula" , "Comprar entradas/Asientos", "Actualizar datos", "Calcular el total de ventas", "Calcular el total de entradas"]
    for x in range(len(menu)):
        print(f"[{x+1}] {menu[x]}")

    while True:
        try:
            opc = int(input("Agregar numerito: "))
            opc -= 1
            if opc == str:
                print("Error, vuelva a intentarlo.")
            else:
                break
        except ValueError:
            print("Error, vuelva a intentarlo.")

    if opc == 0:
        agregar_peliculas()
    elif opc == 1:
        comprar_entrada()
    elif opc == 2:
        actualizar_datos()
    elif opc == 3:
        calcular_ventas()
    elif opc == 4:
        calcular_entradas()

    return(menu, opc)

def buscador_asiento(asientos, fila, colum):

   if asientos[fila,colum] == asientos_ocupados:
     return True

   return False

def solicitar_asientos(asientos):

   contador = 1

   while True:

     while True:

       fila = int(input('fila del asiento 1-20: ')) - 1

       colum = int(input('columna del asiento 1-10: ')) - 1

       if (buscador_asiento(asientos,fila, colum)):

         print('ya existe')

       else:

         break
       
     asientos[fila, colum] = asientos_ocupados

     contador +=1

     if (contador > 1):

        break
       
def comprar_entrada():
    pelicula_elegida = seleccion_peliculas()
    print(asientos)
    print("Valor entrada: $2500")
    while True:
       try:
            dinero_ingresado = int(input("Ingrese la cantidad de dinero: "))
            if dinero_ingresado < 2500:
               print("Error, dinero insuficiente.")
            else:
               break
       except ValueError:
          print("Error, vuelva a intentarlo.")

    if dinero_ingresado == 2500:
       solicitar_asientos(asientos)
       print(asientos)
    elif dinero_ingresado > 2500:
        vuelto = dinero_ingresado - valor_entrada
        solicitar_asientos(asientos)
        print(asientos)
        print(f"Su vuelto es: ${vuelto}")

    
    
    boleta = (f"Num boleta: {contador+1} Cantidad pago :{dinero_ingresado}, {pelicula_elegida}")
    boucher(boleta)

def actualizar_datos():
    cartelera_peliculas()
    indice = int(input("Ingrese el número de la película a actualizar: "))
    pelicula = peliculas[indice-1]
    print("Datos actuales de la película:")
    print(f"Nombre: {pelicula['nombre']}")
    print(f"Descripción: {pelicula['descripcion']}")
    print(f"Categoría: {pelicula['categoria']}")
    nombre = input("Ingrese el nuevo nombre de la película (deje vacío para no modificar): ")
    descripcion = input("Ingrese la nueva descripción de la película (deje vacío para no modificar): ")
    categoria = input("Ingrese la nueva categoría de la película (deje vacío para no modificar): ")
    if nombre:
        pelicula['nombre'] = nombre
    if descripcion:
        pelicula['descripcion'] = descripcion
    if categoria:
        pelicula['categoria'] = categoria
    print("Datos de la película actualizados correctamente.")

def calcular_ventas():
    for pelicula in peliculas:
        num_entradas = sum(1 for fila in asientos for asiento in fila if asiento == 44)
        total_ventas = num_entradas * 2500
        print(f"Total de ventas de la película'{pelicula['nombre']}': ${total_ventas}")

def calcular_entradas():
    for pelicula in peliculas:
        num_entradas = sum(1 for fila in asientos for asiento in fila if asiento == 44)
        print(f"Total de ventas de la película'{pelicula['nombre']}': {num_entradas}")

asientos = lista_asientos()
menu__()
while True:
    print("Desea seguir? (1:SI 2:NO)")
    while True:
        try:
            opc = int(input("Ingrese la opcion deseaeda: "))
            if opc > 0 or opc < 3:
                break
            else:
                print("Error, vuelva a intentarlo.")
        except ValueError:
                print("Error, vuelva a intentarlo.")
    if opc == 1:
       menu__()
    elif opc == 2:
       break













