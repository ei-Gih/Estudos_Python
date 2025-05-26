# Progrma que lê um numero inteiro e mostra na tela o seu Antecessor e seu Sucessor.

n=int(input("Digite um número: "))
a= n-1
s= n+1
print(f"Analisando o valor{n}, Seu antecessor é {a} e o sucessor é {s}")

# ou

n=int(input("Digite um número: "))
print("Analisando o valor{}, Seu antecessor é {} e o sucessor é {}".format(n,(n-1),(n+1)))


