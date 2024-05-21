def inteiro(cartas):
    index = 0
    for cartinhas in cartas:
        cartas[index] = int(cartas[index])
        index += 1

ordem = ""
num_cartas = input()
num_cartas = num_cartas.split()

inteiro(num_cartas)

if num_cartas == sorted(num_cartas):
    ordem = "C"
elif num_cartas == sorted(num_cartas, reverse= True):
    ordem = "D"
else:
    ordem = "N"

print(ordem)