# 📝 Contador de Vogais e Cosoantes em Python

Este é um projeto simples desenvolvido em Python com o objetivo de contar a quantidade de vogais em uma string informada pelo usuário. É o meu primeiro projeto focado em lógica de programação e estou em constante evolução na área! 🚀

---

## 💡 Descrição do Projeto

A aplicação solicita ao usuário que insira uma palavra ou frase e, em seguida, calcula e exibe a quantidade de vogaise consoantes presentes no texto. 

- Contagem de vogais (considera 'a', 'e', 'i', 'o', 'u' e suas versões maiúsculas).

- Contagem de consoantes (considera todas as letras que não são vogais, incluindo 'ç' e 'Ç' e suas versões maiúsculas).

- Interface interativa: o usuário pode digitar várias palavras sem reiniciar o programa.

- Tratamento de entrada: o programa não diferencia maiúsculas de minúsculas, pois o conjunto de caracteres inclui ambas.

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x

---

## 📄 Código Principal

```python

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

consoantes = set('bBcCçÇdDfFgGhHjJkKlLmMnNpPqQrRsStTvVwWxXyYzZ')

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

```

## 📖 Observações

- O conjunto de consoantes foi definido explicitamente, incluindo letras com acentos? Não, o código atual não inclui letras acentuadas. Se necessário, seria preciso expandir o conjunto.

- O programa não conta espaços, números ou caracteres especiais (como @, #, $, etc.) porque as funções só consideram vogais e consoantes definidas.

## ▶️ Exemplo de Saída

```

Digite a Palavra: Python

O número de vogais na palavra são: 1

O número de consoantes na palavra são: 5

Deseja Continuar? (s/n):  s

Digite a Palavra: Programação

O número de vogais na palavra são: 4

O número de consoantes na palavra são: 7

Deseja Continuar? (s/n):  n

```


## 🚀 Como Executar

1- Certifique-se de ter o Python instalado na sua máquina.

2- Copie o código acima para um arquivo com a extensão .py, por exemplo: conta_vogais.py.

3- Execute o script via terminal ou prompt de comando:

```bash
python conta_vogais.py
```
4- Insira a palavra ou frase desejada quando solicitado.

## 🎯 Objetivos de Aprendizado

✅ Praticar a criação de funções
✅ Trabalhar com estruturas de controle e conjuntos
✅ Aprender boas práticas na escrita de código

## 📄 Licença

Este projeto é livre para uso pessoal e educacional, Faz Parte do Projeto [Estudos Python](https://github.com/ei-Gih/Estudos_Python), cofira os outros.

##  ✨ Contribuição
Esse é o meu primeiro projeto na área de programação e estou sempre buscando melhorar! Feedbacks e sugestões são muito bem-vindos. 🚀

