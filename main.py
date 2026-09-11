alunos = []

while True:
    print("\n--- CADASTRO DE ALUNOS ---")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opcao invalida")


alunos = []

def cadastrar():
    nome = input("Nome do aluno: ").strip()
    if nome == "":
        print("O nome nao pode ficar vazio.")
        return

    for aluno in alunos:
        if aluno.lower() == nome.lower():
            print("Aluno ja cadastrado.")
            return

    alunos.append(nome)
    print("Aluno cadastrado com sucesso.")

while True:
    print("\n--- CADASTRO DE ALUNOS ---")
    print("1 - Cadastrar")
    print("0 - Sair")
    
    opcao = input("Escolha: ").strip()
    
    if opcao == "0":
        print("Programa encerrado.")
        break
    elif opcao == "1":
        cadastrar()
    else:
        print("Opcao invalida.")