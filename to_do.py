import json
import os

arquivo_tarefas = "tarefas.json"

if not os.path.exists(arquivo_tarefas):
    with open(arquivo_tarefas, "w", encoding="utf-8") as f:
        json.dump([], f, ensure_ascii=False, indent=4)

def normalizar_tarefa(t):
    if "título" in t and "titulo" not in t:
        t["titulo"] = t.pop("título")
    if "concluída" in t and "concluida" not in t:
        t["concluida"] = t.pop("concluída")
    return t

def carregar_tarefas():
    global tarefas
    try:
        with open(arquivo_tarefas, "r", encoding="utf-8") as f:
            conteudo = f.read().strip()
            if not conteudo:
                tarefas = []
                return
            data = json.loads(conteudo)
            if not isinstance(data, list):
                tarefas = []
                return
            mudou = False
            for i, t in enumerate(data):
                antes = dict(t)
                data[i] = normalizar_tarefa(t)
                if data[i] != antes:
                    mudou = True
            tarefas = data
            if mudou:
                salvar_tarefas()
    except (FileNotFoundError, json.JSONDecodeError):
        tarefas = []

def salvar_tarefas():
    with open(arquivo_tarefas, "w", encoding="utf-8") as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

def adicionar_tarefa():
    titulo = input("Digite uma nova tarefa: ").strip()
    if titulo:
        tarefas.append({"titulo": titulo, "concluida": False})
        salvar_tarefas()
        print("Tarefa adicionada!")
    else:
        print("⚠ O título não pode ser vazio.")

def listar_tarefas():
    if not tarefas:
        print("\nNenhuma tarefa adicionada.\n")
        return
    print("\nTarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        status = "✔" if tarefa["concluida"] else "✘"
        print(f"{i}. {tarefa['titulo']} - {status}")
    print()

def marcar_concluida():
    listar_tarefas()
    if not tarefas:
        return
    try:
        num = int(input("Digite o número da tarefa a marcar como concluída: "))
        if 1 <= num <= len(tarefas):
            tarefas[num - 1]["concluida"] = True
            salvar_tarefas()
            print("Tarefa marcada como concluída!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

def remover_tarefa():
    listar_tarefas()
    if not tarefas:
        return
    try:
        num = int(input("Digite o número da tarefa a remover: "))
        if 1 <= num <= len(tarefas):
            removida = tarefas.pop(num - 1)
            salvar_tarefas()
            print(f"Tarefa '{removida['titulo']}' removida!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, digite um número válido.")

# === Programa principal ===

tarefas = []
carregar_tarefas()

while True:
    print("\n=== TO_DO LIST ===")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        marcar_concluida()
    elif opcao == "4":
        remover_tarefa()
    elif opcao == "5":
        print("Saindo... até mais! 👋")
        break
    else:
        print("Opção inválida, tente novamente.")
