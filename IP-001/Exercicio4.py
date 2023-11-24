# Exercício 4: Manipulação de variáveis de tipo string e explorando os métodos da classe.

# Declare uma variável nome atribuindo a ela seu nome completo
nome_completo = "Murilo Carlos Novais"

# Pesquise por funcionalidades já implementadas nas strings e separe em duas variáveis novas seu nome do seu sobrenome
espaco = nome_completo.find(" ")  # Encontra a posição do primeiro espaço
nome = nome_completo[:espaco]  # Slice para obter o nome
sobrenome = nome_completo[espaco+1:]  # Slice para obter o sobrenome

# Verifique qual das duas novas variáveis antecede a outra na ordem alfabética
ordem_alfabetica = sorted([nome, sobrenome])
nome_primeiro = ordem_alfabetica[0]
sobrenome_primeiro = ordem_alfabetica[1]

# Verifique a quantidade de caracteres de cada uma das novas variáveis
tamanho_nome = len(nome)
tamanho_sobrenome = len(sobrenome)

# Verifique se seu nome é uma palíndromo
nome_palindromo = nome.lower() == nome.lower()[::-1]

# Imprima os resultados
print(f"\nNome completo: {nome_completo}")
print(f"Nome: {nome}, Sobrenome: {sobrenome}")
print(f"Em ordem alfabética: {nome_primeiro}, {sobrenome_primeiro}")
print(f"Tamanho do Nome: {tamanho_nome}, Tamanho do Sobrenome: {tamanho_sobrenome}")
print(f"Seu nome é um palíndromo: {nome_palindromo}")
