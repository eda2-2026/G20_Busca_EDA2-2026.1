#busca sequencial
def filtrar_exercicios(lista, tamanho, grupo, tempo_max, dificuldade_max):
    resultado = []

    i = 0
    while i < tamanho:
        elemento = lista[i]

        if (elemento.grupo == grupo and
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

    return None  # ou o índice, mas para simplicidade, None se não encontrado


def busca_binaria(lista, tamanho, nome):
    esquerda = 0
    direita = tamanho - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        elemento = lista[meio]

        if elemento.nome == nome:
            return elemento
        elif elemento.nome < nome:
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