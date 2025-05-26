# Programa que pergunta a quantidade de Km percorridos por um carro algado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 pro Km rodado.

dias=int(input("Quantos dias alugados? "))
km= float(input("Quantos Km rodados? "))
pago= (dias* 60) + (km*0.15)
print(f"O total a pagar é de R${pago:.2f}")