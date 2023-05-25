#INTEGRANTES
#-DARWIN JOAN ESQUIVEL ARENAS
#-JHON EDWARD SANCHEZ CASTILLO
#-Jhon Freddy Bernal Sarmiento
#-JUAN MANUEL MARTINEZ MARTINEZ
#-MARÍA MÓNICA ALFONSO GÓMEZ
 
import numpy as np

nomdiv={'COP':'Peso Colombiano', 'GBP':'Libra Esterlina', 'USD':'Dolar Americano', 'JPY':'Yen','EUR':'Euro'}
ingresarDiv=()
# Se emplea un diccionario para indexar los nombres de las divisas y emplear una referencia rapida para llamarla
#print(nomdiv.keys())
trm=np.arange(5,3, dtype=float)
#Listas:#Se crea para que se inicialice antes de comenzar el programa
COP=[]
GBP=[]
USD=[]
JPY=[]
EUR=[]
print("  Bienvenido a Divertex")
print("**************************")
print("Seleccione una opcion: ")
print
while True:#se elabora un menu interactivo para que el usuario pueda ingresar una opción
    print("1. Comprar divisas: ")
    print("2. Vender divisas: ")
    print("3. Ver ganancias: ")
    print("4. Salir")
    opcion=int(input("Digite la opcion que desea"))#permite al usuario elegir una opción
    if opcion==1: #para que la seleccion sea multiple debemos usar if, elif y/o else
        #permite agregar datos y guardarlos sin necesidad de volver al menu para seleccionar nuevamente la opción, por medio de listas que a su vez son tuplas
        print("Ingrese la divisa que desea comprar")
        nomdiv=ingresarDiv(nomdiv)#retorna la lista con la divisa que agrego y guarda pisando la lista anterior con la nueva
    elif opcion==2:
        print("Ingrese la divisa que desea vender")
        nomdiv=ingresarDiv(nomdiv)
    elif opcion==3:    

    elif opcion==4:
        break    
    else:
        print("La opcion que selecciono es invalida")
