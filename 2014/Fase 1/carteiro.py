# OBI 2024 - Nível Sênior - Fase 1: https://olimpiada.ic.unicamp.br/pratique/ps/2014/f1/carteiro/

N, M = [int(d) for d in input().split()]
casas = [int(c) for c in input().split()]
encomendas = [int(e) for e in input().split()]


tempo = 0 
local_atual = 0   
index = {}
i = 0

for casa in casas:
    index[casa] = i
    i+= 1

for encomenda in encomendas:
    tempo += abs(index[encomenda] - local_atual) 
    local_atual = index[encomenda] 
    
print(tempo)

