from pandas import DataFrame

class LocalTreinoUsuario():
    def insert_data(self, engine, df:DataFrame):
        df.to_sql("local_treino_usuario", con=engine, index=False, if_exists='append')

class Usuario():
    def insert_data(self, engine, df:DataFrame):
        df.to_sql("usuario", con=engine, index=True, if_exists='append')

class Treino():
    def insert_data(self, engine, df:DataFrame):
        df.to_sql("treino", con=engine, index=True, if_exists='append')

class Avaliacao():
    def insert_data(self, engine, df:DataFrame):
        df.to_sql("avaliacao", con=engine, index=True, if_exists='append')

class Foto():
    def insert_data(self, engine, df:DataFrame):
        df.to_sql("foto", con=engine, index=True, if_exists='append')

class FotoPerfil():
    def insert_data(self, engine, df:DataFrame):
        df.to_sql("foto_perfil", con=engine, index=True, if_exists='append')

class TbMatch():
    def insert_data(self, engine, df:DataFrame):
        df.to_sql("tb_match", con=engine, index=True, if_exists='append')

class Notificacao():
    def insert_data(self, engine, df:DataFrame):
        df.to_sql("notificacao", con=engine, index=True, if_exists='append')

class TreinoHasUsuario():
    def insert_data(self, engine, df:DataFrame):
        df.to_sql("treino_has_usuario", con=engine, index=True, if_exists='append')