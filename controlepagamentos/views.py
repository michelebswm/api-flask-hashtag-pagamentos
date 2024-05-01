from controlepagamentos import app, db, bcrypt
from flask import Flask, render_template, url_for, request, flash, redirect
from flask_login import login_user, logout_user, current_user, login_required
from controlepagamentos.models import User
from controlepagamentos.forms import FormLogin, FormCriarUser

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    form_criaruser = FormCriarUser()
    if form_criaruser.validate_on_submit() and 'btn_cadastro' in request.form:
        if form_criaruser.token.data != app.config['TOKEN_CREATE']:
            flash("Token de cadastro inválido.", "alert-danger")
            return redirect(url_for('cadastro'))

        senha_cript = bcrypt.generate_password_hash(form_criaruser.senha.data).decode('utf-8')

        usuario = User()
        usuario.nome = form_criaruser.nome.data
        usuario.email = form_criaruser.email.data
        usuario.senha = senha_cript
        usuario.token = form_criaruser.token.data

        db.session.add(usuario)
        db.session.commit()

        flash(f'Conta criada com sucesso para o e-mail: {form_criaruser.email.data}', 'alert-success')
        return redirect(url_for('index'))
    return render_template("cadastro.html", form_criaruser=form_criaruser)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit() and 'btn_login' in request.form:
        user = User.query.filter_by(email=form_login.email.data).first()
        print(bcrypt.check_password_hash(user.senha, form_login.senha.data))
        if user and bcrypt.check_password_hash(user.senha, form_login.senha.data):
            login_user(user, remember=form_login.lembrar_dados.data)
            flash(f'Login realizado com sucesso no e-mail: {form_login.email.data}', 'alert-success')
            return redirect(url_for('index'))
        flash(f'Falha no Login E-mail ou senha incorretos!', 'alert-danger')
    return render_template("login.html", form_login=form_login)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout realizado com sucesso!', 'alert-success')
    return redirect(url_for('login'))
