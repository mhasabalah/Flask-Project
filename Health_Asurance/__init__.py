import os
from flask import Flask
from .views import views
from flask_mysqldb import MySQL

def create_app():
    # create and configure the app

    app = Flask(__name__, static_url_path='', 
            static_folder='static',
            template_folder='templates')
    app.config.from_mapping(
        SECRET_KEY='dev'

    #DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'health_insurance'

    mysql = MySQL(app)
    app.register_blueprint(views, url_prefix='/')
    
    return app

