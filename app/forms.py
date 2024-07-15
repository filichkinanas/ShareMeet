from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length


class CommentForm(FlaskForm):
    name = StringField('Имя', validators=[DataRequired()])
    contact = StringField('Контакт для связи')
    comment = TextAreaField('Комментарий', validators=[Length(min=10, max=1000)])
    submit = SubmitField('Отправить')