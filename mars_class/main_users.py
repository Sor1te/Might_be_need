from flask import Flask, render_template, redirect, abort, request, make_response, jsonify
from data.users import User
from forms.user import RegisterForm, LoginForm
from data.jobs import Jobs
from data import db_session
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_restful import reqparse, abort, Api, Resource
from forms.jobs import JobsForm
from data import jobs_api
from mars_class.data import users_resources

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
api = Api(app)


def main():
    db_session.global_init("db/mars_workers.db")
    api.add_resource(users_resources.UsersListResource, '/api/v2/users')
    # для одного объекта
    api.add_resource(users_resources.UsersResource, '/api/v2/users/<int:users_id>')

    # app.register_blueprint(jobs_api.blueprint)
    app.run(port=5050, debug=True)


if __name__ == '__main__':
    main()
