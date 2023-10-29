"""
6. Crea un diccionario cuya clave sea un número de carnet de identidad y cuyo valor sea
una lista que almacene: nombre, salario y departamento en que trabaja. Llena el
diccionario con 15 registros. Imprime el empleado de salario más alto, el empleado de
salario más bajo, imprime el promedio de salarios, pide al usuario un número de carnet
y revisa si existe en el diccionario, si existe muestra los datos de ese empleado.
"""
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
