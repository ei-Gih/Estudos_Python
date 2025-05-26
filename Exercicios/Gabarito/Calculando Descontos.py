#Algoritimoque lê o preço de um produto e mostra seu novo preço com 5% de desconto

preço= float(input("Qual é o preço do produto? R$"))
novo= preço - (preço*5/100)

print(f"O produto que custava R${preço:.2f}, na promoção com desconto de 5% vai custar r${novo:.2f}")