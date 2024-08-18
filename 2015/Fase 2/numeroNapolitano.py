# Mapeamento dos valores dos símbolos napolitanos
VALOR_DE = {
    'I': 1, 'V': 5, 'X': 10, 'L': 50,
    'C': 100, 'D': 500, 'M': 1000
}


simbolo = input()


valores = [VALOR_DE[caractere] for caractere in simbolo]


ultimas_posicoes = {}
proximos_maiores = [len(simbolo)] * len(simbolo)


for i in range(len(simbolo) - 1, -1, -1):
    for caractere in ultimas_posicoes:
        if valores[i] < VALOR_DE[caractere]:
            proximos_maiores[i] = min(proximos_maiores[i], ultimas_posicoes[caractere])
    ultimas_posicoes[simbolo[i]] = i


total = 0
for i in range(len(simbolo)):
    if proximos_maiores[i] != len(simbolo):
        valores[proximos_maiores[i]] -= valores[i]
    else:
        total += valores[i]


print(total)
