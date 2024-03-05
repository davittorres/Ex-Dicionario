alunos = {}

def add_aluno():
    nome = input('Digite o nome do aluno: ')
    matricula = input('Digite o numero da matricula: ')
    alunos[matricula] = nome
    print('Aluno {} adicionado com sucesso!'.format(nome))

def remov_aluno():
    matricula = input('Digite o numero da matricula do aluno que deseja remover: ')
    if matricula in alunos:
        nome = alunos.pop(matricula)
        print('Aluno {} removido com sucesso.'.format(nome))
    else:
        print('Aluno não encontrado')

def visu_aluno():
    if not alunos:
        print('Nenhum aluno registrado')
    else:
        print('Lista de alunos')
        for matricula, nome in alunos.items():
            print('Matricula: {}, Nome: {}.'.format(matricula, nome))

while True:
    print('Escolha uma opcao: ')
    print('Digite 1 para adcionar aluno')
    print('Digite 2 para remover aluno')
    print('Digite 3 para visualizar alunos')
    print('Digite 4 para sair')
    opcao = input('Digite a opcao desejada: ')
    
    if opcao == '1':
        add_aluno()
    elif opcao == '2':
        remov_aluno()   
    elif opcao == '3':
        visu_aluno()
    elif opcao == '4':
        print('Encerrado')
        break
    else:
        print('Digite uma opcao valida!!')
