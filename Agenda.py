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
    lista = ler_tabela()
    texto = input("Digite o nome a pesquisar:")
    for i in lista:
        if texto in i[0]:
            return lista.index(i)

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























