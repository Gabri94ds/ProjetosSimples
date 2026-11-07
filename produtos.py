import numpy as np

#Criando os arrays produtos, precos, estoque atual e estoque minimo

produtos = np.array(['Notebook', 'Mouse','Teclado','Monitor','Headset'])

precos = np.array([3500, 80, 150, 1200, 250])

estoqueAtual = np.array([15, 80, 45, 20, 35])

estoqueMinimo = np.array([5, 20, 10, 8, 10])

#--------------------------------------------------------------------------------

#Funções
#1. Função para consultar produtos

def consultarProduto(indice):
    try:
        indice = int(indice)

        if 0 <= indice < len(produtos):
            print(f'Produto: {produtos[indice]}')
            print(f'Preço: R$ {precos[indice]:.2f}')
            print(f'Estoque atual: {estoqueAtual[indice]}')
            print(f'Estoque mínimo: {estoqueMinimo[indice]}')
        else:
            print("índice fora dos limites do array")

    except (ValueError, TypeError):
        print("Erro: o índice dever ser um número inteiro válido")
    except IndexError:
        print("Erro: índice inexistente em um dos arrays")


def retornarIndice(nome):
    for i in range(0, len(produtos)):
        if produtos[i].strip().lower() == nome.strip().lower():
            return i
    return -1

def consultarProdutoNome(nome):
    indice = retornarIndice(nome)
    if indice == -1:
           print('Produto não encontrado!')
           return
    print(f'Produto: {produtos[indice]}')
    print(f'Preço: {precos[indice]:.2f}')
    print(f'Estoque atual: {estoqueAtual[indice]}')
    print(f'Estoque mínimo: {estoqueMinimo[indice]}')

def calculoEstoque():

    #Conceito de vetorização
    valorTotal = np.sum(precos * estoqueAtual)
    return valorTotal

def verificarEstoqueBaixo():

    mascara = estoqueAtual < estoqueMinimo #A saída é um array booleanda [true, false, false, true]
    return produtos[mascara] #pegamos somente os produtos que a mascara retornou True
    

