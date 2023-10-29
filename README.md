# Ejercicios en Python

**_Elaborado por:_** Israel Jose Huallpara Mencias

## Práctica Python

1. Genera un ciclo while donde el usuario ingrese números que se almacenen en una lista, el ciclo termina cuando se ingresa el valor cero. Al finalizar el ciclo muestra un resumen con la siguiente información: cantidad de números ingresados, cantidad de números pares, cantidad de números impares, sumatoria de los números pares, sumatoria de los números impares, el número máximo, el número mínimo, impresión según el orden en que se ingresaron los números, impresión en sentido opuesto al orden ingresado.

```python
nro = -1
nros = []

while nro != 0:
    nro = int(input("Ingrese un número, si registra el valor 0, el registro de numeros concluirá: "))
    if nro != 0:
        nros.append(nro)
print(f'Se ingresaron {len(nros)} números.')
print(f'Se ingresaron {len([x for x in nros if x % 2 == 0])} números pares.')
print(f'Se ingresaron {len([x for x in nros if x % 2 != 0])} números impares.')
print(f'La sumatoria de los números pares es: {sum([x for x in nros if x % 2 == 0])}')
print(f'La sumatoria de los números impares es: {sum([x for x in nros if x % 2 != 0])}')
print(f'El número máximo es: {max(nros)} y el mínimo es: {min(nros)}')
print('Se introdujeron los números en el siguiente orden:')
print(nros)
print('La impresión de manera opuesta es: ')
nros.reverse()
print(nros)
```

[Código fuente](practica01.py)

```bash
# DEMO
Ingrese un número, si registra el valor 0, el registro de numeros concluirá: 1
Ingrese un número, si registra el valor 0, el registro de numeros concluirá: 2
Ingrese un número, si registra el valor 0, el registro de numeros concluirá: 3
Ingrese un número, si registra el valor 0, el registro de numeros concluirá: 4
Ingrese un número, si registra el valor 0, el registro de numeros concluirá: 5
Ingrese un número, si registra el valor 0, el registro de numeros concluirá: 0
Se ingresaron 5 números.
Se ingresaron 2 números pares.
Se ingresaron 3 números impares.
La sumatoria de los números pares es: 6
La sumatoria de los números impares es: 9
El número máximo es: 5 y el mínimo es: 1
Se introdujeron los números en el siguiente orden:
[1, 2, 3, 4, 5]
La impresión de manera opuesta es:
[5, 4, 3, 2, 1]
```

2. Solicita al usuario que ingrese frutas que se vayan almacenando en una lista, el ciclo termina cuando se ingresa el valor cero. Al finalizar el ciclo muestra un resumen de la cantidad de frutas ingresadas, cuantas frutas tienen una longitud par de letras, cuantas tienen una longitud impar de letras, imprime todas las frutas cuya longitud esté entre 5 y 8, imprime la fruta con la longitud más larga, imprime la fruta con la longitud más
   corta.

```python
fruta = ""
frutas = []

while fruta != '0':
    fruta = input("Ingrese una fruta, si registra el valor 0 el registro de frutas concluirá: ")
    if fruta != '0':
        frutas.append(fruta)
print(f'Se ingresaron {len(frutas)} frutas.')
print(f'Se ingresaron {len([x for x in frutas if len(x) % 2 == 0])} frutas con cantidad de letras pares.')
print(f'Se ingresaron {len([x for x in frutas if len(x) % 2 != 0])} frutas con cantidad de letras impares.')
print('Las frutas con longitud entre 5 y 8 son: ')
print([x for x in frutas if len(x) >= 5 and len(x) <= 8])
print('La(s) fruta(s) con longitud máxima es: ')
print([x for x in frutas if len(x) == max([len(x) for x in frutas])])
print('La(s) fruta(s) con longitud mínima es: ')
print([x for x in frutas if len(x) == min([len(x) for x in frutas])])
```

[Código fuente](practica02.py)

```bash
# DEMO
Ingrese una fruta, si registra el valor 0 el registro de frutas concluirá: Manzana
Ingrese una fruta, si registra el valor 0 el registro de frutas concluirá: Pera
Ingrese una fruta, si registra el valor 0 el registro de frutas concluirá: Uva
Ingrese una fruta, si registra el valor 0 el registro de frutas concluirá: Peramota
Ingrese una fruta, si registra el valor 0 el registro de frutas concluirá: 0
Se ingresaron 4 frutas.
Se ingresaron 2 frutas con cantidad de letras pares.
Se ingresaron 2 frutas con cantidad de letras impares.
Las frutas con longitud entre 5 y 8 son:
['Manzana', 'Peramota']
La(s) fruta(s) con longitud máxima es:
['Peramota']
La(s) fruta(s) con longitud mínima es:
['Uva']
```


3. Solicita números al usuario y que se almacenen en una lista, el ciclo termina cuando se
ingresa el valor cero. Recorre la lista y copia en otra lista sólo los números primos.
Imprime la lista original y la lista de números primos.

```python
# Función para identificar si un numero es primo o no
def primo(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True

nro = -1
nros = []

while nro != 0:
    nro = int(input("Ingrese un número, si registra el valor 0, el registro de numeros concluirá: "))
    if nro != 0:
        nros.append(nro)
primos = [x for x in nros if primo(x)]
print("La lista orginal es: ")
print(nros)
print("De la lista, los números primos son: ")
print(primos)
```

