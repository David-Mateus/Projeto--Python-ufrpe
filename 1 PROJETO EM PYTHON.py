Sistema = []#Criando uma Lista vazia.
Dis = []#Criando uma Lista vazia.
Alu = []#Criando uma Lista vazia.
Tur = []#Criando uma Lista vazia.
#Funçôes
def pede_nome(): 
    return(input("Nome do professor: "))            #Retorna o valor dessa funçâo
def pede_cpf():
    return(input("CPF do professor: "))
def pede_departamento():
    return(input("Departamento do professor: "))
def pede_nome_arquivo():
    return(input("Nome do arquivo: "))

def mostra_dados(nome, cpf, departamento):
    print("Nome do Professor: %s CPF: %s Departamento: %s" %(nome, cpf, departamento))

                                 #DISCIPLINA
def nome_pede():  
    return(input("Nome da disciplina: "))           #Retorna o valor dessa funçâo
def pede_codigo():
    return(input("Digite seu codigo: "))
def nome_arquivo():
    return(input("Nome do arquivo: "))

def mostra_codigo(nome, codigo):
    print("Nome da Disciplina: %s codigo: %s" %(nome, codigo))
                            
                                  #ALUNO
def nome_aluno(): 
    return(input("Nome do aluno: "))                 #Retorna o valor dessa funçâo
def cpf_aluno():
    return(input("CPF do aluno: "))
def mostra_fatos(nome, cpf):
    print("Nome do Aluno: %s CPF: %s" %(nome, cpf))
def arquivo_alu():
    return(input("Nome do arquivo: "))

                           #TURMA
def codigo_turma():
    return(input("Codigo da turma: "))               #Retorna o valor dessa funçâo
def periodo_ufrpe():
    return(input("Qual o seu periodo: "))
def codigo_disciplina():
    return(input("Codigo da sua disciplina: "))
def cpf_professor():
    return(input("CPF do professor: "))
def cpf_aluno():
    return(input("CPF do Aluno: "))
def nome_do_arquivo():
    return(input("Nome do arquivo: "))
def exibir_dados(turma, periodo_ufrpe, disciplina, cpfpro, cpfalu):
    print("Código da turma: %s Periodo: %s Código da disciplina: %s  CPF do professor: %s CPF do aluno: %s" %(turma, periodo_ufrpe, disciplina, cpfpro, cpfalu))




def pesquisa(nome):
    name = nome.lower()                    #convertendo para minúsculo.
    for d, e in enumerate(Sistema):        #acessar a posição do elemento e o prorpio
        if e[0].lower() == name:
            return d
        return None

def procurar(nome):   #DISCIPLINA
    name = nome.lower()
    for d, e in enumerate(Dis):
        if e[0].lower()==name:
            return d
        return None

def buscar(nome):  #ALUNO
    name = nome.lower()
    for d, e in enumerate(Alu):
        if e[0].lower()== name:
            return d
        return None

def exploração(turma): #TURMA
    nome = turma.lower()
    for d, e in enumerate(Tur):
        if e[0].lower() == nome:
            return d
        return None

    
def criação():
    global Sistema
    nome = pede_nome()
    cpf = pede_cpf()
    departamento = pede_departamento()
    Sistema.append([nome,cpf,departamento]) #adicionar dados

def origem(): #DISCIPLINA
    global Dis
    nome = nome_pede()
    codigo = pede_codigo()
    Dis.append([nome, codigo])

def formar(): #ALUNO
    global Alu
    nome = nome_aluno()
    cpf = cpf_aluno()
    Alu.append([nome, cpf])

def gerar(): #TURMA
    global Tur
    turma = codigo_turma()
    periodo = periodo_ufrpe()
    disciplina = codigo_disciplina()
    cpfpro = cpf_professor()
    cpfalu = cpf_aluno()
    Tur.append([turma, periodo, disciplina, cpfpro, cpfalu])




def destruição():
    global Sistema
    nome = pede_nome()
    p = pesquisa(nome) #chama a função pesquisa
    if p != None:#Executa caso a condição for verdadeira
            del Sistema[p]
    else:
        print("Nome não encontrado") #caso for falsa

def demolição(): #DISCIPLINA
    global Dis
    nome = nome_pede()
    n = procurar(nome)
    if n != None:
        del Dis [n]
    else:
        print("Nome não encontrado")

def eliminação(): #ALUNO
    global Alu
    nome = nome_aluno()
    m = buscar(nome)
    if m != None:
        del Alu[m]
    else:
        print("Nome não encontrado")

def fim(): #TURMA
    global Tur
    turma = codigo_turma()
    p = exploração(turma)
    if p != None:
        del Sistema[p]
    else:
        print("Nome não encontrado")

def atualizar():
    p = pesquisa(pede_nome())              #entrada de dados
    if p != None:                          # caso a condição seja verdadeira
        nome = Sistema[p][0]               # procurando os dados no Sistema
        cpf = Sistema [p][1]
        departamento = Sistema[p][2]
        print("Encontrado: ")
        mostra_dados(nome, cpf, departamento)
        nome = pede_nome()
        cpf = pede_cpf()
        departamento = pede_departamento() #dados editados
        Sistema[p] = [nome, cpf, departamento] #Armazenando os novos dados
    else:
        print("Nome não encontrado.")      #caso a condição seja falsa

