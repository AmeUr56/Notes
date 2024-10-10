from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Email,EqualTo,Length,DataRequired
from flask_wtf.recaptcha import RecaptchaField

class RegistrationForm(FlaskForm):
    username = StringField('username',validators=[DataRequired(),Length(min=4,max=20)])
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired(),Length(min=8,max=50)])
    confirm_password = PasswordField('confirm_password',validators=[DataRequired(),EqualTo('password')])
    
    recaptcha = RecaptchaField()
    submit = SubmitField('Register')
    
class LoginForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password',validators=[DataRequired(),Length(min=8,max=50)])
    
    recaptcha = RecaptchaField()
    submit = SubmitField('Login')
    