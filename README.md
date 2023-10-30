# Ejercicios en Python

**_Elaborado por:_** Israel Jose Huallpara Mencias
**_Código fuente en:_** ()[]

## Práctica Pandas

1. Crea una Serie a partir de una lista de nombres y muéstrala.

```python
import pandas as pd
nombres = ['Pepe','Luisa','Sergio','Wallas','Ada']

df_nombres = pd.DataFrame(nombres)

print("La lista se visualiza de la siguiente manera:")
print(nombres)
print("El dataframe se visualiza de la siguiente manera:")
print(df_nombres)
```

[Código fuente](pandas01.py)

```bash
# DEMO
La lista se visualiza de la siguiente manera:
['Pepe', 'Luisa', 'Sergio', 'Wallas', 'Ada']
El dataframe se visualiza de la siguiente manera:
        0
0    Pepe
1   Luisa
2  Sergio
3  Wallas
4     Ada
```
2. Crea una Serie a partir de un diccionario de edades y nombres, 
donde las edades son los valores y los nombres son los índices.

```python
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}

df = pd.DataFrame(diccionario, columns=['Edad'], index=diccionario['Nombre'])

print("El diccionario se visualiza de la siguiente manera:")
print(diccionario)
print("El dataframe se visualiza de la siguiente manera:")
print(df)
```

[Código fuente](pandas02.py)

```bash
# DEMO
El diccionario se visualiza de la siguiente manera:
{'Nombre': ['Pepe', 'Luisa', 'Sergio', 'Wallas', 'Ada'], 'Edad': [12, 30, 23, 48, 33]}
El dataframe se visualiza de la siguiente manera:
        Edad
Pepe      12
Luisa     30
Sergio    23
Wallas    48
Ada       33
```
3. Accede a un elemento específico de una Serie por su índice
```python
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario, columns=['Edad'], index=diccionario['Nombre'])

print(f"El elemento con el índice <<Pepe>> es: {df.loc['Pepe']}")
```

[Código fuente](pandas03.py)

```bash
# DEMO
El elemento con el índice <<Pepe>> es: Edad    12
Name: Pepe, dtype: int64
```

4. Filtra elementos en una Serie que cumplan con una condición específica, como edades
mayores de 30.
```python
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario, columns=['Edad'], index=diccionario['Nombre'])

print("Los elementos con edades mayores a 30 son:")
print(df.loc[df['Edad']>30])
```

[Código fuente](pandas04.py)

```bash
# DEMO
Los elementos con edades mayores a 30 son:
        Edad
Wallas    48
Ada       33
```

5. Realiza una operación matemática en cada elemento de una Serie, como duplicar todas
las edades.
```python
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario, columns=['Edad'], index=diccionario['Nombre'])

print("El dataframe inicial es:")
print(df)

df['Edad'] = df['Edad'] * 2
print("El dataframe con edades duplicadas es:")
print(df)
```

[Código fuente](pandas05.py)

```bash
# DEMO
El dataframe inicial es:
        Edad
Pepe      12
Luisa     30
Sergio    23
Wallas    48
Ada       33
El dataframe con edades duplicadas es:
        Edad
Pepe      24
Luisa     60
Sergio    46
Wallas    96
Ada       66
```

6. Encuentra la edad más alta y la edad más baja.
```python
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario, columns=['Edad'], index=diccionario['Nombre'])

print(f'La mayor edad es: {df.max().max()}, la menor edad es: {df.min().min()}')
```

[Código fuente](pandas06.py)

```bash
# DEMO
La mayor edad es: 48, la menor edad es: 12
```

7. Calcula la media y la mediana de las edades

```python
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario, columns=['Edad'], index=diccionario['Nombre'])

print(f'La media de edad es: {df.mean().mean()}, la mediana de edad es: {df.median().median()}')
```

[Código fuente](pandas07.py)

```bash
# DEMO
La media de edad es: 29.2, la mediana de edad es: 30.0
```

8. Concatena dos Series en una sola Serie más grande.
```python
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
```

[Código fuente](pandas08.py)

```bash
# DEMO
======================Serie 1======================
        Edad
Pepe      12
Luisa     30
Sergio    23
Wallas    48
Ada       33
======================Serie 2======================
           Genero
Pepe    Masculino
Luisa    Femenino
Sergio  Masculino
Wallas  Masculino
Ada      Femenino
Manuel  Masculino
===================Series unidas===================
        Edad     Genero
Pepe      12  Masculino
Luisa     30   Femenino
Sergio    23  Masculino
Wallas    48  Masculino
Ada       33   Femenino
```

