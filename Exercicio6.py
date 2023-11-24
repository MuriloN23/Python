L = [1,2,3,4,5,6,7,8,9]
print(L[::-1])   # Reverso da lista
print(L[-1::])    # Último elemento da lista
print(L[:-1:])    # Lista sem o último elemento
print(L[::-2])    # Lista reversa pulando de 2 em 2
print(L[-2::])    # Últimos dois elementos da lista
print(L[:-2:])    # Lista sem os dois últimos elementos


#------------------------------------------------------------------------


def signo_chines(ano_nascimento):
    signos = ['Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi', 'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro']
    indice_signo = ano_nascimento % 12
    return signos[indice_signo]

# Exemplo de uso:
ano_usuario = int(input("\nDigite o ano de nascimento: "))
signo = signo_chines(ano_usuario)
print(f"O signo chinês do usuário é: {signo}")
