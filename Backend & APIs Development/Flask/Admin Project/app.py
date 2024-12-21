from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

import config

db = SQLAlchemy() # ORM
def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    
    # Create Flask-Admin instance    
    from routes import MyAdminIndexView
    admin = Admin(app, name='Admin', template_mode='bootstrap3', index_view=MyAdminIndexView())
    
    # Add views for each model
    from models import User
    admin.add_view(ModelView(User, db.session))

    # Connect ORM to the App
    db.init_app(app)
    
    # To Migrate App to DB
    migrate = Migrate(app,db)
    
    # For Managing Logins Operations
    login_manager = LoginManager(app)
    login_manager.login_view = 'login' # Redirects to login page if not logged in
    
    from models import User
    # Define the user_loader callback
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # For Hashing Passwords
    bcrypt = Bcrypt(app)
    
    # Import Routes
    from routes import register_routes
    register_routes(app,db,bcrypt)
    
    return app