9. Crea un DataFrame a partir de un diccionario de datos y muestra las primeras filas
```python
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario)

print("Mostrando las primeras 3 filas del DataFrame")
print(df.head(n=3))
```

[Código fuente](pandas09.py)

```bash
# DEMO
Mostrando las primeras 3 filas del DataFrame
   Nombre  Edad
0    Pepe    12
1   Luisa    30
2  Sergio    23
```

10. Selecciona una columna específica de un DataFrame y muéstrala como una Serie.
```python
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario)

print("Mostrando la columna de nombres")
print(df['Nombre'])
```

[Código fuente](pandas10.py)

```bash
# DEMO
Mostrando la columna de nombres
0      Pepe
1     Luisa
2    Sergio
3    Wallas
4       Ada
Name: Nombre, dtype: object
```

11. Filtra filas de un DataFrame basado en una condición, como mostrar solo las personas con edades mayores de 25.
```python
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario)

print("Los elementos con edades mayores a 25 son:")
print(df.loc[df['Edad']>25])
```

[Código fuente](pandas11.py)

```bash
# DEMO
Los elementos con edades mayores a 25 son:
   Nombre  Edad
1   Luisa    30
3  Wallas    48
4     Ada    33
```

12. Agrega una nueva columna al DataFrame que sea el resultado de una operación entre dos columnas existentes.
```python
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario)
df['Nivel'] = ["Senior" if x > 25 else "Junior" for x in df['Edad']]
print("El resultado al agregar la columna Nivel es:")
print(df)
```

[Código fuente](pandas12.py)

```bash
# DEMO
El resultado al agregar la columna Nivel es:
   Nombre  Edad   Nivel
0    Pepe    12  Junior
1   Luisa    30  Senior
2  Sergio    23  Junior
3  Wallas    48  Senior
4     Ada    33  Senior
```

13. Ordena un DataFrame en función de los valores de una columna específica.
```python
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario)
print("=======Dataframe original=======")
print(df)
print("===Dataframe ordenado por edad===")
print(df.sort_values(by=['Edad']))
```

[Código fuente](pandas13.py)

```bash
# DEMO
=======Dataframe original=======
   Nombre  Edad
0    Pepe    12
1   Luisa    30
2  Sergio    23
3  Wallas    48
4     Ada    33
===Dataframe ordenado por edad===
   Nombre  Edad
0    Pepe    12
2  Sergio    23
1   Luisa    30
4     Ada    33
3  Wallas    48
```

14. Realiza una operación estadística, como calcular la suma o el promedio, 
en una columna de un DataFrame.
```python
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio','Wallas','Ada'],'Edad':[12,30,23,48,33]}
df = pd.DataFrame(diccionario)

print(f"De la columna edad, la suma es: {df['Edad'].sum()}, el promedio es: {df['Edad'].mean()}")
```

[Código fuente](pandas14.py)

```bash
# DEMO
De la columna edad, la suma es: 146, el promedio es: 29.2
```

15. Elimina filas o columnas con datos faltantes en un DataFrame.
```python
import pandas as pd
diccionario = {'Nombre':['Pepe','Luisa','Sergio',None,'Ada','Manuel'],'Edad':[12,None,23,48,33,None]}
df = pd.DataFrame(diccionario)
print("Dataframe inicial:")
print(df)

print("Dataframe sin valores vacios en la columna Edad:")
print(df[df['Edad'].notna()])

print("Dataframe sin valores vacios en totalidad:")
print(df.dropna())
```

[Código fuente](pandas15.py)

```bash
# DEMO
Dataframe inicial:
   Nombre  Edad
0    Pepe  12.0
1   Luisa   NaN
2  Sergio  23.0
3    None  48.0
4     Ada  33.0
5  Manuel   NaN
Dataframe sin valores vacios en la columna Edad:
   Nombre  Edad
0    Pepe  12.0
2  Sergio  23.0
3    None  48.0
4     Ada  33.0
Dataframe sin valores vacios en totalidad:
   Nombre  Edad
0    Pepe  12.0
2  Sergio  23.0
4     Ada  33.0
```