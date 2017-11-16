import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

# instantiate the db
db = SQLAlchemy()
# instantiate flask migrate
migrate = Migrate()
# instantiate flask bcrypt
bcrypt = Bcrypt()

def create_app():

    # instantiate the app
    app = Flask(__name__)

    # enable CORS
    CORS(app)

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from project.api.views import payroll_blueprint
    app.register_blueprint(payroll_blueprint)

    return app
