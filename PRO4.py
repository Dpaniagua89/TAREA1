#   Desarrolle un programa en python que lea cuatro números diferentes y a continuación imprima el mayor de los cuatro
#   números introducidos y también el menor de ellos.

def NUMERO_MAYOR(valor1, valor2, valor3, valor4):
    if valor1 > valor2 and valor1 > valor3 and valor1 > valor4:
        print (f"El primer digito ({valor1}) es mayor")
    elif valor2 > valor1 and valor2 > valor3 and valor2 > valor4:
        print (f"El segundo digito ({valor2}) es mayor")
    elif valor3 > valor1 and valor3 > valor2 and valor3 > valor4:
        print (f"El tercer digito ({valor3}) es mayor")
    else:
        print (f"El cuarto digito ({valor4}) es mayor")

def NUMERO_MENOR(valor1, valor2, valor3, valor4): 
    if valor1 < valor2 or valor1 < valor3 or valor1 < valor4:
        print (f"El primer digito ({valor1}) es menor")
    elif valor2 < valor1 or valor2 < valor3 or valor2 < valor4:
        print (f"El segundo digito ({valor2}) es menor")
    elif valor3 < valor1 or valor3 < valor2 or valor3 < valor4:
        print (f"El tercer digito ({valor3}) es menor")
    else:
        print (f"El cuarto digito ({valor4}) es menor")

valor1 = int(input(f"ingrese su primer digito: "))
valor2 = int(input(f"ingrese su segundo digito: "))
valor3 = int(input(f"ingrese su tercer digito: "))
valor4 = int(input(f"ingrese su cuarto digito: "))

resultado   = NUMERO_MAYOR(valor1, valor2, valor3, valor4)
resultado2  = NUMERO_MENOR(valor1, valor2, valor3, valor4)




