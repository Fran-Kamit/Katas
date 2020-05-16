'''
Escribir un programa para una empresa que tiene salas de juegos para todas las
edades y quiere calcular de forma automática el precio que debe cobrar a sus
clientes por entrar. El programa debe preguntar a usuario la edad del clientes
y mostrar el precio de la entrada. Si el cliente es menor de 4 aos puede
entrar gratis, si tiene entre 4 y 18 debe pagar 5€ y si es mayor de 18 aos, 10€.
'''

edad = input('Introduce tu edad: ')
edad = int(edad)

if edad < 4:
    print('El precio de la entrada es 0€.')
elif edad >= 4 and edad <= 18: #4<= edad <=18:
    print('El precio de la entrada es 5€.')
else:
    print('El precio de la entrada es 10€.')