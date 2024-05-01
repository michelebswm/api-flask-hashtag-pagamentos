import smtplib

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from email_validator import validate_email
from controlepagamentos.models import User


class FormCriarUser(FlaskForm):
    nome = StringField("Nome", validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirmação de Senha', validators=[DataRequired(), EqualTo('senha')])
    token = StringField('Token', validators=[DataRequired()])
    btn_cadastro = SubmitField('Criar Conta')

    def validate_email(self, email):
        try:
            # Use validate_email from email_validator for advanced checks
            validate_email(email.data)
        except (ValueError, smtplib.SMTPException) as e:
            raise ValidationError(f"E-mail inválido: {str(e)}")

        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("E-mail já cadastrado")


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_dados = BooleanField('Lembrar dados de acesso')
    btn_login = SubmitField('Acessar')
