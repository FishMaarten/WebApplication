from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField, SelectField)
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log In")

class AddressForm(FlaskForm):
    WINDOWS = [("50","50x50"),("80","80x80"),("100","100x100"),("140","140x140")]
    PROJECTION = [("3D","3D Projection ( x , y , z )"),("2D","2D Projection ( x , y )")]
    header = "Plot any building in Flanders!"
    address = StringField("Which address would you like to see?",
            validators=[DataRequired()])
    projection = SelectField("Projection", choices=PROJECTION, validators=[DataRequired()])
    surroundings = BooleanField("View surroundings?")
    window = SelectField("Window size", choices=WINDOWS, validators=[DataRequired()])
    submit = SubmitField("Plot")

class RegisterForm(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired()])
    sir_name = StringField("Surname", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Re-enter Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")
