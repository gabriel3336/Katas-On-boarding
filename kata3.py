asteroide=input("insterte el tamanio del asteroide")

int(asteroide)



if int(asteroide) > 25:
    print("peligro")
else:
    print("todo en orden")

#ej 2

asteroides = 19
if asteroides > 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
elif asteroides == 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
else:
    print('¡Nada que ver aquí!')

#ej3

velocidad_asteroide = 25
tamano_asteroide = 40
if velocidad_asteroide > 25 and tamano_asteroide > 25:
    print('¡Alerta, Un asteroide muy peligroso viene hacia la Tierra!')
elif velocidad_asteroide >= 20:
    print('Look up! ¡Hay una luz mágica en el cielo!')
elif tamano_asteroide < 25:
    print('Nada que ver aquí :)')
else:
    print('Nada que ver aquí :)')