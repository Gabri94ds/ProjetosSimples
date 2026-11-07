from produtos import consultarProduto, retornarIndice, consultarProdutoNome, calculoEstoque, verificarEstoqueBaixo

def main():

    while True:
        print("\n=== SISTEMA DE GERENCIAMENTO DE ESTOQUE ===")
        print("1. Consulta por índice")
        print("2. Consulta por nome")
        print("3. Valor do estoque")
        print("4. Produtos com estoque baixo")
        print("0. Sair")


        opcao = input("\nEscolha uma opção")

        if opcao == "1":
            indice = int(input("Informe o índice "))
            consultarProduto(indice)
        elif opcao == "2":
            nome = input("Informe o nome do produto")
            consultarProdutoNome(nome)
        elif opcao == "3":
            valorTotal = calculoEstoque()
            print(f"R$ {valorTotal:.2f}")
        elif opcao == "4":
            produtosEstoqueBaixo = verificarEstoqueBaixo()
            print(produtosEstoqueBaixo)
        elif opcao == "0":
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()