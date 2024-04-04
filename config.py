from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect(app):
    db.init_app(app)

def handle_request(app):
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'POST')
        return response

class Config:
    SQLALCHEMY_DATABASE_URI= 'postgresql://postgres:123@localhost/palupi'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER= "static/upload"