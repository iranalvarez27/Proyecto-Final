from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
#inicializar la aplicacion app con la configuracion Config y la base de datos db
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from app.routes.login_bp import login_bp
app.register_blueprint(login_bp, url_prefix="/")
#app.register_blueprint(Vender_bp,url_prefix="/vender")
db.create_all()
