from modelos import *

supino = Exercicio("Supino", "peito", 30, 2, [])
crucifixo = Exercicio("Crucifixo", "peito", 20, 2, [])
triceps = Exercicio("Tríceps Testa", "triceps", 20, 2, [])

remada = Exercicio("Remada", "costas", 30, 2, [])
puxada = Exercicio("Puxada na Barra", "costas", 25, 2, [])
biceps = Exercicio("Rosca Bíceps", "biceps", 20, 1, [])

agachamento = Exercicio("Agachamento", "perna", 40, 3, [])
legpress = Exercicio("Leg Press", "perna", 35, 2, [])
panturrilha = Exercicio("Panturrilha", "perna", 15, 1, [])

ombro = Exercicio("Desenvolvimento", "ombro", 25, 2, [])
elevacao = Exercicio("Elevação Lateral", "ombro", 20, 1, [])

lista_exercicios = [
    supino,
    crucifixo,
    triceps,
    remada,
    puxada,
    biceps,
    agachamento,
    legpress,
    panturrilha,
    ombro,
    elevacao
]
