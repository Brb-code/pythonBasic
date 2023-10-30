"""
5. Realiza una operación matemática en cada elemento de una Serie, como duplicar todas
las edades.
"""
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario, columns=['Edad'], index=diccionario['Nombre'])

print("El dataframe inicial es:")
print(df)

df['Edad'] = df['Edad'] * 2
print("El dataframe con edades duplicadas es:")
print(df)
