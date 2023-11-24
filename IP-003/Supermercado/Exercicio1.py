# main.py

# Lista para armazenar os produtos (dicionários)
produtos = []

def inserir_produto():
    codigo = input("Digite o código do produto (13 caracteres): ")
    while len(codigo) != 13 or not codigo.isdigit():
        print("Código inválido. Deve conter 13 caracteres numéricos.")
        codigo = input("Digite o código do produto (13 caracteres): ")

    nome = input("Digite o nome do produto (começando com letra maiúscula): ")
    while not nome[0].isupper():
        print("Nome inválido. Deve começar com uma letra maiúscula.")
        nome = input("Digite o nome do produto (começando com letra maiúscula): ")

    preco = input("Digite o preço do produto: ")
    while not preco.replace('.', '').isdigit():
        print("Preço inválido. Deve ser um número válido.")
        preco = input("Digite o preço do produto: ")

    produtos.append({"codigo": codigo, "nome": nome, "preco": float(preco)})
    print("Produto inserido com sucesso.")

def excluir_produto():
    codigo = input("Digite o código do produto que deseja excluir: ")
    for produto in produtos:
        if produto["codigo"] == codigo:
            produtos.remove(produto)
            print("Produto excluído com sucesso.")
            return
    print("Produto não encontrado.")

def listar_produtos():
    print("\nLista de Produtos:")
    for i, produto in enumerate(produtos, start=1):
        print(f"{i}. Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")

def consultar_preco():
    codigo = input("Digite o código do produto para consultar o preço: ")
    for produto in produtos:
        if produto["codigo"] == codigo:
            print(f"O preço do produto {produto['nome']} é R${produto['preco']:.2f}")
            return
    print("Produto não encontrado.")

def main():
    while True:
        print("\nMenu de Opções:")
        print("1. Inserir um novo produto")
        print("2. Excluir um produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar o preço de um produto")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            inserir_produto()
        elif opcao == "2":
            excluir_produto()
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            consultar_preco()
        elif opcao == "0":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
