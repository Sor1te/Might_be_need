from flask import Flask
from data.users import User
from data.jobs import Jobs
from data import db_session

db_session.global_init("db/mars_workers.db")
job = Jobs()
job.team_leader = 1
job.job = 'teach myself'
job.work_size = 1
job.collaborators = '1 2 3'
job.is_finished = True
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()

job = Jobs()
job.team_leader = 4
job.job = 'nothing'
job.work_size = 9
job.collaborators = '1 4 5'
job.is_finished = False
db_sess = db_session.create_session()
db_sess.add(job)
db_sess.commit()

