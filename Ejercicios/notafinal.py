notamatematicas = float(input('Digite la nota de matematicas\n'))
notaespañol = float(input('Digite la nota de espalñol\n'))
notaeconomia = float(input('Digite la nota de economia\n'))
notaprogramacion = float(input('Digite la nota de programacion\n'))
notaingles = float(input('Digite la nota de ingles\n'))

notaltotal = notamatematicas + notaespañol + notaeconomia + notaprogramacion + notaingles

notafinal = notaltotal / 5
print('Su promedio de las 5 materias es:', notafinal)