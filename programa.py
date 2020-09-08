Sistema = []#Criando uma Lista vazia.
Dis = []#Criando uma Lista vazia.
Alu = []#Criando uma Lista vazia.
Tur = []#Criando uma Lista vazia.
#Funçôes
def pede_nome():            #PROFESSOR
    return(input("Nome do professor: "))#Retorna o valor dessa funçâo
def pede_cpf():
    return(input("CPF do professor: "))
def pede_departamento():
    return(input("Departamento do professor: "))
def semestre_pro():
    return(input("Qual seu Semestre: "))
def pede_nome_arquivo():
    return(input("Nome do arquivo: "))
def mostra_dados(nome, cpf, departamento,semes):
    print("Nome do Professor: %s CPF: %s Departamento: %s Semestre: %s" %(nome, cpf, departamento, semes))
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
def semestre():
    return(input("Qual seu Semestre: "))
def mostra_fatos(nome, cpf,semestree):
    print("Nome do Aluno: %s CPF: %s Semestre: %s" %(nome, cpf,semestree))
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
    name = nome.lower()    #convertendo para minúsculo.
    for d, e in enumerate(Sistema): #acessar a posição do elemento e o prorpio
        if e[0].lower() == name: #executando o loop
            return d             #executa caso a condição seja verdadeira
    return None              #executa caso seja falsa
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
    global Sistema      #Definindo variavel como Global
    nome = pede_nome()  #Entrada de dados
    cpf = pede_cpf()    #Entrada de dados
    departamento = pede_departamento() #Entrada de dados
    semestre = semestre_pro()          #Entrada de dados
    Sistema.append([nome,cpf,departamento,semestre]) #adicionar dados
def origem(): #DISCIPLINA
    global Dis
    nome = nome_pede()
    codigo = pede_codigo()
    Dis.append([nome, codigo])
def formar(): #ALUNO
    global Alu
    nome = nome_aluno()
    cpf = cpf_aluno()
    semestree = semestre()
    Alu.append([nome, cpf, semestree])
def gerar(): #TURMA
    global Tur
    turma = codigo_turma()
    periodo = periodo_ufrpe()
    disciplina = codigo_disciplina()
    cpfpro = cpf_professor()
    cpfalu = cpf_aluno()
    Tur.append([turma, periodo, disciplina, cpfpro, cpfalu])



def destruição():
    global Sistema     #Definindo a função como global #podem ser acessada por modúlos
    nome = pede_nome() #Entrada de dados
    p = pesquisa(nome) #chama a função pesquisa
    if p != None:#Executa caso a condição for verdadeira
        del Sistema[p]#executa caso a condição seja verdadeira
        print("Destruido com sucesso!")
    else:
        print("Nome não encontrado") #caso for falsa
def demolição(): #DISCIPLINA
    global Dis
    nome = nome_pede()
    n = procurar(nome)
    if n != None:
        del Dis [n]
        print("Destruido com sucesso!")
    else:
        print("Nome não encontrado")
def eliminação(): #ALUNO
    global Alu
    nome = nome_aluno()
    m = buscar(nome)
    if m != None:
        del Alu[m]
        print("Destruido com sucesso")
    else:
        print("Nome não encontrado")
def fim(): #TURMA
    global Tur
    turma = codigo_turma()
    p = exploração(turma)
    if p != None:
        del Sistema[p]
        print("Destruido com sucesso")
    else:
        print("Nome não encontrado")
def atualizar():
    p = pesquisa(pede_nome())              #entrada de dados
    if p != None:                          # caso a condição seja verdadeira
        nome = Sistema[p][0]               # procurando os dados no Sistema
        cpf = Sistema [p][1]               #Procurando os dados no Sistema
        departamento = Sistema[p][2]       #procurando os dados no sistema
        semestre = Sistema[p][3]           #Procurando os dados no Sistema
        print("Encontrado")                #exibir informação
        mostra_dados(nome, cpf, departamento,semestre)#mostra dados
        nome = pede_nome()                  #dados novos
        cpf = pede_cpf()                    #dados novos
        departamento = pede_departamento() #dados editados
        semestre = semestre_pro()
        Sistema[p] = [nome, cpf, departamento, semestre] #Armazenando os novos dados
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
        semestree = Alu[m][2]
        print("Encontrado: ")
        mostra_fatos(nome,cpf)
        nome = nome_aluno()
        cpf = cpf_aluno()
        semestree = semestre()
        Alu[m] = [nome, cpf, semestree]
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
        mostra_dados(e[0], e[1], e[2], e[3])
    print("------------------------------------\n")
def pedir(): #DISCIPLINA
    print("\nSistema\n\n-----------------------------------")
    for e in Dis:
        mostra_codigo(e[0],e[1])
    print("--------------------------------------------\n")
def informa(): #ALUNO
    print("\nSistema\n\n-----------------------------------------")
    for e in Alu:
        mostra_fatos(e[0],e[1], e[2])
    print("-----------------------------------------")
def exame(): #TURMA
    print("\nSistema\n\n___________________________________________")
    for e in Tur:
        exibir_dados(e[0], e[1], e[2], e[3], e[4])
    print("__________________________________________\n")
def grava(): #PROFESSOR
     nome_arquivo = pede_nome_arquivo()
     arquivo = open(nome_arquivo, "w+", encoding = "utf-8") #cria um arquivo e o "W" Escrita, apagar tudo se existir
     for e in Sistema:
         arquivo.write("%s#%s#%s#%s\n" % (e[0], e[1], e[2], e[3]))
     arquivo.close()
