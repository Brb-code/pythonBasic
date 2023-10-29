"""
4. Escribir un programa que almacene en una lista todo el abecedario. Solicite al usuario
un número entre 2 y 5, elimine de la lista las letras que ocupen posiciones múltiplos del
número ingresado, muestre por pantalla la lista resultante.
"""
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