import os
from flask import Flask
from .views import views


def create_app():
    # create and configure the app
    app = Flask(__name__, static_url_path='', 
            static_folder='static',
            template_folder='templates')
    app.config.from_mapping(
        SECRET_KEY='dev'
       #DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    app.register_blueprint(views, url_prefix='/')
    
    
    return app

