# um programa que lê um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians,sin,cos,tan

an=float(input("Digite o ângulo que você deseja: "))
seno= sin(radians(an))
coss= cos(radians(an))
tang= tan(radians(an))

print(f"O ângulo dde {an}º tem o seno de {seno:.2f}")
print(f"O ângulo dde {an}º tem o cosseno de {coss:.2f}")
print(f"O ângulo dde {an}º tem o tangente de {tang:.2f}")