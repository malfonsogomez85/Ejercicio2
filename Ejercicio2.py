""" 
Ejercicio #2 Python - Uso de Diccionarios, Tuplas, Sets  y Listas
Diplomado de Machine Learning en Python - CUN

Grupo N° 2
Integrantes:
Maria Monica Alfonso Gomez
Darwin Joan Esquivel Arenas
Juan Manuel Martinez
Jhon Eduard Sanchez
Jhon Fredy Bernal Sarmiento
"""
 
import numpy as np 
# Se importa la libreria numpy
import pandas as pd
# Se importa la libreria pandas

import datetime
import locale
# Configurar el idioma local en español
locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
# Obtener la fecha actual
fecha_actual = datetime.datetime.now()
# Formatear la fecha en formato largo
fecha_larga = fecha_actual.strftime("%A, %d de %B de %Y")


np.set_printoptions(precision=2, suppress=True)
# Para evitar que se muestre la notación científica al imprimir un arreglo multidimensional numérico en NumPy

n = 5 
# Posiciones que van a tener los arreglos, tuplas, set y diccionarios

# nomdiv={'COP':'Peso Colombiano', 'GBP':'Libra Esterlina', 'USD':'Dolar Americano', 'JPY':'Yen','EUR':'Euro'}
divisa=['Peso Colombiano', 'Libra Esterlina', 'Dolar Americano', 'Yen','Euro'] # Lista con la Definicion de Divisas
asgn=['TRM', 'Precio Compra', 'Precio Venta'] # Lista con las actividades a realizar con las tasas
trm=np.zeros((3,5), dtype=float) # Arreglo multidimensional de 5 x 3 para almacenar los datos diarios de TRM

df = pd.DataFrame(index=asgn, columns=divisa) 
# Dataframe gestionado con pandas para presentar datos a partir del arreglo trm
# Contiene los datos de filas y columnas obtenidos de los arreglos divisa y asgn

print("Bienvenido a Divertex")
print("**********************")

def limpiar_pantalla(): # Se define este metodo para limpiar la pantalla, para luego presentar una opción
    print("\033[H\033[J")


def ingresar_trm():# Se define metodo para almacenar en un arreglo multidimensional los datos de TRM, Compra y venta.
        try:
            for i in range (n):
                for j in range(3):        
                    valor = float(input("Defina Valor de " + str(asgn[j]) + " para la divisa: "+ str(divisa[i]) + ": "))
                    format(valor, ',')
                    trm[j,i]=np.round(valor, decimals=2)                    
                    df.values[:]=trm
                    print(df)  
                    print()   
        except ValueError: # En caso de ingresar un dato no númerico presenta este aviso
            print("Debe ingresar datos de tipo númerico, deberá ingresar todos los datos nuevamente")

def submenu():



        
while True:#Se elabora un menu para que el usuario pueda ingresar una opción
    
    print("Seleccione una opción: ")    
    print("1. Ajustar TRM")
    print("2. Ver TRM")
    print("3. Comprar divisas: ")
    print("4. Vender divisas: ")
    print("5. Ver ganancias: ")
    print("6. Salir")
    print("")
    
    opcion=input("Digite la opcion que desea: ")#permite al usuario elegir una posiblidad
    if opcion=="1": # Al seleccionar la opcion 1 ejecuta estas instrucciones   
        limpiar_pantalla()     
        print("Elegiste ajustar TRM")
        ingresar_trm()
        
    elif opcion=="2": # Al seleccionar la opcion 2 ejecuta estas instrucciones
        print("Seleccionaste ver TRM")
        limpiar_pantalla()        
        df.values[:]=trm # Se transnfieren los valores del arreglo trm al dataframe df
        print()
        print("Estos son los datos de referencia para hoy "+ fecha_larga)
        print(df)
        print()
        #retorna la lista con la divisa que agrego y guarda pisando la lista anterior con la nueva   
    
    elif opcion=="3": 
        print("Ingrese la divisa que desea comprar")
        
    
    elif opcion=="4":
        print("Ingrese la divisa que desea vender")        
        
    elif opcion=="5":    
        print("Ver ganancias")
        
    elif opcion=="6":
        print("Saliendo del programa...")
        break    
    
    else:
        limpiar_pantalla()
        print("La opcion que selecciono es invalida")
        print("Recuerda que estas son posbilidades:")
