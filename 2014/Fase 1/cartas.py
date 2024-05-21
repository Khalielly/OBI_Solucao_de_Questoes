ordem = ''

num_cartas = input("")
num_cartas = num_cartas.split()  

for i in range(len(num_cartas) - 1):
    if num_cartas[i] < num_cartas[i + 1]:
        ordem = 'C'
    elif num_cartas[i] > num_cartas[i - 1]:
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
