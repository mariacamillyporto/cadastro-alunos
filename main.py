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
    nome = input("Nome do aluno: ")
    alunos.append(nome)
    print("Aluno cadastrado.")

while True:
    print("\n--- CADASTRO DE ALUNOS ---")
    print("1 - Cadastrar")
    print("0 - Sair")
    opcao = input("Escolha: ")
    
    if opcao == "0":
        print("Programa encerrado.")
        break
    elif opcao == "1":
        cadastrar()
    else:
        print("Opcao invalida.")

alunos = []

def cadastrar():
    nome = input("Nome do aluno: ").strip()
    if nome == "":
        print("O nome não pode ficar vazio.")
        return
    for aluno in alunos:
        if aluno.lower() == nome.lower():
            print("Aluno já cadastrado.")
            return
    alunos.append(nome)
    print("Aluno cadastrado com sucesso!")

def listar():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    print("\n--- LISTA DE ALUNOS ---")
    for index, aluno in enumerate(alunos, 1):
        print(f"{index}. {aluno}")

while True:
    print("\n--- CADASTRO DE ALUNOS ---")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("0 - Sair")
    opcao = input("Escolha: ")
    
    if opcao == "0":
        print("Programa encerrado.")
        break
    elif opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    else:
        print("Opcao invalida.")


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
    print("Aluno cadastrado.")


def listar():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    print("\n--- ALUNOS ---")
    for numero, aluno in enumerate(alunos, start=1):
        print(f"{numero}. {aluno}")
    print(f"Total: {len(alunos)} aluno(s)")


while True:
    print("\n--- CADASTRO DE ALUNOS ---")
    print("1 - Cadastrar")
    print("2 - Listar")
    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "0":
        print("Programa encerrado.")
        break
    elif opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    else:
        print("Opcao invalida.")