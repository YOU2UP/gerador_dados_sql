from faker import Faker
import random
from datetime import datetime, timedelta
import pandas as pd

def get_faker_generator():
    faker = Faker("pt_BR")
    return faker

def gerar_datas_criacao():
    datas = []
    for _ in range(50):
        data = datetime.now()
        datas.append(data.strftime("%Y-%m-%d"))
    return datas

def gerar_datas_nascimento():
    datas = []
    data_inicio = datetime(1973, 1, 1)
    data_fim = datetime(2004, 12, 31)
    total_dias = (data_fim - data_inicio).days
    for _ in range(50):
        range_days = random.randint(0, total_dias)
        data = data_inicio + timedelta(days=range_days)
        datas.append(data.strftime("%Y-%m-%d"))
    return datas

def gerar_nomes(faker: Faker):
    nomes = []
    for _ in range(50):
        nome = faker.name()
        nomes.append(nome)
    return nomes

def gerar_descricao():
    descricoes = []
    possiveis = [
        "Entusiasta do Fitnes", 
        "Amante de Esportes", 
        "Atleta Profissional"
    ]
    for _ in range(50):
        index = random.randint(0, 2)
        descricao = possiveis[index]
        descricoes.append(descricao)
    return descricoes

def gerar_emails(nomes):
    emails = []
    for nome in nomes:
        email = nome.replace(" ", ".") + "@email.com"
        emails.append(email.lower())
    return emails

def gerar_estagios():
    estagios = []
    possiveis = [
        "Iniciante", 
        "Intermediário", 
        "Avançado"
    ]
    for _ in range(50):
        index = random.randint(0, 2)
        estagio = possiveis[index]
        estagios.append(estagio)
    return estagios

def gerar_metas():
    metas = []
    for _ in range(50):
        meta = random.randint(30, 90)

        if meta % 10 == 0:
            meta += 5
        else:
            meta = meta // 10 * 10

        metas.append(meta)
    return metas

def gerar_senhas():
    senhas = []
    for _ in range(50):
        senhas.append("$2a$10$0/TKTGxdREbWaWjWYhwf6e9P1fPOAMMNqEnZgOG95jnSkHSfkkIrC")
    return senhas

def gerar_locais():
    locais = []
    for _ in range(50):
        index = random.randint(1, 5)
        locais.append(index)
    return locais

def generate_data_frame(datas_criacao, datas_nascimento, descricoes, emails, 
                        estagios, metas, nomes, senhas, locais):
    df = pd.DataFrame(list(zip(datas_criacao, datas_nascimento, descricoes, emails, 
                               estagios, metas, nomes, senhas, locais)),
        columns =["data_criacao_conta", "data_nascimento", "descricao", "email", 
                  "estagio", "meta_treinos", "nome", "senha", "local_treino_id_local_treino"])
    return df

def run():
    faker = get_faker_generator()

    nomes = gerar_nomes(faker)
    datas_criacao = gerar_datas_criacao()
    datas_nascimento = gerar_datas_nascimento()    
    descricoes = gerar_descricao()    
    emails = gerar_emails(nomes)    
    estagios = gerar_estagios()
    metas = gerar_metas()
    senhas = gerar_senhas()
    locais = gerar_locais()

    df = generate_data_frame(datas_criacao, datas_nascimento, descricoes, emails, 
                             estagios, metas, nomes, senhas, locais)
    print(df)
    return df