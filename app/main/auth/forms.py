# -*- coding:utf-8 -*-
from app import db
from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import Email, Length, DataRequired, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(message=u"I forgot to fill in this item!"), Length(1, 64), Email(message=u"Are you sure this is this Email ?")])
    password = PasswordField(u'password', validators=[DataRequired(message=u"I forgot to fill in this item!"), Length(6, 32)])
    remember_me = BooleanField(u"Keep me logged in", default=True)
    submit = SubmitField(u'sign in')


class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(message=u"I forgot to fill in this item!"), Length(1, 64), Email(message=u"Are you sure this is this  Email ?")])
    name = StringField(u'username', validators=[DataRequired(message=u"I forgot to fill in this item!"), Length(1, 64)])
    password = PasswordField(u'password',
                             validators=[DataRequired(message=u"I forgot to fill in this item!"), EqualTo('password2', message=u'Passwords must match'),
                                         Length(6, 32)])
    password2 = PasswordField(u'Confirm password', validators=[DataRequired(message=u"I forgot to fill in this item!")])
    submit = SubmitField(u'Register')

    def validate_email(self, field):
        if User.query.filter(db.func.lower(User.email) == db.func.lower(field.data)).first():
            raise ValidationError(u'Email already registered.')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(u'Old password', validators=[DataRequired(message=u"I forgot to fill in this item!")])
    new_password = PasswordField(u'New password', validators=[DataRequired(message=u"I forgot to fill in this item!"),
                                                     EqualTo('confirm_password', message=u'Passwords must match.'),
                                                     Length(6, 32)])
    confirm_password = PasswordField(u'Confirm new password', validators=[DataRequired(message=u"I forgot to fill in this item!")])
    submit = SubmitField(u"Update Password")

    def validate_old_password(self, field):
        from flask_login import current_user
        if not current_user.verify_password(field.data):
            raise ValidationError(u'Reset Password')
