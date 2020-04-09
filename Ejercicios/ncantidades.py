numero = 1
cantnume = 0
cantnumeronega = 0

while numero != 0:

    numero = float(input('digite un numero\n'))

    if numero > 0:
      	cantnume = cantnume + 1
    elif numero < 0:
        cantnumeronega = cantnumeronega + 1
else:      
      print('La cantidad de numeros myores a cero son:', cantnume)
      print('La cantidad de numeros menores a cero son:', cantnumeronega)
