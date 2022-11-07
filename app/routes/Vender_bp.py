from flask import Blueprint
from app.controllers.VenderController import Vender

Vender_bp = Blueprint('Vender_bp', __name__)

Vender_bp.route("/vender", methods=["GET", "POST"]) (Vender)
Vender_bp.route("/Productos", methods=["GET", "POST"]) (Vender)