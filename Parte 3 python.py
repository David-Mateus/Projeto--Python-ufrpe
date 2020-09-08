Sistema = []

def nome_aluno():
    return(input("Nome do aluno: "))
def cpf_aluno():
    return(input("CPF do aluno: "))
def arquivo_alu():
    return(input("Nome do arquivo: "))
def semestre():
    return(input("Qual seu semestre: "))
def mostra_fatos(nome, cpf, semes):
    print("Nome: %s CPF: %s Semestre: %s" %(nome, cpf, semes))

def buscar(nome):
    name = nome.lower()
    for d, e in enumerate(Sistema):
        if e[0].lower()== name:
            return d
        return None
def formar():
    global Sistema
    nome = nome_aluno()
    cpf = cpf_aluno()
    semes = semestre()
    Sistema.append([nome, cpf, semes])
def eliminação():
    global Sistema
    nome = nome_aluno()
    m = buscar(nome)
    if m != None:
        del Sistema[m]
    else:
        print("Nome não encontrado")
def inovar():
    m = buscar(nome_aluno())
    if m != None:
        nome = Sistema[m][0]
        cpf = Sistema[m][1]
        semes = Sistema[m][2]
        print("Encontrado: ")
        mostra_fatos(nome,cpf, semes)
        nome = nome_aluno()
        cpf = cpf_aluno()
        semes = semestre()
        Sistema[m] = [nome, cpf, semes]
    else:
        print("Nome não encontrado")

def informa():
    print("\nSistema\n\n-----------------------------------------")
    for e in Sistema:
        mostra_fatos(e[0],e[1], e[2])
    print("-----------------------------------------")

def fixar():
     nomearquivo = arquivo_alu()
     arquivo = open(nomearquivo, "w", encoding = "utf-8")
     for e in Sistema:
         arquivo.write("%s#%s\n" % (e[0], e[1], e[2]))
     arquivo.close()
def aluno():
    for e in Sistema:
        mostra_fatos(e[0], e[1], e[2])
    print("________________________________")

def validar(pergunta, inicio, fim):
    while True:
        try:
            valor = int(input(pergunta))
            if inicio <= valor <= fim:
                return(valor)
            return
        except ValueError:
            print("Valor invalido, favor digitar entre %d e %d" %(inicio, fim))

def menu():
    print('''
    1 - criação
    2 - atualizar
    3 - consulta
    4 - destruição
    5 - gravar
    6 - aluno
    0 - Sair
''')

    return validar("Escolha uma opção: ",0,6) #retorna o valor da opção

while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        formar()
    elif opção == 2:
        inovar()
    elif opção == 3:
        informa()
    elif opção == 4:
        eliminação()
    elif opção == 5:
        fixar()
    elif opção==6:
        aluno()

    
