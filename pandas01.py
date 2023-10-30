"""
1. Crea una Serie a partir de una lista de nombres y muéstrala.
"""
import pandas as pd
nombres = ['Pepe','Luisa','Sergio','Wallas','Ada']

df_nombres = pd.DataFrame(nombres)

print("La lista se visualiza de la siguiente manera:")
print(nombres)
print("El dataframe se visualiza de la siguiente manera:")
print(df_nombres)