[Código fuente](practica03.py)

```bash
# DEMO
Ingrese un número, si registra el valor 0, el registro de numeros concluirá: 2
Ingrese un número, si registra el valor 0, el registro de numeros concluirá: 3
Ingrese un número, si registra el valor 0, el registro de numeros concluirá: 4
Ingrese un número, si registra el valor 0, el registro de numeros concluirá: 5
Ingrese un número, si registra el valor 0, el registro de numeros concluirá: 6
Ingrese un número, si registra el valor 0, el registro de numeros concluirá: 0
La lista orginal es: 
[2, 3, 4, 5, 6]
De la lista, los números primos son: 
[2, 3, 5]
```

4. Escribir un programa que almacene en una lista todo el abecedario. Solicite al usuario
un número entre 2 y 5, elimine de la lista las letras que ocupen posiciones múltiplos del
número ingresado, muestre por pantalla la lista resultante.

```python
abc = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
nro = int(input("Ingrese un numero entre 2 y 5: "))
new_abc = []
i = 1
if nro >= 2 and nro <= 5:
    for (ind, el) in enumerate(abc):
        if nro * i == ind:
            i += 1
        else:
            new_abc.append(el)         
    print("La lista resultante es: ")
    print(new_abc)
else:
    print(f'El numero ingresado {nro} no ingresa en el rango solicitado')
```

[Código fuente](practica04.py)

```bash
# Considerar que la posición de la lista inicia en 0
# DEMO
Ingrese un numero entre 2 y 5: 3
La lista resultante es: 
['A', 'B', 'C', 'E', 'F', 'H', 'I', 'K', 'L', 'N', 'Ñ', 'P', 'Q', 'S', 'T', 'V', 'W', 'Y', 'Z']

#DEMO
Ingrese un numero entre 2 y 5: 9
El numero ingresado 9 no ingresa en el rango solicitado
```

5. Escribe una función que solicite al usuario el ingreso de 8 materias con sus respectivas
notas entre 1 y 100, almacena los datos en un diccionario. Imprime en pantalla todas las
materias en las que se tenga una nota de aprobación, imprime las materias con nota de
reprobación, imprime las notas más alta y más baja, imprime el promedio general del
estudiante, imprime el promedio de las materias aprobadas, finalmente imprime el
promedio de las materias reprobadas.

```python
datos = {}
def cargar_datos():
    materia = input("Ingrese el nombre de la materia: ")
    nro = -1
    while nro<1 or nro >100:
        nro = int(input(f'Ingrese la nota de la materia {materia} (Esta debe estar entre 1 y 100 necesariamente):'))
    datos[materia] = nro

print("Ingrese 8 materias:")
for i in range(0,8):
    cargar_datos()
print("Materias aprobadas")
print([k for k,v in datos.items() if v>50])

print("Materias reprobadas")
print([k for k,v in datos.items() if v<51])

print(f'La nota más alta es: {max([v for v in datos.values()])} y la nota más baja es: {min([v for v in datos.values()])}')
print(f'El promedio general es: {sum([v for v in datos.values()])/len(datos)}')
print(f'El promedio de las notas de aprobación es: {sum([v for k,v in datos.items() if v>50])/len([v for k,v in datos.items() if v>50])}')
print(f'El promedio de las notas de reprobación es: {sum([v for k,v in datos.items() if v<51])/len([v for k,v in datos.items() if v<51])}')

```

[Código fuente](practica05.py)

```bash
# DEMO
Ingrese 8 materias:
Ingrese el nombre de la materia: BD
Ingrese la nota de la materia BD (Esta debe estar entre 1 y 100 necesariamente):0
Ingrese la nota de la materia BD (Esta debe estar entre 1 y 100 necesariamente):53
Ingrese el nombre de la materia: PROGRA
Ingrese la nota de la materia PROGRA (Esta debe estar entre 1 y 100 necesariamente):22
Ingrese el nombre de la materia: ANALISIS
Ingrese la nota de la materia ANALISIS (Esta debe estar entre 1 y 100 necesariamente):85
Ingrese el nombre de la materia: TEORIA
Ingrese la nota de la materia TEORIA (Esta debe estar entre 1 y 100 necesariamente):33
Ingrese el nombre de la materia: FISICA
Ingrese la nota de la materia FISICA (Esta debe estar entre 1 y 100 necesariamente):99
Ingrese el nombre de la materia: MATE
Ingrese la nota de la materia MATE (Esta debe estar entre 1 y 100 necesariamente):83
Ingrese el nombre de la materia: HISTORIA
Ingrese la nota de la materia HISTORIA (Esta debe estar entre 1 y 100 necesariamente):43
Ingrese el nombre de la materia: DEV
Ingrese la nota de la materia DEV (Esta debe estar entre 1 y 100 necesariamente):78
Materias aprobadas
['BD', 'ANALISIS', 'FISICA', 'MATE', 'DEV']
Materias reprobadas
['PROGRA', 'TEORIA', 'HISTORIA']
La nota más alta es: 99 y la nota más baja es: 22
El promedio general es: 62.0
El promedio de las notas de aprobación es: 79.6
El promedio de las notas de reprobación es: 32.666666666666664
```

