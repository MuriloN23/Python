#Exercício 5: Manipulação de variáveis de ponto flutuante, explorando as características e os limites.

# Demonstre como funcionam os operadores aritméticos e aritméticos compostos em Python
a = 5.0
b = 2.0

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

# Operadores compostos
a += 1.5  # Isso é equivalente a a = a + 1.5

# Imprime os resultados
print(f"\nSoma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Operação composta: {a}")

# Utilizando o operador de exponenciação, mostra a maior e a menor potência de 2 que pode ser representada
maior_potencia_de_2 = 2.0 ** 1023
menor_potencia_de_2 = 2.0 ** -1022

print(f"\nMaior potência de 2: {maior_potencia_de_2}")
print(f"Menor potência de 2: {menor_potencia_de_2}")

# As variáveis numéricas são imutáveis
c = 3.0
d = c
d += 2.0

# A variável original não é alterada
print(f"\nVariável original: {c}")

# Verifique quais métodos estão disponíveis para as variáveis de ponto flutuante
float_methods = dir(3.0)
print(f"\nMétodos disponíveis para variáveis de ponto flutuante: {float_methods}")
