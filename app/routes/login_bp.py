
from flask import Blueprint
from app.controllers.LoginController import index, register, choose, vender, productos, registrar_producto

login_bp = Blueprint('login_bp', __name__)

login_bp.route("/", methods=["GET", "POST"]) (index)
login_bp.route("/register", methods=["GET", "POST"]) (register)
login_bp.route("/choose", methods=["GET", "POST"]) (choose)
login_bp.route("/vender", methods=["GET", "POST"]) (vender)
login_bp.route("/productos", methods=["GET", "POST"]) (productos)
login_bp.route("/registrar_producto", methods=["GET", "POST"]) (registrar_producto)