def decorar(): #DISCIPLINA
     nomearquivo = nome_arquivo()
     arquivo = open(nomearquivo, "w+", encoding = "utf-8")
     for e in Dis:
         arquivo.write("%s#%s\n" % (e[0], e[1]))
     arquivo.close()
def fixar():  #ALUNO
     nomearquivo = arquivo_alu()
     arquivo = open(nomearquivo, "w+", encoding = "utf-8")
     for e in Alu:
         arquivo.write("%s#%s#%s\n" % (e[0], e[1], e[2]))
     arquivo.close()
def memorizar(): #TURMA
     nomearquivo = nome_do_arquivo()
     arquivo = open(nomearquivo, "w+", encoding = "utf-8")
     for e in Tur:
         arquivo.write("%s#%s#%s#%s#%s\n" % (e[0], e[1], e[2], e[3], e[4]))
     arquivo.close()
def relatorio():
    print('''_____________________|ATA de Exercicio|_____________________''')
    print()
    for e in Sistema:
        mostra_dados(e[0]+'\n',e[1]+'\n',e[2]+'\n',e[3])
    print('___________________________________________________________')
    print()
    for a in Dis:
        mostra_codigo(a[0]+'\n',a[1]+'\n')

    print('___________________________________________________________')
    print()
    for v in Alu:
        mostra_fatos(v[0]+'\n', v[1]+'\n',v[2])
    print('___________________________________________________________')
    print()
    for i in Tur:
        exibir_dados(i[0]+'\n' ,i[1], i[2]+'\n',i[3], i[4])
    print('___________________________________________________________')

def professor():
    print("""____________|Todas as turmas por professor|______________""")
    print()
    for e in Sistema:
        mostra_dados(e[0]+'\n',e[1]+'\n',e[2]+'\n',e[3])
    print("==========================================================")
    print()
    for v in Alu:
        mostra_fatos(v[0]+'\n', v[1]+'\n', v[2])
    print('==========================================================')
    print()
    for a in Dis:
        mostra_codigo(a[0]+'\n',a[1]+'\n')
    print('==========================================================')
    print()
    
    for i in Tur:
        exibir_dados(i[0]+'\n' ,i[1], i[2]+'\n',i[3], i[4])
    print('==========================================================')

def semestre_turma():
    print('''____________|Turmas por Semestre|____________''')
    print()
    for e in Sistema:
        mostra_dados(e[0]+'\n',e[1]+'\n',e[2]+'\n',e[3])
    print("==========================================================")
    print()
    for v in Alu:
        mostra_fatos(v[0]+'\n', v[1]+'\n',v[2])
    print('==========================================================')
    print()
    for a in Dis:
        mostra_codigo(a[0]+'\n',a[1]+'\n')
    print('==========================================================')
    print()
    
    for i in Tur:
        exibir_dados(i[0]+'\n' ,i[1], i[2]+'\n',i[3], i[4]+'\n',)
    print('==========================================================')

def aluno():
    print('''____________|Lista de turmas por aluno|____________''')
    print()
    for v in Alu:
        mostra_fatos(v[0]+'\n', v[1]+'\n', v[2])
    print('==========================================================')
    print()
    for e in Sistema:
        mostra_dados(e[0]+'\n',e[1]+'\n',e[2]+'\n', e[3])
    print("==========================================================")
    print()
    for a in Dis:
        mostra_codigo(a[0]+'\n',a[1]+'\n')
    print('==========================================================')
    print()
    for i in Tur:
        exibir_dados(i[0]+'\n' ,i[1], i[2]+'\n',i[3], i[4])
    print('==========================================================')

def semestre_alu():
    print("""_______________|Turma por Semestre|________________""")
    print()
    for e in Sistema:
        mostra_dados(e[0]+'\n',e[1]+'\n',e[2]+'\n',e[3])
    print("==========================================================")
    print()
    for v in Alu:
        mostra_fatos(v[0]+'\n', v[1]+'\n', v[2])
    print('==========================================================')
    print()
    for a in Dis:
        mostra_codigo(a[0]+'\n',a[1]+'\n')
    print('==========================================================')
    print() 
    for i in Tur:
        exibir_dados(i[0]+'\n' ,i[1], i[2]+'\n',i[3], i[4]+'\n')
    print('==========================================================')


def validar(pergunta, inicio, fim):   #Função para validar numeros inteiros
    while True:                       #Criando um loop infinito
        try:                          #Criando um acordo/condição
            valor = int(input(pergunta))#Entrada de dados
            if inicio <= valor <= fim:  #Determinado uma condição
                return(valor)#executa se for verdadeira
            return
        except ValueError:   #caso seja falsa
            print("Valor invalido, favor digitar entre %d e %d" %(inicio, fim))
def menu():
    print("""_____________|Sistemas de Controle Acadêmico Simplificado|_____________""") #toda informações contida entre 3 aspas SIMPLES
                                                                                         #é considerada como caracteres que devem ser ignorados.

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
    22 - Turma/Professor
    23 = Turma/Aluno
    24 - Semestre/Professor
    25 = Semestre/Aluno

    0  - Saí
    
''')

    return validar("Escolha uma opção: ",0,25) #retorna o valor das opções

          
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
        eliminação()
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
    elif opção==22:
        professor()
    elif opção==23:
        aluno()
    elif opção==24:
        semestre_turma()
    elif opção==25:
        semestre_alu()

