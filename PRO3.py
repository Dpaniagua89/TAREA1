#   Desarrolle un programa en python que permita leer tres valores. El programa debe imprimir cual es el mayor y cual es el
#   menor. Recuerde constatar que los tres valores introducidos por el teclado sean valores distintos. Presente un mensaje de
#   alerta en caso de que se detecte la introducción de valores iguales.

def valor_mayor(valor1, valor2, valor3):
    if valor1 == valor2:
        print(f"error, valor1 y valor2 iguales")
    elif valor2 == valor3:
        print(f"error, valor2 y valor3 iguales")
    elif valor3 == valor1: 
        print(f"error, valor3 y valor1 iguales")
    elif valor1 > valor2 and valor1 > valor3:
        print (f"el primer digito ({valor1}) es mayor")
    elif valor2 > valor1 and  valor2  > valor3:
        print (f"el segundo digito ({valor2}) es mayor")
    elif valor3 > valor1 and  valor3  > valor2:
        print (f"el tercer digito ({valor3}) es mayor")

def valor_menor(valor1, valor2, valor3):
    if valor1 == valor2:
        print(f"error, valor1 y valor2 iguales")
    elif valor2 == valor3:
        print(f"error, valor2 y valor3 iguales")
    elif valor3 == valor1: 
        print(f"error, valor3 y valor1 iguales")
    elif valor1 < valor2 and valor1 < valor3:
        print (f"el primer digito ({valor1}) es menor")
    elif valor2 < valor1 and  valor2  < valor3:
        print (f"el segundo digito ({valor2}) es menor")
    elif valor3 < valor1 and  valor3  < valor2:
        print (f"el tercer digito ({valor3}) es menor")


valor1 = int(input(f"ingrese su primer digito: "))
valor2 = int(input(f"ingrese su segundo digito: ")) 
valor3 = int(input(f"ingrese su tercer digito: ")) 

resultado1  = valor_mayor(valor1, valor2, valor3)
resultado2  = valor_menor(valor1, valor2, valor3)