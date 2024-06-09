# Prova da Olimpíada Brasileira de Informática 2023 (https://olimpiada.ic.unicamp.br/static/extras/obi2023/provas/ProvaOBI2023_f1ps.pdf)

linhas, colunas = map(int, input().split())

matriz = []

# bom só para eu nn esquecer, o for está aqui para fazer a matriz de acordo com o tamanho passado pelo input acima, dai a variavel "linha" vai pegar o valor da primeira linha da matriz, que será add na variavel "matriz" pelo metodo"append" 
for i in range(linhas):
    linha = [int(l)for l in input().split()]  
    matriz.append(linha)

# pLinha = I = tipo J = tamanho
numPedidos = int(input())
pedidos = []

for pedido in range(numPedidos):
    pLinha = [int(p)for p in input().split()]
    pedidos.append(pLinha) 

vendas= 0
# explicaçãooooooooooooo da linha 23 a 26. Bom é o seguinte a pessoa faz o pedido dessa forma 1 1, pois esta falando que quer acessar a linha 1 da coluna 1 obs: é por isso que temos duas matrizes nesse programa. Bom pro programa acessar a l e c, é preciso ter um controle de indice. Portanto foi criado um for para a cada pedido. 
# Seguinte primeiro precisamos dividir em i = tipo e j = tamanho que está na lista pedido ent se a pessoa digitar 1 2, vai ficar assim tipo=1 e tamanho=2. Feito isso temos que ter ctz que tem estoque para aquele pedido e pra isso acessamos o indice do tipo e tamanho colocando -1 para ajustar os indices e dps dessa verificação tiramos uma unidade que esta na posição matriz[tipo - 1][tamanho - 1]. 
for pedido in pedidos:
    tipo, tamanho = pedido
    if matriz[tipo - 1][tamanho - 1] > 0:
        matriz[tipo - 1][tamanho - 1] -= 1
        vendas += 1


print(vendas)