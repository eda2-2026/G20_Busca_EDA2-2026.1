def filtrar_exercicios(lista, tamanho, grupo, tempo_max, dificuldade_max):
    resultado = []
    grupo_lower = grupo.lower() if grupo else None

    i = 0
    while i < tamanho:
        elemento = lista[i]
        grupo_valido = True

        if grupo_lower:
            grupo_valido = elemento.grupo.lower() == grupo_lower

        if (grupo_valido and
            elemento.tempo <= tempo_max and
            elemento.nivel <= dificuldade_max):

            resultado.append(elemento)

        i += 1

    return resultado


def busca_binaria_por_tempo(lista, tamanho, tempo):
    esquerda = 0
    direita = tamanho - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        elemento = lista[meio]

        if elemento.tempo == tempo:
            return elemento
        elif elemento.tempo < tempo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return None  


def busca_binaria(lista, tamanho, nome):
    nome_lower = nome.lower()
    esquerda = 0
    direita = tamanho - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        elemento = lista[meio]
        elemento_nome_lower = elemento.nome.lower()

        if elemento_nome_lower == nome_lower:
            return elemento
        elif elemento_nome_lower < nome_lower:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return None


def construir_tabela_hash_por_nome(lista):
    tabela = {}

    i = 0
    tamanho = len(lista)
    while i < tamanho:
        elemento = lista[i]
        chave = elemento.nome.lower()
        tabela[chave] = elemento
        i += 1

    return tabela


def busca_hash_por_nome(tabela, nome):
    chave = nome.lower()
    return tabela.get(chave)