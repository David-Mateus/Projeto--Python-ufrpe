def professor():
    print("""____________|Todas as turmas por professor|______________""")
    print()
    for e in Sistema:
        mostra_dados(e[0]+'\n',e[1]+'\n',e[2]+'\n')
    print("==========================================================")
    print()
    for v in Alu:
        mostra_fatos(v[0]+'\n', v[1]+'\n')
    print('==========================================================')
    print()
    for a in Dis:
        mostra_codigo(a[0]+'\n',a[1]+'\n')
    print('==========================================================')
    print()
    
    for i in Tur:
        exibir_dados(i[0]+'\n' ,i[1], i[2]+'\n',i[3], i[4])
    print('==========================================================')

turmas por semestre
def semestre_pro():
    return(input("Professor de que semestre: "))

def semestre():
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
        exibir_dados(i[0]+'\n' ,i[1], i[2]+'\n',i[3], i[4]+'\n',i[5])
    print('==========================================================')



Lista de turmas por aluno
def aluno():
    print('''____________|Lista de turmas por aluno|____________''')
    print()
    for v in Alu:
        mostra_fatos(v[0]+'\n', v[1]+'\n')
    print('==========================================================')
    print()
     for e in Sistema:
        mostra_dados(e[0]+'\n',e[1]+'\n',e[2]+'\n')
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
        mostra_fatos(v[0]+'\n', v[1]+'\n',v[3])
    print('==========================================================')
    print()
    for a in Dis:
        mostra_codigo(a[0]+'\n',a[1]+'\n')
    print('==========================================================')
    print()
    
    for i in Tur:
        exibir_dados(i[0]+'\n' ,i[1], i[2]+'\n',i[3], i[4]+'\n',i[5])
    print('==========================================================')
