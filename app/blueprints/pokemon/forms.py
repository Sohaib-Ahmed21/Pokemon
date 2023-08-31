# from flask_wtf import FlaskForm
# from wtforms import StringField, IntegerField, TextAreaField
# from wtforms.validators import NumberRange
#
#
# class InitialDataForm(FlaskForm):
#     team = StringField("Team")
#     user_idel = StringField("Username")
#     user_idmove = StringField("User Idmove")
#     level = IntegerField("Level", validators=[NumberRange(min=1)])
#     xp = IntegerField("XP", validators=[NumberRange(min=0)])
#     items = TextAreaField("Items")
#     pokemon = TextAreaField("Pokemon")
# from flask_wtf import FlaskForm
# from wtforms import StringField, SelectField
# from wtforms.validators import DataRequired
#
#
# class InitialDataForm(FlaskForm):
#     user_idel = StringField("Username", validators=[DataRequired()])
#     team = SelectField(
#         "Select a team",
#         choices=[("team1", "Team 1"), ("team2", "Team 2")],
#         validators=[DataRequired()],
#     )
#     pokemon = SelectField(
#         "Select an initial Pokemon",
#         choices=[("pokemon1", "Pokemon 1"), ("pokemon2", "Pokemon 2")],
#         validators=[DataRequired()],
#     )

# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField
from wtforms.validators import DataRequired


class InitialDataForm(FlaskForm):
    user_idel = StringField("Username", validators=[DataRequired()])
    team = SelectField(
        "Select a team",
        choices=[("team1", "Team 1"), ("team2", "Team 2"), ("team3", "Team 3")],
        validators=[DataRequired()],
    )
    pokemon = SelectField(
        "Select an initial Pokemon",
        choices=[("pokemon1", "Pikachu"), ("pokemon2", "Charmane")],
        validators=[DataRequired()],
    )


class QuestionnaireForm(FlaskForm):
    name = StringField("Name")
    gender = RadioField(
        "Gender", choices=[("male", "Male"), ("female", "Female"), ("other", "Other")]
    )
