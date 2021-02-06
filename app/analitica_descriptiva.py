import datetime
import pandas as pd
import numpy as np
import csv

file_name = "data/data_base.csv"

def update(file_name):
    datos_pandas = leer_datos(file_name)
    funcion_maximo(datos_pandas, file_name)
    funcion_Minimo(datos_pandas, file_name)
    funcion_Mediana(datos_pandas, file_name)
    funcion_Promedio(datos_pandas, file_name)
    funcion_Desviacion(datos_pandas, file_name)
    funcion_Varianza(datos_pandas, file_name)
   
    datos_graficar = leer_datos(file_name)
    return datos_graficar


def funcion_maximo(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    resultado_max = max(valor_temperatura)
    
    dato_guardar = [1, date_string, "Maximo", resultado_max]
    guardar(dato_guardar, file_name)


def funcion_minimo(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valores_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    resultado_min = min(valor_temperatura)
    
    dato_guardar = [1, date_string, "Minimo", resultado_min]
    guardar(dato_guardar, file_name)

def funcion_Promedio(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valor_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    resultado_promedio = np.mean(valor_temperatura)
    
    dato_guardar = data = [1, date_string, "Promedio", resultado_promedio]
    guardar(dato_guardar, file_name)

def funcion_Mediana(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valor_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    resultado_mediana = np.median(valor_temperatura)
    
    dato_guardar = data = [1, date_string, "Mediana", resultado_mediana]
    guardar(dato_guardar, file_name)
    

def funcion_Varianza(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valor_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
   
    resultado_varianza = np.var(valor_temperatura)

    dato_guardar = data = [1, date_string, "Varianza", resultado_varianza]
    guardar(dato_guardar, file_name)

def funcion_Desviacion(datos, file_name):
    now = datetime.datetime.now()
    date_string = now.strftime("%d/%m/%y %H:%M:%S")
    valor_temperatura = datos[datos["sensor"] == "Temperatura"]["value"]
    
    resultado_desviacion = np.std(valor_temperatura)
    
    dato_guardar = data = [1, date_string, "Desviacion", resultado_desviacion]
    guardar(dato_guardar, file_name)

    

def guardar(data, file_name):    
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(data)

def leer_datos(file_name):
    datos_pandas = pd.read_csv(file_name, index_col=0, parse_dates=True)
    return datos_pandas