from flask import Flask
from config import db, migrate
from dotenv import load_dotenv
import os
from flask_jwt_extended import JWTManager
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)

# Permitir solo tu frontend de Amplify
CORS(app, resources={r"/*": {"origins": "https://main.db5n3w69x7kah.amplifyapp.com"}})

# Configuración de JWT y base de datos
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'Clave secreta para examen')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de extensiones
db.init_app(app)
migrate.init_app(app, db)
jwt = JWTManager(app)

@app.route('/')
def home():
    return 'API realizada para el tercer examen de Aplicaciones Web'

# Registro de rutas
from routes.user import usuario_bp
app.register_blueprint(usuario_bp, url_prefix='/usuarios')

if __name__ == '__main__':
    app.run(debug=True)
