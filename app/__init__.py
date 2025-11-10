from flask import Flask,jsonify
from app.blueprints.app_v1 import bp as app_v1_bp
from config import Config
from app.extensions import init_extensions
def create_app(config_object=None):
        app= Flask(__name__)
        app.config.from_object(Config)
        app.register_blueprint(app_v1_bp, url_prefix='/api/v1')
        init_extensions(app)


        return app

    