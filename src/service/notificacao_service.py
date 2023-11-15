import pandas as pd
import random
from datetime import datetime, timedelta

def gerar_conteudos():
    conteudos = []
    possiveis = [
        "Você recebeu uma mensagem",
        "Novo desafio disponível",
        "Parabéns! Você atingiu sua...",
        "Novo treino personalizado disponível",
        "Avalie seu último treino",
        "Desafio semanal: Corrida de...",
        "Atualize suas metas de treino",
        "Participe do torneio de esportes",
        "Convide amigos para treinar juntos"
    ]
    for _ in range(50):
        index = random.randint(0, 8)
        conteudo = possiveis[index]
        conteudos.append(conteudo)
    return conteudos

def gerar_data_hora():
    datas = []
    data_inicio = datetime(2023, 1, 1)
    data_fim = datetime(2023, 10, 31)
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

def gerar_id():
    ids = []
    for _ in range(50):
        index = random.randint(1, 50)
        ids.append(index)
    return ids

def generate_data_frame(conteudos, datas, ids):
    df = pd.DataFrame(list(zip(conteudos, datas, ids)),
        columns =["conteudo", "data_hora", "usuario_id_usuario"])
    return df

def run():
    conteudos = gerar_conteudos()
    datas = gerar_data_hora()
    ids = gerar_id()

    df = generate_data_frame(conteudos, datas, ids)
    print(df)
    return df