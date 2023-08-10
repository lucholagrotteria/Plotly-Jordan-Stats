from flask import Flask
from .views import views

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(views, url_prefix='/')
    app.config['SECRET_KEY'] = '++*25}~1!jne.,['

    return app