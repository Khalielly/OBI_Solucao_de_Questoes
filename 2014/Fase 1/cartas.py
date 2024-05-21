ordem = ''

num_cartas = input("")
num_cartas = num_cartas.split()  

for i in range(len(num_cartas) - 1):
    if num_cartas[i] < num_cartas[i + 1]:
        ordem = 'C'
    elif num_cartas[i] < num_cartas[i - 1]:
        ordem = 'D'
    else:
        ordem = 'N'
        break

if ordem == 'C':
    print(f'{ordem}\n')
elif ordem == 'D':
    print(f'{ordem}\n')
else:
    print(f'{ordem}\n')
