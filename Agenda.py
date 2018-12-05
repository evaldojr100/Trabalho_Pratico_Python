import csv

arquivo_csv=[]
def entrada_dados():
    linha=[]
    cod=len(arquivo_csv)+1
    texto = input("Digite seu nome:")
    telefone = input("Digite o telefone de %s:" % (texto))
    linha=[cod,texto,telefone]
    arquivo_csv.append(linha)
    gravar()
def gravar(lista):
    with open("dados.csv","w") as arquivo:
        writer = csv.writer(arquivo, delimiter=',')
        writer.writerows(lista)
def ler_tabela():
    with open("dados.csv", "r") as arquivo:
        dados = list((csv.reader(arquivo, delimiter=',')))
        arquivo.close()
        return dados

def consultar():
    while True:
        bool =False
        lista = ler_tabela()
        texto = input("Digite o nome a pesquisar:")
        for i in lista:
            if texto in i[0]:
                return lista.index(i)
                bool=True
                break
        if bool == False:
            print("Nome Não encontrado Tente Novamente!!")


def alterar():
    lista=ler_tabela()
    indice=consultar()
    dado=lista[indice]
    print("\nNome:%s, Telefone:%s\n"%(dado[0],dado[1]))
    print("Se deseja alterar o nome digite 1")
    print("Se deseja alterar o telefone digite 2")
    print("Se deseja alterar o nome e telefone digite 3")
    aux=int(input("Sua escolha:"))
    if aux==1:
        dado[0]=input("Digite o novo Nome:")
    elif aux==2:
        dado[1]=input("Digite o novo Telefone:")
    elif aux==3:
        dado[0] = input("Digite o novo Nome:")
        dado[1] = input("Digite o novo Telefone:")
    lista[indice]=dado
    gravar(lista)

def remover():
    lista = ler_tabela()
    del lista[consultar()]
    gravar(lista)

opcao=0
while opcao==0:
    print("Digite 1 para Inserir Dados")
    print("Digite 2 para Pesquisar um cadastro")
    print("Digite 3 para Alterar Um cadastro")
    print("Digite 4 para Excluir um Cadastro")
    print("Digite 5 para Imprimir a Tabela")
    opcao = int(input("Sua Escolha:"))
    
    if opcao==1:
        entrada_dados()
        opcao=0
    elif opcao==2:
        lista=ler_tabela()
        dado=lista[consultar()]
        print("\n---Resultado---\nNome:%s\nTelefone:%s\n"%(dado[0],dado[1]))
    elif opcao==3:
        alterar()
        opcao=0
    elif(opcao==4):
        remover()
        opcao=0
    elif(opcao==5):
        lista=ler_tabela()
        for i in lista:
            print("Nome:%s\nTelefone:%s\n" % (i[0], i[1]))
        opcao=0






















