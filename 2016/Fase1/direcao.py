#Questão da OBI: https://olimpiada.ic.unicamp.br/pratique/ps/2016/f1/direcao/
#não teve como testar esse codigo dentro do servidor da obi

direcao_amg, direcao_oasis = input().split()

leste = 0
norte = 90
oeste = 180
sul = 270

if direcao_amg == 'leste' or direcao_amg == 'Leste':
    direcao_amg = leste
elif direcao_amg == 'norte' or direcao_amg == 'Norte':
    direcao_amg = norte
elif direcao_amg == 'oeste' or direcao_amg == 'Oeste':
    direcao_amg = oeste
else:
    direcao_amg = sul

if direcao_oasis == 'leste' or direcao_oasis == 'Leste':
    direcao_oasis = leste
elif direcao_oasis == 'norte' or direcao_oasis == 'Norte':
    direcao_oasis = norte
elif direcao_oasis == 'oeste' or direcao_oasis == 'Oeste':
    direcao_oasis = oeste
else:
    direcao_oasis = sul

direcao_final = direcao_amg - direcao_oasis

direcao_final=abs(direcao_final)

print(direcao_final)