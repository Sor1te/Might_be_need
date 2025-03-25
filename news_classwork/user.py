from flask import Flask
from data_for_news.users import User
from data_for_news.news import News
from data_for_news import db_session

db_session.global_init("db/blogs.db")
news = News()
user = User()
user.name = "Пользователь 112434"
user.about = "биография пользователя 1235324"
user.email = "email2s3244df34@email.ru"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user.name = "Пользователь 12"
user.about = "биография пользователя 1235324"
user.email = "emafsadfs45656dffg@email.ru"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user.name = "Пользователь 192"
user.about = "биография пользователя 1324"
user.email = "emashhjgl2346798901jklfg@email.ru"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user.name = "Пользователь 2"
user.about = "биография пользователя 34"
user.email = "ema2erdgil@email.ru"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()


user = db_sess.query(User).first()
print(user.name)

for user in db_sess.query(User).all():
    print(user)