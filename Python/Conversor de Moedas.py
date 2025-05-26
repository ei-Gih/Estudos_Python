#Programa que lê o quanto uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#Considerando US$1,00= R$5,50.

real= float(input("Quanto dinheiro você tem na carteira? R$"))
dolar= real/ 5.50
euro= real/6.49
yen= real/0.04

print(f"Com R${real:.2f} você pode comprar US${dolar:.2f}, ou, €{euro:.2f},ou , ¥{yen:.2f}")


