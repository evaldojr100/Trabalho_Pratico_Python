import csv

def inserir():
    arquivo = open("dados.csv", "w")
    texto = input("Digite seu nome:")
    telefone = input("Digite o telefone de %s:" % (texto))
    arquivo.writelines((texto, "\t", telefone, "\n"))
    arquivo.close()

def procurar():
    arquivo = open("dados.csv", "r")
    lista = list(csv.reader(arquivo, delimiter=','))
    arquivo.close()
    return lista


print(lista)




