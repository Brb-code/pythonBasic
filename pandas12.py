"""
12. Agrega una nueva columna al DataFrame que sea el resultado de una operación entre
dos columnas existentes.
"""
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario)
df['Nivel'] = ["Senior" if x > 25 else "Junior" for x in df['Edad']]
print("El resultado al agregar la columna Nivel es:")
print(df)
