import datetime
import pandas as pd
import numpy as np

def update(file_name):
    datos_pandas = leer_datos(file_name)
    funcion_maximo(datos_pandas)
    funcion_Minimo(datos_pandas)
    
    """
    Inserte aqui las otras funciones.
    
    funcion_Mediana(datos_pandas)
    funcion_Promedio()
    funcion_Desviacion()
    funcion_Varianza()
    """
    datos_graficar = leer_datos(file_name)
    return datos_graficar


def funcion_maximo(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    resultado_max = max(datos)
    
    dato_guardar = [1, date_string, "Maximo", resultado_max]
    guardar(dato_guardar, file_name)


def funcion_minimo(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    resultado_min = min(datos)
    
    dato_guardar = [1, date_string, "Minimo", resultado_min]
    guardar(dato_guardar, file_name)



    

def guardar(data, file_name):    
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(data)

def leer_datos(file_name):
    datos_pandas = pd.read_csv(file_name, index_col=0, parse_dates=True)
    return datos_pandas