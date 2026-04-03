class Exercicio:
    def __init__(self, nome, grupo, tempo, nivel, cargas):
        self.nome = nome
        self.grupo = grupo
        self.tempo = tempo
        self.nivel = nivel
        self.cargas = []


class Treino:
    def __init__(self,nome):
        self.nome = nome
        self.exercicios = []
        self.tempo_max = 0
    
    def adicionar_exercicio(self, exercicio):
        self.exercicios.append(exercicio)
        self.tempo_max += exercicio.tempo
        

class Usuario:
    def __init__(self,nome):
        self.nome = nome
        self.historico = []
