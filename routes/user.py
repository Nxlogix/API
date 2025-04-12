from flask import Blueprint, jsonify, request
from controllers.Users_Controller import create_usuario, login_usuario, get_all_usuarios

usuario_bp = Blueprint('usuarios', __name__)

@usuario_bp.route('/', methods=['POST'])
def user_store():
    data = request.get_json()
    email = data.get('email')
    nombre = data.get('nombre')
    password = data.get('password')

    if not all([email, nombre, password]):
        return jsonify({"error": "Rellena todos los campos por favor"}), 400
    
    return create_usuario(nombre, email, password)

@usuario_bp.route('/login', methods=['POST'])
def login_usuario_route():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "El email y la contraseña son requeridos para iniciar sesión"}), 400
    
    return login_usuario(email, password)

# Ruta para obtener todos los usuarios
@usuario_bp.route('/obtener', methods=['GET'])
def get_usuarios():
    return get_all_usuarios()