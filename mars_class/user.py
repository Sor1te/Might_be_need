from flask import Flask
from data.users import User
from data.jobs import Jobs
from data import db_session

db_session.global_init("db/mars_workers.db")
user = User()
user.surname = "r"
user.name = "r"
user.age = 67
user.position = 'pos'
user.speciality = 'gfs'
user.address = 'fghghfshg'
user.email = "email2fghfgh32134254@email.ru"
user.hashed_password = "12345"
user.set_password(user.hashed_password)
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

db_session.global_init("db/blogs.db")
user = User()
user.surname = "r"
user.name = "r"
user.age = 67
user.position = 'pos'
user.speciality = 'gfs'
user.address = 'fghghfshg'
user.email = "email2321dfdfcv323regdfhdf4254@email.ru"
user.hashed_password = "12345"
user.set_password(user.hashed_password)
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

db_session.global_init("db/blogs.db")
user = User()
user.surname = "r"
user.name = "r"
user.age = 67
user.position = 'pos'
user.speciality = 'gfs'
user.address = 'fghghfshg'
user.email = "em4wertedffgh254@email.ru"
user.hashed_password = "12345"
user.set_password(user.hashed_password)
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user = db_sess.query(User).first()
print(user.name)

for user in db_sess.query(User).all():
    print(user)