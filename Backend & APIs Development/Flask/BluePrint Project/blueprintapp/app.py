
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    db.init(app)
    
    # Import and Register all Blueprints
    from blueprintapp.todos.routes import todos
    app.register_blueprint(todos,url_prefix='/todos')
    
    migrate = Migrate(app,db)
    
    return app