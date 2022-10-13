
from flask import Blueprint
from app.controllers.LoginController import index, register, choose

login_bp = Blueprint('login_bp', __name__)

login_bp.route("/", methods=["GET", "POST"]) (index)
login_bp.route("/register", methods=["GET", "POST"]) (register)
login_bp.route("/choose", methods=["GET", "POST"]) (choose)