# 1. Recebe número;
# 2. Conta quantos divisores ele tem (de 1 até ele);
# 3. Se divisores == 2 → primo;
# 4. Senão → não primo;

def verificar_primo(numero):
    if numero < 2:
        return False  # Números menores que 2 não são primos
    for i in range(2, numero):
        if numero % i == 0:
            return False  # Se tiver outro divisor além de 1 e ele mesmo
    return True  # Se não encontrou divisores → é primo

while True:
    try:
        num = int(input("Digite um número: "))
        
        if verificar_primo(num):
            print(f"O número {num} é primo.")
        else:
            print(f"O número {num} NÃO é primo.")
    
    except ValueError:
        print("Por favor, digite um número inteiro!")
        continue  # Volta para o começo do loop

    continuar = input("Deseja verificar outro número? (s/n): ").lower()
    if continuar != "s":
        print("Programa encerrado. Até mais!")
        break
