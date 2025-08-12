
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from app import models
from app.models.database import db, User
from werkzeug.security import generate_password_hash
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from app import models
from app.models.database import db, User
from werkzeug.security import generate_password_hash
import importlib.util
spec = importlib.util.spec_from_file_location("app_module", os.path.join(os.path.dirname(__file__), "app.py"))
app_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_module)
create_app = app_module.create_app
from app.models.database import db, User
from werkzeug.security import generate_password_hash

def main():
    app, _ = create_app()
    with app.app_context():
        email = input("Email del usuario: ")
        password = input("Contraseña: ")
        username = input("Username (opcional): ")
        if not email or not password:
            print("Email y contraseña son obligatorios.")
            return
        if len(password) < 6:
            print("La contraseña debe tener al menos 6 caracteres.")
            return
        if User.query.filter_by(email=email).first():
            print("El email ya está registrado.")
            return
        user = User(email=email, password=generate_password_hash(password), username=username or None)
        db.session.add(user)
        db.session.commit()
        print("Usuario registrado:", user.to_dict())

if __name__ == "__main__":
    main()
