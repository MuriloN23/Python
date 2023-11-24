# main.py

import os

# Função para reajustar salários em 10%
def reajusta_dez_porcento(empregados):
    for empregado in empregados:
        empregado["salario"] *= 1.1
1
# Função para ler dados de funcionários de um arquivo
def ler_arquivo(nome_arquivo):
    empregados = []
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.strip().split(", ")
                empregado = {
                    "nome": dados[0],
                    "sobrenome": dados[1],
                    "ano_nascimento": int(dados[2]),
                    "RG": dados[3],
                    "ano_admissao": int(dados[4]),
                    "salario": float(dados[5])
                }
                empregados.append(empregado)
    return empregados

# Função para salvar dados de empregados de volta no arquivo
def salvar_arquivo(nome_arquivo, empregados):
    with open(nome_arquivo, "w") as arquivo:
        for empregado in empregados:
            linha = f"{empregado['nome']}, {empregado['sobrenome']}, {empregado['ano_nascimento']}, {empregado['RG']}, {empregado['ano_admissao']}, {empregado['salario']:.2f}\n"
            arquivo.write(linha)

# Função para exibir informações dos empregados
def exibir_empregados(empregados):
    print("\nLista de Empregados:")
    for empregado in empregados:
        print(f"Nome: {empregado['nome']} {empregado['sobrenome']}, Ano de Nascimento: {empregado['ano_nascimento']}, RG: {empregado['RG']}, Ano de Admissão: {empregado['ano_admissao']}, Salário: R${empregado['salario']:.2f}")

# Função principal
def main():
    arquivo_empregados = "dados_empregados.txt"
    empregados = ler_arquivo(arquivo_empregados)

    while True:
        print("\nMenu de Opções:")
        print("1. Exibir informações dos empregados")
        print("2. Reajustar salários em 10%")
        print("0. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            exibir_empregados(empregados)
        elif opcao == "2":
            reajusta_dez_porcento(empregados)
            salvar_arquivo(arquivo_empregados, empregados)
            print("Salários reajustados em 10%. Dados salvos.")
        elif opcao == "0":
            print("Saindo do programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
