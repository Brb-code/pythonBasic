"""
7. Calcula la media y la mediana de las edades
"""
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario, columns=['Edad'], index=diccionario['Nombre'])

print(f'La media de edad es: {df.mean().mean()}, la mediana de edad es: {df.median().median()}')