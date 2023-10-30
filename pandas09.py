"""
9. Crea un DataFrame a partir de un diccionario de datos y muestra las primeras filas
"""
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario)

print("Mostrando las primeras 3 filas del DataFrame")
print(df.head(n=3))