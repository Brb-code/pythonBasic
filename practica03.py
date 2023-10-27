"""
3. Solicita números al usuario y que se almacenen en una lista, el ciclo termina cuando se
ingresa el valor cero. Recorre la lista y copia en otra lista sólo los números primos.
Imprime la lista original y la lista de números primos.
"""
# Función para identificar si un numero es primo o no
def primo(n):
    for i in range(2, n-1):
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