import csv


def entrada_dados():
    linha=[]
    lista=ler_tabela()
    texto = input("Digite seu nome:")
    telefone = input("Digite o telefone de %s:" % (texto))
    linha=[texto,telefone]
    lista.append(linha)
    print("*" * 50)
    print("Cadastrado com Sucesso")
    print("*" * 50)
    gravar(lista)
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

    lista=ler_tabela()
    procurar()
    while True:
        aux=int(input("Qual o indice que deseja manipular:"))
        if aux>len(lista):
           print("Tente Novamente")
        else:
            return aux
            break
def procurar():
   bool = False
   lista = ler_tabela()
   texto = input("Digite o nome a pesquisar:")
   for i in lista:
       if texto in i[0]:
           print("-"*50)
           print("cod:%d\nNome:%s\nTelefone:%s"%(lista.index(i),i[0],i[1]))
           bool=True

   if bool == False:
       print("Nome Não encontrado Tente Novamente!!")



def alterar():
    lista=ler_tabela()
    indice=consultar()
    dado=lista[indice]
    while True:
        print("\nNome:%s, Telefone:%s\n"%(dado[0],dado[1]))
        print("Se deseja alterar o nome digite 1")
        print("Se deseja alterar o telefone digite 2")
        print("Se deseja alterar o nome e telefone digite 3")
        aux=int(input("Sua escolha:"))
        if aux==1:
            dado[0]=input("Digite o novo Nome:")
            break
        elif aux==2:
            dado[1]=input("Digite o novo Telefone:")
            break
        elif aux==3:
            dado[0] = input("Digite o novo Nome:")
            dado[1] = input("Digite o novo Telefone:")
            break
        else:
            print("\nOpção Invalida!!!")


    lista[indice]=dado
    print("*"*50)
    print("Alterado com Sucesso")
    print("*" * 50)
    gravar(lista)

def remover():
    lista = ler_tabela()
    del lista[consultar()]
    print("*" * 50)
    print("Deletado com Sucesso")
    print("*" * 50)
    gravar(lista)

opcao=0
while opcao==0:
    print("\nDigite 1 para Inserir Dados")
    print("Digite 2 para Pesquisar um cadastro")
    print("Digite 3 para Alterar Um cadastro")
    print("Digite 4 para Excluir um Cadastro")
    print("Digite 5 para Imprimir a Tabela")
    print("Digite 6 para Sair do Software")
    opcao = int(input("Sua Escolha:"))
    
    if opcao==1:
        entrada_dados()
        opcao=0
    elif opcao==2:
        procurar()
        aux="s"
        while aux=="s":
            aux =input("\nDeseja Procurar novamente?(s/n)")
            if aux=="s":
                procurar()
            elif aux=="n":
                opcao=0
            else:
                print("Opção Invalida!!")
                aux="s"

    elif opcao==3:
        alterar()
        opcao=0
    elif(opcao==4):
        remover()
        opcao=0
    elif(opcao==5):
        lista=ler_tabela()
        for i in lista:
            print("-" * 50)
            print("Nome:%s\nTelefone:%s" % (i[0], i[1]))
        opcao=0






















