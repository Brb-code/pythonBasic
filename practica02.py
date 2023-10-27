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