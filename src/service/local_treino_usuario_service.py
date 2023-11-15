import random
import pandas as pd
from pandas import DataFrame

class Endereco:
    def __init__(self, bairro, cidade, is_academia, nome, rua, numero, uf) -> None:
        self.bairro = bairro
        self.cidade = cidade
        self.is_academia = is_academia
        self.nome = nome
        self.rua = rua
        self.numero = numero
        self.uf = uf

def mount_enderecos():
    enderecos = [
        ["Vila Mariana", "São Paulo", False, "Parque do Ibirapuera", "Av. Pedro Álvares Cabral", "230", "SP"],
        ["Santa Paula", "São Caetano do Sul", True, "Academia 1", "Rua Oswaldo Cruz", "141", "SP"],
        ["Montanhão", "São Bernardo do Campo", False, "Praça Pedro Afonso", "Rua Bamburral", "565", "SP"],
        ["Bosque da Saúde", "São Paulo", True, "Academia 2", "Rua Izar", "102", "SP"],
        ["Rua Nova York 499", "Brooklin Paulista", True, "Smart Fit", "Rua Nova York", "499", "SP"]
    ]
    return enderecos

def make_objects(enderecos, df:DataFrame): 
    for _ in range(50):
        index = random.randint(0, 4)
        escolhido = enderecos[index] 
        endereco = Endereco(escolhido[0], escolhido[1], escolhido[2], escolhido[3], 
                            escolhido[4], escolhido[5], escolhido[6])
        df = fill_df(df, endereco)

def fill_df(df:DataFrame, endereco):
    lista = [endereco.bairro, endereco.cidade, endereco.is_academia, endereco.nome, 
             endereco.rua, endereco.numero, endereco.uf]
    df.loc[len(df)] = lista
    return df

def run():
    enderecos = mount_enderecos()
    df = pd.DataFrame(columns=["bairro", "cidade", "is_academia", "nome", "numero", "rua", "uf"])
    make_objects(enderecos, df)
    print(df)
    return df