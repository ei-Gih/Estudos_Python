
def conta_vogais(texto):
# Defina um conjunto de vogais tanto minúsculas quanto maiúsculas:
    vogais = set('aeiouAEIOU')
    
# Inicialize um contador para contar as vogais:
    contador = 0

# Iteramos pelos caracteres da string
    for char in texto:
# Verifique se o caractere atual é uma vogal e incremente o valor do contador:
        if char in vogais:
            contador += 1
    
    return contador
def conta_consoante(texto):
    consoantes= set('bBcCçÇdddDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ')
    contador = 0

    for char in texto:
        if char in consoantes:
            contador += 1
    return contador

while True:
    # Solicitamos ao usuário que insira uma string
    texto = input("Digite a Palavra: ")

    # Chamamos a função e exibimos o resultado
    resultado_v = conta_vogais(texto)
    resultado_c = conta_consoante(texto)
    print(f"O número de vogais na palavra são: {resultado_v}")
    print(f"O número de consoantes na palavra são: {resultado_c}")

    continuar = input("Deseja Continuar? (s/n):  ")
    
    if continuar != "s":
        break