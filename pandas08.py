"""
8. Concatena dos Series en una sola Serie más grande.
"""
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df1 = pd.DataFrame(diccionario, columns=['Edad'], index=diccionario['Nombre'])
diccionario2 = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada','Manuel'],'Genero':['Masculino','Femenino','Masculino','Masculino','Femenino','Masculino']}
df2 = pd.DataFrame(diccionario2, columns=['Genero'], index=diccionario2['Nombre'])

print("======================Serie 1======================")
print(df1)
print("======================Serie 2======================")
print(df2)
dfU = pd.merge(df1, df2,right_index=True, left_index=True)
print("===================Series unidas===================")
print(dfU)