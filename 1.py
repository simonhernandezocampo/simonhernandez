num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
"""num1 = 4
num2 = 2"""
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
metros = float(input("Ingrese la cantidad en metros: "))

centimetros = metros * 100
kilometros = metros / 1000

print(metros, "metros equivalen a:")
print(centimetros, "centímetros")
print(kilometros, "kilómetros")

precio_original = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))

descuento_cantidad = precio_original * (descuento / 100)
precio_final = precio_original - descuento_cantidad

print("El descuento es de:", descuento_cantidad)
print("El precio final es:", precio_final)

calificacion1 = float(input("Ingrese la primera calificación: "))
calificacion2 = float(input("Ingrese la segunda calificación: "))
calificacion3 = float(input("Ingrese la tercera calificación: "))

promedio = (calificacion1 + calificacion2 + calificacion3) / 3

if promedio >= 5:
    print("Aprobaste con un promedio de:", promedio)
else:
    print("Reprobaste con un promedio de:", promedio)

resultado1 = (((2 + (3 * 4)) > 10) and ((5 ** 2) == 25)) or (not False)
print(resultado1)

#resultado1 = 2 + 3 * 4 > 10 and 5 ** 2 == 25 or not


#Ejercico2
resultado2 = ((10 + (5 * 2)) > 15) and ((30 / 3) == 10) or (not ((2 ** 3) != 8))
print(resultado2)







