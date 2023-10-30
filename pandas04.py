"""
4. Filtra elementos en una Serie que cumplan con una condición específica, como edades
mayores de 30.
"""
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario, columns=['Edad'], index=diccionario['Nombre'])

print("Los elementos con edades mayores a 30 son:")
print(df.loc[df['Edad']>30])