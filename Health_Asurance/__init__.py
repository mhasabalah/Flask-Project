from flask import Flask
from flask_mysqldb import MySQL
from Health_Asurance.sqlConfig import *

mysql = MySQL()

def create_app():
    # create and configure the app

    app = Flask(__name__, static_url_path='',
                static_folder='static',
                template_folder='templates')
    app.config.from_mapping(
        SECRET_KEY='dev'

    )
    app.config['MYSQL_USER'] = USER
    app.config['MYSQL_PASSWORD'] = PASSWORD
    app.config['MYSQL_HOST'] = HOST
    app.config['MYSQL_DB'] = DATABASE

    mysql = MySQL(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    return app
