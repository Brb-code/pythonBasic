"""
5. Escribe una función que solicite al usuario el ingreso de 8 materias con sus respectivas
notas entre 1 y 100, almacena los datos en un diccionario. Imprime en pantalla todas las
materias en las que se tenga una nota de aprobación, imprime las materias con nota de
reprobación, imprime las notas más alta y más baja, imprime el promedio general del
estudiante, imprime el promedio de las materias aprobadas, finalmente imprime el
promedio de las materias reprobadas.
"""
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
