#Questão da OBI: https://olimpiada.ic.unicamp.br/pratique/ps/2016/f1/chaves/

def contagem_de_chaves(codigo):
    aberto = 0
    fechado = 0

    for linha in codigo:
        for elemento in linha:
            for char in elemento:
                if char == "{":
                    aberto+= 1
                elif char == "}":
                    fechado+= 1
                    if fechado > aberto:
                        return 'N'
        if aberto == fechado:
            print(f'qtd = {aberto}')
            return 'S'
        else:
            return 'N'


N = int(input())
codigo = [input().split() for _ in range(N)]

resultado = contagem_de_chaves(codigo)

print(resultado) 


