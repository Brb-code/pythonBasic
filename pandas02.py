"""
2. Crea una Serie a partir de un diccionario de edades y nombres, 
donde las edades son los valores y los nombres son los índices.
"""
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}

df = pd.DataFrame(diccionario, columns=['Edad'], index=diccionario['Nombre'])

print("El diccionario se visualiza de la siguiente manera:")
print(diccionario)
print("El dataframe se visualiza de la siguiente manera:")
print(df)