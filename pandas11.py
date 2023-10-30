"""
11. Filtra filas de un DataFrame basado en una condición, como mostrar solo las personas
con edades mayores de 25.
"""
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario)

print("Los elementos con edades mayores a 25 son:")
print(df.loc[df['Edad']>25])