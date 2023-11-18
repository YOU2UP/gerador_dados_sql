import random
import pandas as pd

def get_realizados(treinos_realizados:list):
    id_realizado = []
    for index, value in enumerate(treinos_realizados):
        if value == 1:
            id_realizado.append(index + 1)
    return id_realizado

def gerar_notas(ids_realizados: list):
    notas = []
    for _ in ids_realizados:
        index = random.uniform(3, 5)
        notas.append(round(index, 1))
    return notas

def gerar_avaliados(ids_realizados: list):
    avaliados = []
    for _ in ids_realizados:
        index = random.randint(1, 50)
        avaliados.append(index)
    return avaliados

def gerar_avaliadores(ids_realizados: list):
    avaliadores = []
    for _ in ids_realizados:
        index = random.randint(1, 50)
        avaliadores.append(index)
    return avaliadores

def gerar_treinos(ids_realizados: list):
    treinos = []
    for index in ids_realizados:
        treinos.append(index)
    return treinos

def generate_data_frame(notas, avaliados, avaliadores, treinos):
    df = pd.DataFrame(list(zip(notas, avaliados, avaliadores, treinos)),
        columns =["nota", "avaliado_id_usuario", "avaliador_id_usuario", "treino_id_treino"])
    return df

def run(treinos_realizados:list):
    ids_realizados = get_realizados(treinos_realizados)
    notas = gerar_notas(ids_realizados)
    avaliados = gerar_avaliados(ids_realizados)
    avaliadores = gerar_avaliadores(ids_realizados)
    treinos = gerar_treinos(ids_realizados)
    df = generate_data_frame(notas, avaliados, avaliadores, treinos)
    print(df)
    return df