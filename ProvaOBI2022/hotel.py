diaria = int(input())
a = int(input())
dia = int(input())

x = 32
total = 0

if dia > 1 and dia <= 14:
    x =-dia
    diaria = diaria + dia * a
    total = x * diaria 

elif dia == 1:
    x =-dia
    total = x * diaria 

else:
    x =- dia
    diaria = diaria + 14 * a
    total = x * diaria 

print(total)
