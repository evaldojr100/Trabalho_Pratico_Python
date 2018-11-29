
arquivo= open("dados.csv","w")
for i in range(2):
    texto =input("Digite seu nome:")
    telefone = input("Digite o telefone de %s:"%(texto))
    arquivo.writelines((texto,"\t",telefone,"\n"))
arquivo.close()
arquivo= open("dados.csv","r")
for linha in arquivo.readlines():
    print (linha)
arquivo.close()

arquivo= open("dados.csv","w")
arquivo.writelines(("Luiz\t33212589\n"))
arquivo.close()

arquivo= open("dados.csv","r")
for linha in arquivo.readlines():
    print (linha)
arquivo.close()


