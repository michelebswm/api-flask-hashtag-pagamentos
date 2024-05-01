from controlepagamentos import app, db, bcrypt
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_login import login_user
from controlepagamentos.forms import FormLogin, FormCriarUser
from controlepagamentos.models import User


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    return render_template("home.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit() and 'btn_login' in request.form:
        user = User.query.filter_by(email=form_login.email.data).first()
        if user and bcrypt.check_password_hash(user.senha, form_login.senha.data):
            login_user(user, remember=form_login.lembrar_dados.data)
            flash(f'Login realizado com sucesso no e-mail: {form_login.email.data}', 'alert-success')
            return redirect(url_for('index'))
        flash(f'Falha no Login E-mail ou senha incorretos!', 'alert-danger')
    return render_template("login.html", form_login=form_login)

