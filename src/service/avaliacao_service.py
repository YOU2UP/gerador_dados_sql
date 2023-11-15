import random
import pandas as pd

def gerar_notas():
    notas = []
    for _ in range(50):
        index = random.uniform(3, 5)
        notas.append(round(index, 1))
    return notas

def gerar_avaliados():
    avaliados = []
    for _ in range(50):
        index = random.randint(1, 50)
        avaliados.append(index)
    return avaliados

def gerar_avaliadores():
    avaliadores = []
    for _ in range(50):
        index = random.randint(1, 50)
        avaliadores.append(index)
    return avaliadores

def gerar_treinos():
    treinos = []
    for _ in range(50):
        index = random.randint(1, 5)
        treinos.append(index)
    return treinos

def generate_data_frame(notas, avaliados, avaliadores, treinos):
    df = pd.DataFrame(list(zip(notas, avaliados, avaliadores, treinos)),
        columns =["nota", "avaliado_id_usuario", "avaliador_id_usuario", "treino_id_treino"])
    return df

def run():
    notas = gerar_notas()
    avaliados = gerar_avaliados()
    avaliadores = gerar_avaliadores()
    treinos = gerar_treinos()
    df = generate_data_frame(notas, avaliados, avaliadores, treinos)
    print(df)
    return df