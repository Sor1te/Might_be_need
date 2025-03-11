from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobsForm(FlaskForm):
    team_leader = IntegerField('Тим-лидер', validators=[DataRequired()])
    job = StringField('Работа', validators=[DataRequired()])
    work_size = StringField('Кол-во часов', validators=[DataRequired()])
    collaborators = StringField('Коллабораторы', validators=[DataRequired()])
    is_finished = BooleanField("Закончена")
    submit = SubmitField('Применить')