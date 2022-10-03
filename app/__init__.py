from flask import Flask
import flask
from config import Config
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

from app.routes.login_bp import login_bp
from app.routes.register_bp import register_bp 

#inicializar la aplicacion app con la configuracion Config y la base de datos db
app = Flask(__name__)
cors = CORS(app)
Config.from_object(Config)
db = SQLAlchemy(app)

app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(register_bp, url_prefix="/register")
db.create_all()
