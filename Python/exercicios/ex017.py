import random

num = random.randint(1,20)
print(num)

# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
# O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

n1=str(input("Escreva o primeiro nome: "))
n2=str(input("Escreva o segundo nome: "))
n3=str(input("Escreva o terceiro nome: "))
n4=str(input("Escreva o quarto nome: "))
lista = [n1,n2,n3,n4]

escolhido= random.choice(lista)
print(f"O aluno escolhido foi {escolhido}.")

random.shuffle(lista)
print("A ordem da apresentação será: ")
print(lista)
