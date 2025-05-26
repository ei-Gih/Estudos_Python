# Programa que lê notas de um aluno e calcula e mostra a sua media.

nota1=float(input("Primeira nota do aluno: "))
nota2=float(input("Segunda nota do aluno: "))
nota3=float(input("Terceira nota do aluno: "))
nota4=float(input("Quarta nota do aluno: "))

media=(nota1+nota2+nota3+nota4)/4

print(f"A média entre {nota1:.1f}, {nota2:.1f}, {nota3:.1f} e {nota4:.1f}, é igual a {media:.1f}")
