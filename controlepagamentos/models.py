from controlepagamentos import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_usuario(id_usuario):
    return User.query.get(int(id_usuario))


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String, nullable=False)
    token = db.Column(db.String(50))


class Pagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(30), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    forma_pagamento = db.Column(db.String(30), nullable=False)
    parcelas = db.Column(db.Integer, nullable=False)
    data_webhook = db.Column(db.DateTime, nullable=False)
    acesso_curso = db.Column(db.Boolean, default=False)
    mensagem_enviada = db.Column(db.Boolean, default=False)






