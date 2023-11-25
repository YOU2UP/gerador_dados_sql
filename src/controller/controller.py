from pandas import DataFrame
from sqlalchemy.orm import Session

class Treino():
    def insert_data(self, engine, df:DataFrame):
        df.to_sql("treino", con=engine, index=False, if_exists='append')

class LocalTreinoUsuario():
    def insert_data(self, engine, df:DataFrame):
        df.to_sql("local_treino_usuario", con=engine, index=False, if_exists='append')

class Usuario():
    def insert_data(self, engine, df:DataFrame):
        df.to_sql("usuario", con=engine, index=False, if_exists='append')

    def update_user_id_perfil(self, db:Session):
        for index in range(1, 51):
            query = f"UPDATE usuario SET foto_perfil_id_foto_perfil = {index} WHERE id_usuario = {index};"
            db.execute(query)
            db.commit()

class Notificacao():
    def insert_data(self, engine, df:DataFrame):
        df.to_sql("notificacao", con=engine, index=False, if_exists='append')

class TreinoHasUsuario():
    def insert_data(self, engine, df:DataFrame):
        df.to_sql("treino_has_usuario", con=engine, index=False, if_exists='append')

class Avaliacao():
    def insert_data(self, engine, df:DataFrame):
        df.to_sql("avaliacao", con=engine, index=False, if_exists='append')

class Foto():
    def insert_data(self, engine, df:DataFrame):
        df.to_sql("foto", con=engine, index=False, if_exists='append')

    def update_varchar(self, db:Session):
        query = "alter table foto modify column url varchar(1000);"
        db.execute(query)
        db.commit()

class FotoPerfil():
    def insert_data(self, engine, df:DataFrame):
        df.to_sql("foto_perfil", con=engine, index=False, if_exists='append')

    def update_varchar(self, db:Session):
        query = "alter table foto_perfil modify column url varchar(1000);"
        db.execute(query)
        db.commit()