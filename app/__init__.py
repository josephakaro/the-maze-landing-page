from flask import Flask
# from flask_login import LoginManager

# login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    # login_manager.init_app(app)

    from app.auth import login
    from app.home import index
    from app.routes import about

    app.register_blueprint(login.login)
    app.register_blueprint(index.index)
    app.register_blueprint(about.about)


    return app