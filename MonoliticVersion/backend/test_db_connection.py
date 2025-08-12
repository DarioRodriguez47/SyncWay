import os
import logging
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_database_url():
    load_dotenv()  # Carga variables de entorno
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        # Usar SQLite local si no existe DATABASE_URL
        database_url = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'app', 'local.db')}"
        logging.warning(f"No se encontró DATABASE_URL, usando SQLite local: {database_url}")
    return database_url

def test_connection(engine):
    try:
        with engine.connect() as connection:
            # Probar consulta según tipo de base de datos
            if str(engine.url).startswith('sqlite'):
                result = connection.execute(text("SELECT datetime('now');"))
            else:
                result = connection.execute(text("SELECT NOW();"))
            current_time = result.scalar()
            logging.info(f"Conexión exitosa! Hora actual en la DB: {current_time}")
    except SQLAlchemyError as e:
        logging.error(f"Error al conectar con la base de datos: {e}")
        raise

def main():
    database_url = get_database_url()
    engine = create_engine(database_url)
    test_connection(engine)

if __name__ == "__main__":
    main()
