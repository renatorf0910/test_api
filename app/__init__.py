from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:3001"])
    from . import routes
    app.register_blueprint(routes.bp, url_prefix='/api')

    return app
