import csv

lista=[]
def entrada_dados():
    linha=[]
    texto = input("Digite seu nome:")
    telefone = input("Digite o telefone de %s:" % (texto))
    linha=[texto,telefone]
    lista.append(linha)
    gravar()
def gravar():
    with open("dados.csv","w") as arquivo:
        writer = csv.writer(arquivo, delimiter=',')
        writer.writerows(lista)
def ler_tabela():
    with open("dados.csv", "r") as arquivo:
        dados = list(csv.reader(arquivo, delimiter=','))
        arquivo.close()
        return dados


'''opcao=0
while opcao==0:
    print("Digite 1 para Inserir Dados")
    print("Digite 2 para Pesquisar um cadastro")
    print("Digite 3 para Alterar Um cadastro")
    print("Digite 4 para Excluir um Cadastro")
    opcao = int(input("Sua Escolha:"))
    
    if opcao==1:
        entrada_dados()
        opcao=0'''























