from flask import session, redirect, url_for, request
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import json
import os

# Archivo para almacenar usuarios (en producción usar BD)
USERS_FILE = "users.json"

# Usuario y contraseña por defecto
DEFAULT_USER = "admin"
DEFAULT_PASSWORD = "admin123"

def init_users():
    """Inicializa usuarios por defecto"""
    if not os.path.exists(USERS_FILE):
        users = {
            DEFAULT_USER: generate_password_hash(DEFAULT_PASSWORD)
        }
        with open(USERS_FILE, 'w') as f:
            json.dump(users, f)

def get_users():
    """Obtiene todos los usuarios"""
    if not os.path.exists(USERS_FILE):
        init_users()
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def verify_user(username, password):
    """Verifica credenciales del usuario"""
    users = get_users()
    if username in users:
        return check_password_hash(users[username], password)
    return False

def login_required(f):
    """Decorador para proteger rutas"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def add_user(username, password):
    """Agrega un nuevo usuario"""
    users = get_users()
    if username not in users:
        users[username] = generate_password_hash(password)
        with open(USERS_FILE, 'w') as f:
            json.dump(users, f)
        return True
    return False

def change_password(username, old_password, new_password):
    """Cambia la contraseña de un usuario"""
    if verify_user(username, old_password):
        users = get_users()
        users[username] = generate_password_hash(new_password)
        with open(USERS_FILE, 'w') as f:
            json.dump(users, f)
        return True
    return False
