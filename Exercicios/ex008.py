# Estrutura de repetição for

lista_vendas=[1000,500,800,1500,2000,2300]
meta=1200
percentual_bonus=0.1

# for i in range(10):       # i in range, é quantas vezes voce deseja que aquele codigo seja executado
# for item in list:        # vai executar esse codigo para cada item da sua lista

for venda in lista_vendas:
    if venda >= meta:
        bonus= percentual_bonus * venda
    else:
        bonus = 0

    print(bonus)