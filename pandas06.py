"""
6. Encuentra la edad más alta y la edad más baja.
"""
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario, columns=['Edad'], index=diccionario['Nombre'])

print(f'La mayor edad es: {df.max().max()}, la menor edad es: {df.min().min()}')