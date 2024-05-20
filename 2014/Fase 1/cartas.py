lista_cartas = []
ordem = ''

for i in range(5):
    num_cartas = int(input(""))
    lista_cartas.append(num_cartas) 

for i in range(len(lista_cartas) - 1):
    if lista_cartas[i] < lista_cartas[i + 1]:
        ordem = 'C'
    elif lista_cartas[i] > lista_cartas[i - 1]:
        ordem = 'D'
    else:
        ordem = 'N'
        break

if ordem == 'C':
    print(ordem)
elif ordem == 'D':
    print(ordem)
else:
    print(ordem)
