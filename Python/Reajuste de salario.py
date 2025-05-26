# Algoritmo que lê o salário de um funcionário e mostra seu novo salário.
# com 15% de aumento.

salario= float(input("Qual é o salario do funcionário? R$"))
novo= salario+(salario*15/100)

print(f"Um funcionário que ganhava R${salario:.2f}, com 15% de aumento, passa a receber R${novo:.2f}")