def atual():   #DISCIPLINA
    n = procurar(nome_pede())
    if n != None:
        nome = Dis[n][0]
        codigo = Dis[n][1]
        print("Encontrado: ")
        mostra_codigo(nome, codigo)
        nome = nome_pede()
        cpf = pede_codigo()
        Dis [n] = [nome, codigo]
    else:
        print("Nome não encontrado.")

def inovar(): #ALUNO
    m = buscar(nome_aluno())
    if m != None:
        nome = Alu[m][0]
        cpf = Alu[m][1]
        print("Encontrado: ")
        mostra_fatos(nome,cpf)
        nome = nome_aluno()
        cpf = cpf_aluno()
        Alu[m] = [nome, cpf]
    else:
        print("Nome não encontrado")


def renovar(): #TURMA
    p = exploração(codigo_turma())
    if p != None:
        turma = [p][0]
        periodo = Tur [p][1]
        disciplina = Tur[p][2]
        cpfpro = Tur[p][3]
        cpfalu = Tur[p][4]
        print("Econtrado: ")
        exibir_dados(turma, periodo_ufrpe, disciplina, cpfpro, cpfalu)
        turma = codigo_turma()
        periodo = periodo_ufrpe()
        disciplina = codigo_disciplina()
        cpfpro = cpf_professor()
        cpfalu = cpf_aluno()
        Tur[p] = [turma, periodo_ufrpe, disciplina, cpfpro, cpfalu]
    else:
        print("Nome não encontrado.")


def consulta():                              #mostra a lista do sistema
    print("\nSistema\n\n------------------------------------")
    for e in Sistema:
        mostra_dados(e[0], e[1], e[2])
    print("------------------------------------\n")

def pedir(): #DISCIPLINA
    print("\nSistema\n\n-----------------------------------")
    for e in Dis:
        mostra_codigo(e[0],e[1])
    print("--------------------------------------------\n")

def informa(): #ALUNO
    print("\nSistema\n\n-----------------------------------------")
    for e in Alu:
        mostra_fatos(e[0],e[1])
    print("-----------------------------------------")

def exame(): #TURMA
    print("\nSistema\n\n___________________________________________")
    for e in Tur:
        exibir_dados(e[0], e[1], e[2], e[3], e[4])
    print("__________________________________________\n")

def grava(): #PROFESSOR
     nome_arquivo = pede_nome_arquivo()
     arquivo = open(nome_arquivo, "w", encoding = "utf-8")
     for e in Sistema:
         arquivo.write("%s#%s#%s\n" % (e[0], e[1], e[2]))
     arquivo.close()

def decorar(): #DISCIPLINA
     nomearquivo = nome_arquivo()
     arquivo = open(nomearquivo, "w", encoding = "utf-8")
     for e in Dis:
         arquivo.write("%s#%s\n" % (e[0], e[1]))
     arquivo.close()
def fixar():  #ALUNO
     nomearquivo = arquivo_alu()
     arquivo = open(nomearquivo, "w", encoding = "utf-8")
     for e in Alu:
         arquivo.write("%s#%s\n" % (e[0], e[1]))
     arquivo.close()

def memorizar(): #TURMA
     nomearquivo = nome_do_arquivo()
     arquivo = open(nomearquivo, "w", encoding = "utf-8")
     for e in Tur:
         arquivo.write("%s#%s#%s#%s#%s\n" % (e[0], e[1], e[2], e[3], e[4]))
     arquivo.close()

def relatorio():
    print('''_____________________ATA de Exercicio______________________''')
    print()
    for e in Sistema:
        mostra_dados(e[0]+'\n',e[1]+'\n',e[2]+'\n')
    print('___________________________________________________________')
    for a in Dis:
        mostra_codigo(a[0]+'\n',a[1]+'\n')
    print('___________________________________________________________')
    for v in Alu:
        mostra_fatos(v[0]+'\n', v[1]+'\n')
    print('___________________________________________________________')
    for i in Tur:
        exibir_dados(i[0]+'\n' ,i[1], i[2]+'\n',i[3], i[4])
    print('___________________________________________________________')


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
    PROFESSOR:
    1 - criação
    2 - atualizar
    3 - consulta
    4 - destruição
    5 - Gravar
    DISCIPLINA:
    6 - criação
    7 - atualizar
    8 - consulta
    9 - destruição
    10 - Gravar
    ALUNO:
    11 - criação
    12 - atualizar
    13 - consulta
    14 - destruição
    15 - Gravar
    TURMA:
    16 - criação
    17 - atualizar
    18 - consulta
    19 - destruição
    20 - Gravar
    ATA DE EXERCÍCIO
    21 - relatóio

    0  - Saí
    
''')

    return validar("Escolha uma opção: ",0,21) #retorna o valor das opções

          
while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        criação()
    elif opção == 2:
        atualizar()
    elif opção == 3:
        consulta()
    elif opção == 4:
        destruição()
    elif opção == 5:
        grava()
    elif opção == 6:
        origem()
    elif opção == 7:
        atual()
    elif opção == 8:
        pedir()
    elif opção == 9:
        demolição()
    elif opção == 10:
        decorar()
    elif opção == 11:
        formar()
    elif opção == 12:
        inovar()
    elif opção == 13:
        informa()
    elif opção == 14:
        eliminação
    elif opção == 15:
        fixar()
    elif opção == 16:
        gerar()
    elif opção == 17:
        renovar()
    elif opção == 18:
        exame()
    elif opção == 19:
        fim()
    elif opção == 20:
        memorizar()
    elif opção == 21:
        relatorio()

