from controlepagamentos import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)


class Pagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    forma_pagamento = db.Column(db.String(30), nullable=False)
    parcelas = db.Column(db.Integer, nullable=False)
    movimentacao = db.Column(db.DateTime)
    acesso_curso = db.Column(db.Boolean, default=False)
    mensagem_enviada = db.Column(db.Boolean, default=False)






