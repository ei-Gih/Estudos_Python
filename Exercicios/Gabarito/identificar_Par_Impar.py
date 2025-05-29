while True:
    try:
        num = int(input("Digite um número: "))
        
        if num % 2 == 0:
            resultado = "Par"
        else:
            resultado = "Ímpar"

        print(f"O número {num} é: {resultado}")
        
    except ValueError:
        print("Você deve digitar um número inteiro!")
        continue  # Volta para o início do loop e pede novamente

    continuar = input("Deseja continuar? (s/n): ")

    if continuar.lower() != "s":
        print("Programa encerrado. Até mais!")
        break

    print("-" * 30)