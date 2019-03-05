"""Entry point for the application and for the WSGI Server"""
from app import create_app, db

# import your models here

from app.models import Model

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Model': Model}
