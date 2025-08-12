#!/bin/bash
set -e

# Script de inicialización para la base de datos PostgreSQL
# Este script se ejecuta automáticamente cuando se crea el contenedor por primera vez

# Crear extensiones necesarias
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    -- Crear extensión para UUID
    CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
    
    -- Crear extensión para funciones de texto
    CREATE EXTENSION IF NOT EXISTS "unaccent";
    
    -- Crear extensión para búsqueda de texto completo
    CREATE EXTENSION IF NOT EXISTS "pg_trgm";
    
    -- Configurar zona horaria
    SET timezone = 'America/Lima';
    
    -- Crear función para actualizar timestamps automáticamente
    CREATE OR REPLACE FUNCTION update_modified_column()
    RETURNS TRIGGER AS \$\$
    BEGIN
        NEW.updated_at = CURRENT_TIMESTAMP;
        RETURN NEW;
    #!/bin/bash
    set -e

    # Script de inicialización para la base de datos PostgreSQL
    # Este script se ejecuta automáticamente cuando se crea el contenedor por primera vez

    # Crear extensiones necesarias
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
        CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
        CREATE EXTENSION IF NOT EXISTS "unaccent";
        CREATE EXTENSION IF NOT EXISTS "pg_trgm";
        SET timezone = 'America/Lima';
        CREATE OR REPLACE FUNCTION update_modified_column()
        RETURNS TRIGGER AS $$
        BEGIN
            NEW.updated_at = CURRENT_TIMESTAMP;
            RETURN NEW;
        END;
        $$ language 'plpgsql';
    EOSQL

    echo "✅ Extensiones y funciones creadas correctamente"

    # Crear tablas iniciales
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(120) UNIQUE NOT NULL,
            password VARCHAR(255) NOT NULL,
            username VARCHAR(50),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS songs (
            id SERIAL PRIMARY KEY,
            title VARCHAR(200) NOT NULL,
            artist VARCHAR(100) NOT NULL,
            album VARCHAR(100),
            duration INTEGER,
            file_path VARCHAR(500),
            cover_url VARCHAR(500),
            artist_name VARCHAR(100),
            artist_nickname VARCHAR(100),
            nationality VARCHAR(10),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );

        CREATE TABLE IF NOT EXISTS favorite_songs (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            song_id INTEGER NOT NULL REFERENCES songs(id) ON DELETE CASCADE,
            added_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, song_id)
        );

        CREATE TABLE IF NOT EXISTS chat_messages (
            id SERIAL PRIMARY KEY,
            user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
            message TEXT NOT NULL,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            room VARCHAR(50) DEFAULT 'general'
        );

        CREATE TRIGGER update_users_modtime 
            BEFORE UPDATE ON users 
            FOR EACH ROW EXECUTE FUNCTION update_modified_column();
        CREATE TRIGGER update_songs_modtime 
            BEFORE UPDATE ON songs 
            FOR EACH ROW EXECUTE FUNCTION update_modified_column();
    EOSQL

    echo "✅ Tablas creadas correctamente"

    # Crear índices
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
        CREATE INDEX IF NOT EXISTS idx_songs_artist ON songs USING gin(artist gin_trgm_ops);
        CREATE INDEX IF NOT EXISTS idx_songs_artist_name ON songs(artist_name);
        CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
        CREATE INDEX IF NOT EXISTS idx_favorite_songs_user_id ON favorite_songs(user_id);
        CREATE INDEX IF NOT EXISTS idx_favorite_songs_song_id ON favorite_songs(song_id);
    EOSQL

