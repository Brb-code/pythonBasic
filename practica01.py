"""
1. Genera un ciclo while donde el usuario ingrese números que se almacenen en una lista,
el ciclo termina cuando se ingresa el valor cero. Al finalizar el ciclo muestra un resumen
con la siguiente información: cantidad de números ingresados, cantidad de números
pares, cantidad de números impares, sumatoria de los números pares, sumatoria de los
números impares, el número máximo, el número mínimo, impresión según el orden en
que se ingresaron los números, impresión en sentido opuesto al orden ingresado.
"""
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