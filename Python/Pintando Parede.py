# Programa que Lê a largura e a altura de uma parede em metros,
# calcula a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta,pinta uma área de 2m².

larg= float(input("Largura da Parede: "))
alt= float(input("altura da parede: "))
area= larg*alt

print(f"A àrea da sua parede é de {area}m².")

tinta= area/2
print(f"Para pintar essa parede, você precisará de {tinta}l de tinta.")