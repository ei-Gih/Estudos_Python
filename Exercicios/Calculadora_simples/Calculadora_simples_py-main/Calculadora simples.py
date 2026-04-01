# 1. Passo a passo lógico para resolver:
# Identificar o que precisa ser feito: criar um programa que realize quatro operações básicas: soma, subtração, multiplicação e divisão.
# Solicitar ao usuário dois números: o programa precisa de dois valores para fazer a operação.
# Solicitar ao usuário qual operação quer fazer: pode ser, por exemplo, com texto ("soma") ou símbolos ("+").
# Executar a operação correspondente: dependendo da escolha do usuário, você faz uma das operações.
# Exibir o resultado: mostrar o resultado final da operação.

while True:
    num1=float(input("Qual o primeiro número? "))
    num2=float(input("Qual o segundo? "))

    operacao=int(input("""O que quer fazer com eles?
               1 - Adição
               2 - Subtração
               3 - Multiplicação
               4 - Divisão
               5 - Divisão inteira
               6 - Sair
    Opção: """))

    resultado = None

    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4:
        resultado = num1 / num2
    elif operacao == 5:
        resultado = num1 // num2
    elif operacao == 6:  
        print("Saindo...")
        break
    else:
        print("Valor invalido ( Digite uma operação valida)")

    if resultado is not None:
        print(f"Resultado: {resultado}\n")

    continuar = input("\nDeseja fazer outra operação? (s/n): ").strip().lower()
    if continuar != 's':
        print("Até mais! 👋")
        break