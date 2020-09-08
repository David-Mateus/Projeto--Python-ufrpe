from modfunçôes import nome_pede
Sistema = []

def nome_pede():
    return(input("Nome da disciplina: "))
def pede_codigo():
    return(input("Digite seu codigo: "))
def nome_arquivo():
    return(input("Nome do arquivo: "))

def mostra_codigo(nome, codigo):
    print("Nome: %s codigo: %s" %(nome, codigo))
def procurar(nome):
    name = nome.lower()
    for d, e in enumerate(Sistema):
        if e[0].lower()==name:
            return d
        return None
def origem():
    global Sistema
    nome = nome_pede()
    codigo = pede_codigo()
    Sistema.append([nome, codigo])
def demolição():
    global Sistema
    nome = nome_pede()
    n = procurar(nome)
    if n != None:
        del Sistema[n]
    else:
        print("Nome não encontrado")
def atual():
    n = procurar(nome_pede())
    if n != None:
        nome = Sistema[n][0]
        codigo = Sistema[n][1]
        print("Encontrado: ")
        mostra_codigo(nome, codigo)
        nome = nome_pede()
        cpf = pede_codigo()
        Sistema[n] = [nome, codigo]
    else:
        print("Nome não encontrado.")
def pedir():
    print("\nSistema\n\n-----------------------------------")
    for e in Sistema:
        mostra_codigo(e[0],e[1])
    print("--------------------------------------------\n")
def grava():
     nomearquivo = nome_arquivo()
     arquivo = open(nomearquivo, "w", encoding = "utf-8")
     for e in Sistema:
         arquivo.write("%s#%s\n" % (e[0], e[1]))
     arquivo.close()
     
def tornar(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return(valor)
            return
        except ValueError:
            print("Valor invalido, favor digitar entre %d e %d" %(inicio,fim))
def menu():
    print('''
    1 - criação
    2 - atualizar
    3 - consulta
    4 - destruição
    5 - gravar
    0 - Sair
''')

    return tornar("Escolha uma opção: ",1,6) #retorna o valor da opção

while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        origem()
    elif opção == 2:
        atual()
    elif opção == 3:
        pedir()
    elif opção == 4:
        demolição()
    elif opção == 5:
        grava()
        
    



