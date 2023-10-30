"""
15. Elimina filas o columnas con datos faltantes en un DataFrame.
"""
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio',None,'Ada','Manuel'],'Edad':[12,None,23,48,33,None]}
df = pd.DataFrame(diccionario)
print("Dataframe inicial:")
print(df)

print("Dataframe sin valores vacios en la columna Edad:")
print(df[df['Edad'].notna()])

print("Dataframe sin valores vacios en totalidad:")
print(df.dropna())