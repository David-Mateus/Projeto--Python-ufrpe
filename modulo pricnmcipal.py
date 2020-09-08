import programa 
#PROFESSSOR
programa.pede_nome()
programa.pede_cpf()
programa.pede_departamento()
programa.semestre_pro()
programa.pede_nome_arquivo()
programa.mostra_dados()

#DISCIPLINA
programa.nome_pede()
programa.pede_codigo()
programa.nome_arquivo()
programa.mostra_codigo()

#ALUNO
programa.nome_aluno()
programa.cpf_aluno()
programa.semestre()
programa.mostra_fatos()
programa.arquivo_alu()

#TURMA
programa.codigo_turma()
programa.periodo_ufrpe()
programa.codigo_disciplina()
programa.cpf_professor()
programa.cpf_aluno()
programa.nome_do_arquivo()
programa.exibir_dados

#Pesquisa do Professor
programa.pesquisa(nome)
#Disciplina
programa.procurar(nome)
#Aluno
programa.buscar(nome)
#Turma
programa.exploração(turma)

#Criação de Professor
programa.criação()
#Criação de disciplina
programa.origem()
#CriaçãoAliuno
programa.formar()
#Criação turma
programa.gerar()

#Destruição do professor
programa.destruição()
#Destruição Disciplina
programa.demolição()
#Destruição aluno
programa.eliminação()
#Destruição turma
programa.fim()

#Atualizar professor
programa.atualizar()
#Atualizar disciplina
programa.atual()
#Atualizar aluno
programa.inovar()
#Atualizar turma
programa.renovar()

#Consulta prof
programa.consulta()
#consulta disciplina
programa.pedir()
#consulta aluno
programa.informa()
#consulta turma
programa.exame()

#Grava professor
programa.grava()
#Grava disciplina
programa.decorar()
#Grava aluno
programa.fixar()
#Grava turma
programa.memorizar()

#_______ATA de Exercicio________|
programa.relatorio()

#____Todas as turmas por professor____|
programa.professor()

#_______Turmas por Semestre_______|
programa.semestre_turma()

#______Lista de turmas por aluno______|
programa.aluno()

#______Turma por Semestre______|
programa.semestre_alu

#Validar
programa.validar(pergunta, inicio, fim)

#MENU
#programa.menu()
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







