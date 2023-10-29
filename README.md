# Ejercicios en Python

**_Elaborado por:_** Israel Jose Huallpara Mencias
**_Código fuente:_** [https://github.com/Brb-code/pythonBasic](https://github.com/Brb-code/pythonBasic)

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

6. Crea un diccionario cuya clave sea un número de carnet de identidad y cuyo valor sea
una lista que almacene: nombre, salario y departamento en que trabaja. Llena el
diccionario con 15 registros. Imprime el empleado de salario más alto, el empleado de
salario más bajo, imprime el promedio de salarios, pide al usuario un número de carnet
y revisa si existe en el diccionario, si existe muestra los datos de ese empleado.

```python
# Diccionario de  empleados
empleados = {
    12345: ['Juan Perez', 5000, 'Ventas'],
    23456: ['María Rodriguez', 3000, 'Finanzas'],
    34567: ['Carlos Gomez', 2500, 'RRHH'],
    45678: ['Mario Ortiz', 2500, 'RRHH'],
    56789: ['Laura Saenz', 4000, 'Sistemas'],
    67890: ['Mike Solivan', 2000, 'Seguridad'],
    78901: ['Lupe Carrasco', 3500, 'Legal'],
    89012: ['Susana Quinteros', 5000, 'Ventas'],
    90123: ['Patricio Estrella', 5500, 'Gerencia'],
    11234: ['Lina Torres', 4000, 'Ventas'],
    12234: ['Luis Sanchez', 2000, 'Seguridad'],
    12223: ['Luordes Carrillo', 4000, 'Atención al cliente'],
    12222: ['Liz Lopez', 5000, 'Ventas'],
    13123: ['Lu Ortiz', 4000, 'RRHH'],
    13312: ['Mauricio Mendez', 3000, 'Legal'],    
}

salario_alto = max(empleados.items(), key=lambda x: x[1][1])
print(f'El empleado con salario más alto es: {salario_alto[1][0]}')

salario_bajo = min(empleados.items(), key=lambda x: x[1][1])
print(f'El empleado con salario más bajo es: {salario_bajo[1][0]}')

salarios = [empleado[1] for empleado in empleados.values()]
print(f"El promedio de salarios es: {sum(salarios)/len(salarios)}")

nro_ci = int(input("Ingrese el número de carnet a buscar: "))

if nro_ci in empleados:
    datos_empleado = empleados[nro_ci]
    print(f"Los datos del empleado buscado son: número de carnet {nro_ci}: Nombre: {datos_empleado[0]}, Salario: {datos_empleado[1]}, Departamento: {datos_empleado[2]}")
else:
    print(f"No se encontró información para el número de carnet {nro_ci}")
```

[Código fuente](practica06.py)

```bash
# DEMO
El empleado con salario más alto es: Patricio Estrella
El empleado con salario más bajo es: Mike Solivan
El promedio de salarios es: 3666.6666666666665
Ingrese el número de carnet a buscar: 122222
No se encontró información para el número de carnet 122222

#DEMO
El empleado con salario más alto es: Patricio Estrella
El empleado con salario más bajo es: Mike Solivan
El promedio de salarios es: 3666.6666666666665
Ingrese el número de carnet a buscar: 12222
Los datos del empleado buscado son: número de carnet 12222: Nombre: Liz Lopez, Salario: 5000, Departamento: Ventas
```

7. Mediante el uso de un diccionario, escribe el código de un programa que implemente
una agenda. En la agenda se podrán guardar nombres y números de teléfono. El
programa nos dará el siguiente menú:
- Añadir/modificar: Se debe introducir el nombre y el teléfono que será añadido al
diccionario si no existe, y si existe deberá actualizar el teléfono al nuevo valor.
- Buscar: Nos pide el nombre, y muestra el número de teléfono de esa persona si es
que lo encuentra, sino lo encuentra muestra el mensaje adcuado.
- Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la
agenda.
- Listar: Nos muestra todos los contactos de la agenda

```python
agenda = {}

def agregar_modificar():
    nombre = input("Ingrese el nombre de su contacto: ")
    telefono = input("Ingrese el número de teléfono de su contacto: ")
    agenda[nombre] = telefono
    print(f"El contacto {nombre} fue agregado/modificado con éxito.")

def buscar():
    nombre = input("Ingrese el nombre a buscar: ")
    if nombre in agenda:
        print(f"El número de teléfono de {nombre} es: {agenda[nombre]}")
    else:
        print(f"{nombre} no se encuentra en la agenda.")

def borrar():
    nombre = input("Ingrese el nombre del contacto a borrar: ")
    if nombre in agenda:
        confirmacion = input(f"¿Está seguro de que desea borrar a {nombre} de la agenda? (s/n): ")
        if confirmacion.lower() == 's':
            del agenda[nombre]
            print(f"{nombre} fue eliminado con éxito.")
    else:
        print(f"{nombre} no se encuentra en la agenda.")

def listar():
    print("Contactos en la agenda:")
    for nombre, telefono in agenda.items():
        print(f"{nombre}: {telefono}")

while True:
    print("\nMi agenda:\nMenú")
    print("1. Añadir/Modificar")
    print("2. Buscar")
    print("3. Borrar")
    print("4. Listar")
    print("5. Salir")

    opcion = input("Seleccione una opción (1-5): ")

    if opcion == '1':
        agregar_modificar()
    elif opcion == '2':
        buscar()
    elif opcion == '3':
        borrar()
    elif opcion == '4':
        listar()
    elif opcion == '5':
        print("Gracias, vuelvo pronto....")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
```

[Código fuente](practica07.py)

```bash
# DEMO
Mi agenda:
Menú
1. Añadir/Modificar
2. Buscar
3. Borrar
4. Listar
5. Salir
Seleccione una opción (1-5): 2
Ingrese el nombre a buscar: pepe
pepe no se encuentra en la agenda.

Mi agenda:
Menú
1. Añadir/Modificar
2. Buscar
3. Borrar
4. Listar
5. Salir
Seleccione una opción (1-5): 1
Ingrese el nombre de su contacto: pepe
Ingrese el número de teléfono de su contacto: 123123
El contacto pepe fue agregado/modificado con éxito.

Mi agenda:
Menú
1. Añadir/Modificar
2. Buscar
3. Borrar
4. Listar
5. Salir
Seleccione una opción (1-5): 4
Contactos en la agenda:
pepe: 123123

Mi agenda:
Menú
1. Añadir/Modificar
2. Buscar
3. Borrar
4. Listar
5. Salir
Seleccione una opción (1-5): 3
Ingrese el nombre del contacto a borrar: pepe
¿Está seguro de que desea borrar a pepe de la agenda? (s/n): s
pepe fue eliminado con éxito.

Mi agenda:
Menú
1. Añadir/Modificar
2. Buscar
3. Borrar
4. Listar
5. Salir
Seleccione una opción (1-5): 4
Contactos en la agenda:

Mi agenda:
Menú
1. Añadir/Modificar
2. Buscar
3. Borrar
4. Listar
5. Salir
Seleccione una opción (1-5): 6
Opción no válida. Intente nuevamente.

Mi agenda:
Menú
1. Añadir/Modificar
2. Buscar
3. Borrar
4. Listar
5. Salir
Seleccione una opción (1-5): 5
Gracias, vuelvo pronto....
```
