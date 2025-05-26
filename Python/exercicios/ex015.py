# Algoritmo que lê um numero e mostra o seu dobro, tiplo e a raiz quadrada.

n=int(input("Digite um número: "))
d= n*2
t= n*3
r= n**(1/2)
print((f"O dobro de {n} vale {d}."))
print((f"O triplo de {n} vale {t}."))
print(("A Raiz quadrada de {} é igual a {:.2f}.".format(n,r)))