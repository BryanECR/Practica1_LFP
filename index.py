from tkinter import filedialog

lista = []
#ARCHIVOS
def abrirArchivo():
    file_path = filedialog.askopenfilename(initialdir = "", title = "Abrir Archivo", filetypes = (("text files", "*.txt"),("all files", "*.*")) )
    archivo = open(file_path, 'r')
    c = archivo.readlines()
    archivo.close()

    #ORDENAR Y SEPARAR EL ARCHIVO
    for x in range(len(c)):
        palabra = c[x]
        d = palabra.split()
        lista.append(d)
    
    variable = '''
    ******** Abierto Correctamente ************
    '''
    print(variable)

#ORDENAMIENTO
def dist(lista):
    
    pivote = lista[0]
    menores = []
    mayores = []

    for i in range(1, len(lista)):

        if lista[i] < pivote:
            menores.append(lista[i])
        else:
            mayores.append(lista[i])
    
    return menores, pivote, mayores

def quicksort(lista):
     
    if len(lista) < 2:
        return lista
    
    menores, pivote, mayores = dist(lista)

    return quicksort(menores) + [pivote] + quicksort(mayores)


#BUSQUEDA
def busqueda(arr, buscado):
    palabra = arr.split(",")
    c = ''
    for index in range(len(palabra)):
        if buscado == palabra[index]:
            c += str(index) +" "
            
    return c

#REPORTE HTML
def reporte():
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="utf-8" />
        <title>Reporte</title>
        <style>
        body{
            background-color: cornflowerblue;
        }
        .titulos{
            text-align: center;
        }
        .contenido{
            margin: 75px;
            padding: 30px;
            background-color: #FBEAB6;
        }
        </style>
    </head>
    <body>
        <div class="contenido">
        <h1 class="titulos">Elementos de entrada</h1>
    """
    c = ""
    for var in range(len(lista)):
        c += str(lista[var])+"<br/>"
        
    html2 = """
        <h2 class="titulos">Elementos de Salida</h2>
        """

    datos = ""
    for numero in range(len(lista)):
        if len(lista[numero]) == 3:
                    
            datos += str(lista[numero][0])+" "+str(lista[numero][1])+" | Resultado ordenado: " + str(quicksort(lista[numero][1].split(",")))+"<br/>"
                    
        elif len(lista[numero]) == 4:
                    
            datos += str(lista[numero][0])+" "+str(lista[numero][1])+" | valor buscado: "+str(lista[numero][3])+" | valor encontrado en: "
                    
            datos += busqueda(lista[numero][1],str(lista[numero][3]))+"<br/>"
        elif len(lista[numero]) == 5:
                    
            datos += str(lista[numero][0])+" "+str(lista[numero][1])+" | Resultado ordenado: " + str(quicksort(lista[numero][1].split(",")))+"<br/>"
                    
            datos +=    str(lista[numero][0])+" "+str(lista[numero][1])+" | valor buscado: "+str(lista[numero][4])+" | valor encontrado en: "+str(busqueda(lista[numero][1],lista[numero][4]))+"<br/>"


    html3 = """
        </div>
    </body>
    </html>
    """
    file = open("Reporte.html","w")
    file.write(html+c+html2+datos+html3)
    file.close()


#MENU
def menu():
    while(True):
        print('**************** Menu *********************')
        print('*    1. Cargar Archivo de entrada         *')
        print('*    2. Desplegar Listas ordenadas        *')
        print('*    3. Desplegar Busqueda                *')
        print('*    4. Desplegar todas                   *')
        print('*    5. Desplegar todas del archivo       *')
        print('*    6. Salir                             *')
        print('*******************************************')
        
        opcion = int(input())

        if opcion == 1:
            abrirArchivo()
        elif opcion == 2:
            print("\n")

            for numero in range(len(lista)):

                if len(lista[numero]) == 3 or len(lista[numero]) == 5:
                    print(str(lista[numero][0])+" "+str(lista[numero][1])+" | Resultado ordenado: " + str(quicksort(lista[numero][1].split(","))))

            print("\n")

        elif opcion == 3:
            print('\n')
            for numero in range(len(lista)):
                if len(lista[numero]) == 4:
                    print(
                        str(lista[numero][0])+" "+str(lista[numero][1])+" | valor buscado: "+str(lista[numero][3])+" | valor encontrado en: "
                        )
                    print(busqueda(lista[numero][1],lista[numero][3]))

                elif len(lista[numero]) == 5:
                    print(
                        str(lista[numero][0])+" "+str(lista[numero][1])+" | valor buscado: "+str(lista[numero][4])+" | valor encontrado en: "+str(busqueda(lista[numero][1],str(lista[numero][4])))
                        )
            print('\n')       

        elif opcion == 4:

            print('\n')
            for numero in range(len(lista)):
                if len(lista[numero]) == 3:
                    print(
                        str(lista[numero][0])+" "+str(lista[numero][1])+" | Resultado ordenado: " + str(quicksort(lista[numero][1].split(",")))
                    )
                elif len(lista[numero]) == 4:
                    print(
                        str(lista[numero][0])+" "+str(lista[numero][1])+" | valor buscado: "+str(lista[numero][3])+" | valor encontrado en: "
                    )
                    print(busqueda(lista[numero][1],lista[numero][3]))
                elif len(lista[numero]) == 5:
                    print(
                        str(lista[numero][0])+" "+str(lista[numero][1])+" | Resultado ordenado: " + str(quicksort(lista[numero][1].split(",")))
                    )
                    print(
                        str(lista[numero][0])+" "+str(lista[numero][1])+" | valor buscado: "+str(lista[numero][4])+" | valor encontrado en: "+str(busqueda(lista[numero][1],lista[numero][4]))
                    )
            print('\n')

        elif opcion == 5:

            reporte()
            var = """ 
            **************** Reporte Generado Correctamente *******************************
            """
            print(var)

        elif opcion == 6:
            info = """
            Carnet: 201801155
            Nombre: Bryan Eduardo Caal Racanac
            Correo electronico: caal320@gmail.com
            Curso: Lenguajes formales de programacion
             """
            print(info)
            break
        else:
            print('Ingrese el numero de la opcion que desea por el teclado')

menu()