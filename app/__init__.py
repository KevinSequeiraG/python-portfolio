from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    
    app.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY'),
        MAILGUN_KEY = os.environ.get('MAILGUN_API_KEY'),
        MAILGUN_DOMAIN = os.environ.get('MAILGUN_DOMAIN')
    )
    
    from . import portfolio
    app.register_blueprint(portfolio.bp)

    # Forzar el modo de depuración
    app.debug = True
    
    return app