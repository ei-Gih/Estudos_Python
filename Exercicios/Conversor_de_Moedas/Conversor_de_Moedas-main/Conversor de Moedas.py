#Programa que lê o quanto uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# O usuário digita um valor em reais.
# O programa consulta as taxas de câmbio em tempo real.
# Converte para Dólar (USD), Euro (EUR) e Iene (JPY).
# Mostra o resultado formatado.

import requests

# Entrada do usuário
real = float(input("Quanto dinheiro você tem na carteira? R$"))

# Fazendo a requisição da cotação em tempo real
url = "https://api.exchangerate.host/latest?base=BRL&symbols=USD,EUR,JPY"
resposta = requests.get(url)
dados = resposta.json()

# Obtendo as cotações
cotacao_usd = dados["rates"]["USD"]
cotacao_eur = dados["rates"]["EUR"]
cotacao_jpy = dados["rates"]["JPY"]

# Convertendo
dolar = real * cotacao_usd
euro = real * cotacao_eur
yen = real * cotacao_jpy

# Exibindo o resultado
print(f"Com R${real:.2f} você pode comprar:")
print(f"- US${dolar:.2f}")
print(f"- €{euro:.2f}")
print(f"- ¥{yen:.2f}")
