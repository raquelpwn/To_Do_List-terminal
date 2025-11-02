import json

tarefas = []

def salvar_tarefas():
    with open("tarefas.json", "w", encoding = "utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

def carregar_tarefas():
    global tarefas
    try:
        with open("tarefas.json", "r", encoding = "utf-8") as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        tarefas = []        

def mostrar_menu():
    print("\n=== TO_DO LIST ===")
    print("1. Adicionar tarefa\n2. Listar tarefas\n3. Marcar tarefa como concluída\n4. Remover tarefa\n5. Sair")

def listar_tarefas():
    if not tarefas:
        print("\nNenhuma tarefa adicionada")
        return
    print("\nTarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✔" if tarefa["concluída"] else "✘"
        print(f"{i}. {tarefa['título']}- {status}")
        
def adicionar_tarefa():
    titulo = input("Digite uma nova tarefa: ").strip()
    if titulo:
        tarefas.append({"título": titulo, "concluída": False})
        salvar_tarefas()
        print("Tarefa adicionada!")
    else:
        print("Título não pode ser vazio.")        

def marcar_concluída():
    listar_tarefas()
    if not tarefas:
        return
    try: 
        num = int(input("Digite o número da tarefa"))
        tarefas[num - 1]["concluída"] = True
        salvar_tarefas
        print("Tarefa concluída!")
    except (ValueError, IndexError):
        print("Número inválido.")

def remover_tarefa():
    listar_tarefas()
    if not tarefas:
        return
    try:
        num = int(input("Digite a tarefa que quer remover: "))
        removida = tarefas.pop(num - 1)
        salvar_tarefas()
        print(f"Tarefa '{removida['titulo']}' removida!")
    except (ValueError, IndexError):
        print("Número inválido.")

carregar_tarefas()        

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ").strip()
    if escolha == "1":
        adicionar_tarefa()
    elif escolha == "2":
        listar_tarefas()
    elif escolha == "3":
        marcar_concluída()
    elif escolha == "4":
        remover_tarefa()
    elif escolha == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")        