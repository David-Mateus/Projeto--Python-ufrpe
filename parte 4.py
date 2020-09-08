Sistema = []
def codigo_turma():
    return(input("Codigo da turma: "))
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
def exploração(turma):
    nome = turma.lower()
    for d, e in enumerate(Sistema):
        if e[0].lower() == nome:
            return d
        return None
def gerar():
    global Sistema
    turma = codigo_turma()
    periodo = periodo_ufrpe()
    disciplina = codigo_disciplina()
    cpfpro = cpf_professor()
    cpfalu = cpf_aluno()
    Sistema.append([turma, periodo_ufrpe, disciplina, cpfpro, cpfalu])
def fim():
    global Sistema
    turma = codigo_turma()
    p = exploração(turma)
    if p != None:
        del Sistema[p]
    else:
        print("Nome não encontrado")
def renovar():
    p = exploração(codigo_turma())
    if p != None:
        turma = [p][0]
        periodo = Sistema [p][1]
        disciplina = Sistema[p][2]
        cpfpro = Sistema[p][3]
        cpfalu = Sistema[p][4]
        print("Econtrado: ")
        exibir_dados(turma, periodo_ufrpe, disciplina, cpfpro, cpfalu)
        turma = codigo_turma()
        periodo = periodo_ufrpe()
        disciplina = codigo_disciplina()
        cpfpro = cpf_professor()
        cpfalu = cpf_aluno()
        Sistema[p] = [turma, periodo_ufrpe, disciplina, cpfpro, cpfalu]
    else:
        print("Nome não encontrado.")

def exame():
    print("\nSistema\n\n___________________________________________")
    for e in Sistema:
        exibir_dados(e[0], e[1], e[2], e[3], e[4])
    print("__________________________________________\n")

def memorizar():
     nomearquivo = nome_do_arquivo()
     arquivo = open(nomearquivo, "w", encoding = "utf-8")
     for e in Sistema:
         arquivo.write("%s#%s#%s#%s#%s\n" % (e[0], e[1], e[2], e[3], e[4]))
     arquivo.close()
def aluno():
    print()
    for e in Sistema:
        exibir_dados(e[0], e[1], e[2], e[3], e[4])
    print('________________________________________________')
    
    


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
    TURMA POR ALUNO
    6 - Aluno
    
    0 - Sair
''')

    return validar("Escolha uma opção: ",1,6) #retorna o valor da opção

while True:
    opção = menu()
    if opção == 0:
        break
    elif opção == 1:
        gerar()
    elif opção == 2:
        renovar()
    elif opção == 3:
        exame()
    elif opção == 4:
        fim()
    elif opção == 5:
        memorizar()
    elif opção == 6:
        aluno()

    

        

        

    
