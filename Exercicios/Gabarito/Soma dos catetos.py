# Um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import hypot

co= float(input("Comprimento do cateto oposto: "))
ca= float(input("Comprimento do cateto adjacente: "))
hi= (co**2 + ca**2) ** (1/2)
print(f"A hipotenusa vai medir {hi:.2f}")


#ou

hi= hypot(co,ca)
print(f"A hipotenusa vai medir {hi:.2f}")