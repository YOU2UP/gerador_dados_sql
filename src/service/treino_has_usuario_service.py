import pandas as pd
import random
from datetime import datetime, timedelta

def gerar_inicio_treino():
    datas = []
    data_inicio = datetime(2023, 12, 10)
    data_fim = datetime(2023, 12, 31)
    total_dias = (data_fim - data_inicio).days
    for _ in range(50):
        range_days = random.randint(0, total_dias)
        data = data_inicio + timedelta(days=range_days)

        hora = random.randint(0, 23)
        minutos = random.randint(0, 59)
        segundos = random.randint(0, 59)
        
        data_hora = data.replace(hour=hora, minute=minutos, second=segundos)
        datas.append(data_hora.strftime("%Y-%m-%d %H:%M:%S"))
    return datas

def gerar_id_treino():
    ids_treinos = []
    for _ in range(50):
        index = random.randint(1, 50)
        ids_treinos.append(index)
    return ids_treinos

def gerar_id_usuario():
    ids_usuarios = []
    for _ in range(50):
        index = random.randint(1, 50)
        ids_usuarios.append(index)
    return ids_usuarios

def generate_data_frame(conteudos, datas, ids):
    df = pd.DataFrame(list(zip(conteudos, datas, ids)),
        columns =["inicio_treino", "treino_id_treino", "usuario_id_usuario"])
    return df

def run():
    datas = gerar_inicio_treino()
    ids_treinos = gerar_id_treino()
    ids_usuarios = gerar_id_usuario()

    df = generate_data_frame(datas, ids_treinos, ids_usuarios)
    print(df)
    return df