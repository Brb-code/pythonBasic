"""
14. Realiza una operación estadística, como calcular la suma o el promedio, 
en una columna de un DataFrame.
"""
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario)

print(f"De la columna edad, la suma es: {df['Edad'].sum()}, el promedio es: {df['Edad'].mean()}")