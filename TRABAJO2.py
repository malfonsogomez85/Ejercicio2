#INTEGRANTES
#-DARWIN JOAN ESQUIVEL ARENAS
#-JHON EDWARD SANCHEZ CASTILLO
#-Jhon Freddy Bernal Sarmiento
#-JUAN MANUEL MARTINEZ MARTINEZ
#-MARÍA MÓNICA ALFONSO GÓMEZ
 
import numpy as np

nomdiv={'COP':'Peso Colombiano', 'GBP':'Libra Esterlina', 'USD':'Dolar Americano', 'JPY':'Yen','EUR':'Euro'}
# Se emplea un diccionario para indexar los nombres de las divisas y emplear una referencia rapida para llamarla
#print(nomdiv.keys())
trm=np.arange(5,3, dtype=float)
#Listas:
Compra=[]
Venta=[]
print("  Bienvenido a Divertex")
print("**************************")
print("Seleccione una opcion: ")
print
while True:#se elabora un menu interactivo para que el usuario pueda ingresar una opción
    print("1. Comprar divisas: ")
    print("2. Vender divisas: ")
    print("3. Ver ganancias: ")
    print("4. Salir")
    opcion=int(input("La opcion que selecciono es: "))#permite al usuario elegir una opción
    break

