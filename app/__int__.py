from flask import Flask
from configuracion import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
from app.Rutas.login_bp import login_bp

app.register_blueprint(login_bp, url_prefix="/login")