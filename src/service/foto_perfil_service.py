import pandas as pd

def gerar_fotos_perfil():
    fotos = []
    for i in range(1, 51):
        link = "url" + str(i)
        fotos.append(link)
    return fotos 

def get_ids():
    ids = list(range(1, 51))
    return ids

def generate_data_frame(fotos, ids):
    df = pd.DataFrame(list(zip(fotos, ids)),
        columns =["url", "usuario_id_usuario"])
    return df

def run():
    fotos = gerar_fotos_perfil()
    ids = get_ids()

    df = generate_data_frame(fotos, ids)
    print(df)
    return df