from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, PasswordField

from wtforms import validators, ValidationError


class LoginForm(Form):
    name =   TextField("Name:", [validators.Required("Please enter your name.")])
    email = TextField("Email", [validators.Required("Please enter your email address."),
                                validators.Email("Please enter your email address.")])
    password = PasswordField("Password",[validators.required("Please Enter Password")])
    submit = SubmitField("Send")

