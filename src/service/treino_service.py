import random
import pandas as pd

def gerar_realizado():
    dados = []
    possiveis = [True, False]
    for _ in range(50):
        index = random.randint(0, 1)
        is_realizado = possiveis[index]
        dados.append(is_realizado)
    return dados

def gerar_periodo():
    periodos = []
    possiveis = ["Manhã", "Tarde", "Noite"]
    for _ in range(50):
        index = random.randint(0, 2)
        periodo = possiveis[index]
        periodos.append(periodo)
    return periodos

def generate_data_frame(realizado, periodo):
    df = pd.DataFrame(list(zip(realizado, periodo)),
        columns =["is_realizado", "periodo"])
    return df

def run():
    realizado = gerar_realizado()
    periodo = gerar_periodo()

    df = generate_data_frame(realizado, periodo)
    print(df)
    return df, realizado