import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from modelos import Exercicio
from data import lista_exercicios as default_exercicios
from algoritmos import (
    filtrar_exercicios,
    busca_binaria,
    busca_binaria_por_tempo,
    construir_tabela_hash_por_nome,
    busca_hash_por_nome,
)

STORAGE_PATH = os.path.join(os.path.dirname(__file__), "exercicios.json")


def exercicio_to_dict(exercicio):
    return {
        "nome": exercicio.nome,
        "grupo": exercicio.grupo,
        "tempo": exercicio.tempo,
        "nivel": exercicio.nivel,
        "cargas": exercicio.cargas,
    }


def dict_to_exercicio(d):
    return Exercicio(d["nome"], d["grupo"], d["tempo"], d["nivel"], d.get("cargas", []))


def carregar_exercicios():
    if os.path.exists(STORAGE_PATH):
        with open(STORAGE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [dict_to_exercicio(item) for item in data]

    salvar_exercicios(default_exercicios)
    return list(default_exercicios)


def salvar_exercicios(exercicios):
    with open(STORAGE_PATH, "w", encoding="utf-8") as f:
        json.dump([exercicio_to_dict(e) for e in exercicios], f, ensure_ascii=False, indent=2)


def adicionar_exercicio(exercicios):
    nome = input("Nome do exercício: ").strip()
    if not nome:
        print("Nome não pode ser vazio.\n")
        return

    grupo = input("Grupo (peito, costas, perna, ombro, etc): ").strip()
    if not grupo:
        print("Grupo não pode ser vazio.\n")
        return

    try:
        tempo = int(input("Duração (min): ").strip())
        if tempo <= 0:
            raise ValueError
    except ValueError:
        print("Duração deve ser um número inteiro positivo.\n")
        return

    try:
        nivel = int(input("Nível de dificuldade (1-5): ").strip())
        if not 1 <= nivel <= 5:
            raise ValueError
    except ValueError:
        print("Nível deve ser um número inteiro entre 1 e 5.\n")
        return

    cargas_input = input("Cargas (separadas por vírgula, ex: 10kg,12kg ou vazio): ").strip()
    cargas = [c.strip() for c in cargas_input.split(",") if c.strip()] if cargas_input else []

    nova = Exercicio(nome, grupo, tempo, nivel, cargas)
    exercicios.append(nova)
    salvar_exercicios(exercicios)
    print(f"Exercício '{nome}' adicionado e salvo com sucesso!\n")


def listar_exercicios(exercicios):
    if not exercicios:
        print("Nenhum exercício cadastrado.\n")
        return

    print("=== Exercícios cadastrados ===")
    for e in exercicios:
        print(f"{e.nome} | {e.grupo} | {e.tempo} min | nível {e.nivel}")
    print()


def busca_sequencial_por_nome(exercicios, nome):
    for e in exercicios:
        if e.nome.lower() == nome.lower():
            return e
    return None


def editar_exercicio(exercicios):
    nome = input("Nome do exercício a editar: ").strip()
    exercicio = busca_sequencial_por_nome(exercicios, nome)
    if not exercicio:
        print("Exercício não encontrado.\n")
        return

    print(f"Editando: {exercicio.nome} | {exercicio.grupo} | {exercicio.tempo} min | nível {exercicio.nivel}")
    print("Deixe em branco para manter o valor atual.")

    novo_nome = input(f"Novo nome ({exercicio.nome}): ").strip() or exercicio.nome
    novo_grupo = input(f"Novo grupo ({exercicio.grupo}): ").strip() or exercicio.grupo

    try:
        novo_tempo_str = input(f"Nova duração ({exercicio.tempo}): ").strip()
        novo_tempo = int(novo_tempo_str) if novo_tempo_str else exercicio.tempo
        if novo_tempo <= 0:
            raise ValueError
    except ValueError:
        print("Duração deve ser um número inteiro positivo.\n")
        return

    try:
        novo_nivel_str = input(f"Novo nível ({exercicio.nivel}): ").strip()
        novo_nivel = int(novo_nivel_str) if novo_nivel_str else exercicio.nivel
        if not 1 <= novo_nivel <= 5:
            raise ValueError
    except ValueError:
        print("Nível deve ser um número inteiro entre 1 e 5.\n")
        return

    cargas_input = input(f"Novas cargas ({', '.join(exercicio.cargas) or 'vazio'}): ").strip()
    novas_cargas = [c.strip() for c in cargas_input.split(",") if c.strip()] if cargas_input else exercicio.cargas

    exercicio.nome = novo_nome
    exercicio.grupo = novo_grupo
    exercicio.tempo = novo_tempo
    exercicio.nivel = novo_nivel
    exercicio.cargas = novas_cargas

    salvar_exercicios(exercicios)
    print(f"Exercício '{novo_nome}' editado e salvo com sucesso!\n")


def remover_exercicio(exercicios):
    nome = input("Nome do exercício a remover: ").strip()
    exercicio = busca_sequencial_por_nome(exercicios, nome)
    if not exercicio:
        print("Exercício não encontrado.\n")
        return

    exercicios.remove(exercicio)
    salvar_exercicios(exercicios)
    print(f"Exercício '{nome}' removido com sucesso!\n")


def filtrar_customizado(exercicios):
    grupo = input("Grupo para filtrar (ou vazio para todos): ").strip()
    try:
        tempo_max_str = input("Tempo máximo (min, ou vazio para ilimitado): ").strip()
        tempo_max = int(tempo_max_str) if tempo_max_str else float('inf')
        if tempo_max <= 0:
            raise ValueError
    except ValueError:
        print("Tempo máximo deve ser um número inteiro positivo.\n")
        return

    try:
        dificuldade_max_str = input("Nível máximo (1-5, ou vazio para ilimitado): ").strip()
        dificuldade_max = int(dificuldade_max_str) if dificuldade_max_str else 5
        if not 1 <= dificuldade_max <= 5:
            raise ValueError
    except ValueError:
        print("Nível máximo deve ser um número inteiro entre 1 e 5.\n")
        return

    filtrados = filtrar_exercicios(exercicios, len(exercicios), grupo, tempo_max, dificuldade_max)
    print("=== Exercícios filtrados ===")
    if not filtrados:
        print("Nenhum exercício encontrado com os critérios.\n")
    else:
        for e in filtrados:
            print(e.nome, "|", e.grupo, "|", e.tempo, "min", "| nível", e.nivel)
        print()


def busca_por_nome(exercicios):
    nome = input("Nome do exercício para busca binária: ").strip()
    ordenados = sorted(exercicios, key=lambda x: x.nome)
    resultado = busca_binaria(ordenados, len(ordenados), nome)

    if resultado and resultado.nome == nome:
        print("Encontrado:", resultado.nome, "|", resultado.grupo, "|", resultado.tempo, "min", "| nível", resultado.nivel)
    else:
        print("Exercício não encontrado.")
    print()


def busca_por_nome_hash(exercicios):
    nome = input("Nome do exercício para busca (tabela hash): ").strip()
    tabela = construir_tabela_hash_por_nome(exercicios)
    resultado = busca_hash_por_nome(tabela, nome)

    if resultado:
        print("Encontrado:", resultado.nome, "|", resultado.grupo, "|", resultado.tempo, "min", "| nível", resultado.nivel)
    else:
        print("Exercício não encontrado.")
    print()


def busca_por_tempo(exercicios):
    try:
        tempo = int(input("Tempo do exercício para busca binária: ").strip())
    except ValueError:
        print("Tempo deve ser um número inteiro.\n")
        return

    ordenados = sorted(exercicios, key=lambda x: x.tempo)
    resultado = busca_binaria_por_tempo(ordenados, len(ordenados), tempo)

    if resultado:
        print("Encontrado:", resultado.nome, "|", resultado.grupo, "|", resultado.tempo, "min", "| nível", resultado.nivel)
    else:
        print("Exercício com tempo exato não encontrado.")
    print()


def main():
    exercicios = carregar_exercicios()

    while True:
        print("1) Listar exercícios")
        print("2) Adicionar exercício")
        print("3) Buscar exercício por nome (tabela hash)")
        print("4) Buscar exercício por nome (busca binária)")
        print("5) Buscar exercício por tempo (busca binária)")
        print("6) Editar exercício")
        print("7) Remover exercício")
        print("8) Filtrar customizado")
        print("9) Sair")

        opc = input("Escolha uma opção: ").strip()
        print()

        if opc == "1":
            listar_exercicios(exercicios)
        elif opc == "2":
            adicionar_exercicio(exercicios)
        elif opc == "3":
            busca_por_nome_hash(exercicios)
        elif opc == "4":
            busca_por_nome(exercicios)
        elif opc == "5":
            busca_por_tempo(exercicios)
        elif opc == "6":
            editar_exercicio(exercicios)
        elif opc == "7":
            remover_exercicio(exercicios)
        elif opc == "8":
            filtrar_customizado(exercicios)
        elif opc == "9":
            break
        else:
            print("Opção inválida. Tente novamente.\n")


if __name__ == "__main__":
    main()