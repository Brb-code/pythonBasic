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
"""
2. Solicita al usuario que ingrese frutas que se vayan almacenando en una lista, el ciclo
termina cuando se ingresa el valor cero. Al finalizar el ciclo muestra un resumen de la
cantidad de frutas ingresadas, cuantas frutas tienen una longitud par de letras, cuantas
tienen una longitud impar de letras, imprime todas las frutas cuya longitud esté entre 5
y 8, imprime la fruta con la longitud más larga, imprime la fruta con la longitud más
corta.
"""
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
