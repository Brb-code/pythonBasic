"""
10. Selecciona una columna específica de un DataFrame y muéstrala como una Serie.
"""
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario)

print("Mostrando la columna de nombres")
print(df['Nombre'])