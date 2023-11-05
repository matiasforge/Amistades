class User:
    def __init__(self, id, nombre, apellido):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido

class Friendship:
    def __init__(self, id, fecha_creacion, fecha_actualizacion):
        self.id = id
        self.fecha_creacion = fecha_creacion
        self.fecha_actualizacion = fecha_actualizacion

class UserFriend:
    def __init__(self, id, user_id, friend_id, fecha_creacion, fecha_actualizacion):
        self.id = id
        self.user_id = user_id
        self.friend_id = friend_id
        self.fecha_creacion = fecha_creacion
        self.fecha_actualizacion = fecha_actualizacion
