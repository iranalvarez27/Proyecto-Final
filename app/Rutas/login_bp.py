from flask import Blueprint
from app.Controladores.LoginControlador import login, register
login_bp = Blueprint('login_bp', __name__)

login_bp.route("/", methods=["GET", "POST"]) (login)
login_bp.route("/register", methods=["GET", "POST"]) (register)