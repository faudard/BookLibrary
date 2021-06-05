# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, URL
from flask_pagedown.fields import PageDownField
from flask_wtf.file import FileField, FileAllowed
from app import avatars


class EditProfileForm(FlaskForm):
    name = StringField(u'User name', validators = [DataRequired (message=u"The item forgot filled out! "), Length(1, 64, message=u"Length of 1 to 64 characters ")])
    major = StringField(u'major professional', validators = [Length(0, 128, message=u"Length is 0 to 128 characters ")])
    headline = StringField(u'a sentence introduces yours', Validators = [Length (0, 32, message=u"Within 32 characters ")])
    about_me = PageDownField(u"Personal profile ")
    submit = SubmitField(u"save Changes ")


class AvatarEditForm(FlaskForm):
    avatar_url = StringField('', validators=[Length(1, 100, message=u"Length limit within 100 characters "), URL(message=u"Please fill in the correct URL ")])
    submit = SubmitField(u"save ")


class AvatarUploadForm(FlaskForm):
    avatar = FileField('', validators=[FileAllowed(avatars, message=u"Only allowed to upload pictures ")])
