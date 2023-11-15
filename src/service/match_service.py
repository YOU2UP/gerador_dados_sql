import pandas as pd
import random
from datetime import datetime, timedelta

def gerar_datas_criacao():
    datas = []
    data_inicio = datetime(2023, 1, 1)
    data_fim = datetime(2023, 10, 31)
    total_dias = (data_fim - data_inicio).days
    for _ in range(50):
        range_days = random.randint(0, total_dias)
        data = data_inicio + timedelta(days=range_days)
        datas.append(data.strftime("%Y-%m-%d"))
    return datas

def gerar_ativos():
    ativos = []
    possiveis = [True, False]
    for _ in range(50):
        index = random.randint(0, 1)
        ativo = possiveis[index]
        ativos.append(ativo)
    return ativos

def gerar_id_1():
    ids_1 = []
    for _ in range(50):
        index = random.randint(1, 50)
        ids_1.append(index)
    return ids_1

def gerar_id_2():
    ids_2 = []
    for _ in range(50):
        index = random.randint(1, 50)
        ids_2.append(index)
    return ids_2

def generate_data_frame(datas, ativos, ids_1, ids_2):
    df = pd.DataFrame(list(zip(datas, ativos, ids_1, ids_2)),
        columns =["data_match", "is_ativo", "usuario1_id_usuario", "usuario2_id_usuario"])
    return df

def run():
    datas = gerar_datas_criacao()
    ativos = gerar_ativos()
    ids_1 = gerar_id_1()
    ids_2 = gerar_id_2()

    df = generate_data_frame(datas, ativos, ids_1, ids_2)
    print(df)
    return df