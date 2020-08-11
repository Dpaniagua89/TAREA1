
print (f"Hola , Puede decirme su nombre")
nombre = input()
print (f"Hola {nombre} me alegro de conocerlo") 
mensaje = """
Por favor digita sus valores.
"""

print (mensaje)
valor1 = int(input("ingresa el primer valor: "))
valor2 = int(input("ingresa el primer valor: "))

if valor1 > valor2: 
    print (f"el numero {valor1} es mayor que el numero {valor2}")
elif valor1 < valor2:
    print (f"el numero {valor2} es mayor que el numero {valor1}")
else:
    print (f"los valores son iguales")
