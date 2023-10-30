"""
13. Ordena un DataFrame en función de los valores de una columna específica.
"""
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario)
print("=======Dataframe original=======")
print(df)
print("===Dataframe ordenado por edad===")
print(df.sort_values(by=['Edad']))
