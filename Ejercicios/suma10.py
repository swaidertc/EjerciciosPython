print("SUMA DE VALORES")
numero = int(input("Cuantos valores va a introducir? "))

if numero <= 0:
	print("¡Imposible!")
else:
    suma = 0
for i in range(1, numero + 1):
    valor = float(input(f"Escriba el numero {i}: "))
    suma = suma + valor
    
print(f"La suma de los numeros que ha escrito es {suma}")

