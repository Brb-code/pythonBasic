"""
3. Accede a un elemento específico de una Serie por su índice
"""
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario, columns=['Edad'], index=diccionario['Nombre'])

print(f"El elemento con el índice <<Pepe>> es: {df.loc['Pepe']}")