from flask import Blueprint
from app.controllers.LoginController import index, register

login_bp = Blueprint('login_bp', __name__)

login_bp.route("/", methods=["GET", "POST"]) (index)
login_bp.route("/register", methods=["GET", "POST"]) (register)