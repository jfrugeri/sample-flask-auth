from flask import Flask, request, jsonify
from models.user import User
from database import db
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from dotenv import load_dotenv
import bcrypt
import os

load_dotenv()
db_root_password = os.getenv("MYSQL_ROOT_PASSWORD")
db_database_name = os.getenv("MYSQL_DATABASE")

app = Flask(__name__)
app.config["SECRET_KEY"] = "Your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://root:{db_root_password}@127.0.0.1:3306/{db_database_name}"

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)

# View de Login
login_manager.login_view = "login"

# Carrega o usuario
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Criar usuarios
@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username and password:
        hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
        user = User(username=username, password=hashed_password, role="user")
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": "Usuario criado com sucesso"}), 201

    return jsonify({"message": "Dados invalidas"}), 400

# Login dos usuarios
@app.route('/login', methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username and password:
        user = User.query.filter_by(username=username).first()

        if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
            login_user(user)
            return jsonify({"message": "Autentificacao realizada com sucesso"})

    return jsonify({"message": "Credenciais invalidas"}), 400

# Logout dos usuarios
@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return jsonify({"messag": "Logout realizado com sucesso"})

# Pegar usuario por ID
@app.route('/user/<int:id_user>', methods=['GET'])
@login_required
def read_user(id_user):
    user = User.query.get(id_user)
    
    if user:
        return jsonify({"message": "Usuario encontrado", "id": user.id, "username": user.username})

    return jsonify({"message": "Usuario nao encontrado"}), 404

# Update de senha do usuario
@app.route('/user/<int:id_user>', methods=['PUT'])
@login_required
def update_user(id_user):
    data = request.get_json()
    user = User.query.get(id_user)

    if id_user != current_user.id and current_user.role == "user":
        return jsonify({"message": "Voce nao pode atualizar a senha de outro usuario"}), 403
    
    if user and data.get("password"):
        
        hashed_password = bcrypt.hashpw(str.encode(data.get("password")), bcrypt.gensalt())
        user.password = hashed_password
        db.session.commit()

        return jsonify({"message": "Usuario atualizado"})
    
    return jsonify({"message": "Usuario nao encontrado"}), 404

# Deletar usuarios
@app.route('/user/<int:id_user>', methods=['DELETE'])
@login_required
def delete_user(id_user):
    user = User.query.get(id_user)

    if current_user.role != "admin":
        return jsonify({"message": "Voce nao tem permissao para deletar usuarios"}), 403

    if id_user == current_user.id:
        return jsonify({"message": "Voce nao pode deletar sua propria conta"}), 403
    
    if user:
        db.session.delete(user)
        db.session.commit()

        return jsonify({"message": f"Usuario {user.username} deletado"})

    return jsonify({"message": "Usuario nao encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)
