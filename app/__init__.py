from flask import Flask

def create_app():
    print(f'11')
    app = Flask(__name__)
    print(f'12')
    from . import routes
    app.register_blueprint(routes.bp)
    print(f'13')
    return app
