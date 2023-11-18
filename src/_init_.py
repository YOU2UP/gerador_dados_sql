from infrastructure import conection_db

from service import (
    user_service, 
    treino_service,
    local_treino_usuario_service,
    avaliacao_service,
    foto_service,
    foto_perfil_service,
    notificacao_service,
    treino_has_usuario_service
)


from controller import (
    controller
)

def start():
    engine, db = conection_db.conect()

    locais = local_treino_usuario_service.run()
    local_db = controller.LocalTreinoUsuario()
    local_db.insert_data(engine, locais)

    usuarios = user_service.run()
    usuario_db = controller.Usuario()
    usuario_db.insert_data(engine, usuarios)

    treinos, realizados = treino_service.run()
    treino_db = controller.Treino()
    treino_db.insert_data(engine, treinos)

    avaliacoes = avaliacao_service.run(realizados)
    avaliacao_db = controller.Avaliacao()
    avaliacao_db.insert_data(engine, avaliacoes)

    fotos = foto_service.run()
    foto_db = controller.Foto()
    foto_db.insert_data(engine, fotos)

    fotos_perfil = foto_perfil_service.run()
    foto_perfil_db = controller.FotoPerfil()
    foto_perfil_db.insert_data(engine, fotos_perfil)
    
    notificacoes = notificacao_service.run()
    notificacao_db = controller.Notificacao()
    notificacao_db.insert_data(engine, notificacoes)

    treinos_usuarios = treino_has_usuario_service.run()
    treino_usuario_db = controller.TreinoHasUsuario()
    treino_usuario_db.insert_data(engine, treinos_usuarios)

    usuario_db.update_user_id_perfil(db)

start()