# Prova da Olimpíada Brasileira de Informática 2023 (https://olimpiada.ic.unicamp.br/static/extras/obi2023/provas/ProvaOBI2023_f1ps.pdf)

valor = int(input())
A = int(input())
F = int(input())
P = int(input())


contas=[A,F,P]
contas.sort()
contasPg = 0

for conta in contas:
    if valor >= conta:
        valor-=conta
        contasPg+=1

print(contasPg)