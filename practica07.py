"""
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
"""
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
