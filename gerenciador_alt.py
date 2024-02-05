print("\nMenu do Gerenciador de Lista de Tarefas")

tarefas = ("1. Adicionar tarefa", "2. Ver tarefa", "3. Atualizar tarefa", "4. Completar tarefa", "5. Deletar tarefas completadas", "6. Sair")

for elementos in tarefas:
    print(elementos)

escolha = input("Digite a sua escolha: ")

while escolha != "6":
    for elementos in tarefas:
        print(elementos)
    escolha = input("Digite a sua escolha: ")

if escolha == "6":
    print("Programa finalizado")

