from flask import request,render_template,Blueprint

from blueprintapp.app import db
from blueprintapp.todos.models import Todo

todos = Blueprint('todos',__name__)


@todos.route('/')
def index():
    todos = Todo






