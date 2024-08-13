N = int(input())
C = input()

caractere = C[0]        #caractere = a
contador = 1
resultado=[]


for i in range(1, N):
    
    if C[i]== caractere: 
        contador +=1

    else:
        resultado.append(f"{contador} {caractere}")
        caractere = C[i]
        contador = 1

resultado.append(f"{contador} {caractere}")

print(' '.join(resultado))


