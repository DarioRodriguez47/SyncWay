import sqlite3

# Ruta a la base de datos SQLite
DB_PATH = 'backend/app.db'

def clean_invalid_favorites():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Verificar si la tabla songs existe
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='songs'")
        if not cursor.fetchone():
            print("❌ La tabla 'songs' no existe en la base de datos. Verifica la ruta y la estructura.")
            conn.close()
            return

        # Verificar si la tabla favorite_songs existe
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='favorite_songs'")
        if not cursor.fetchone():
            print("❌ La tabla 'favorite_songs' no existe en la base de datos. Verifica la ruta y la estructura.")
            conn.close()
            return

        # Obtener todos los song_id válidos de la tabla songs
        cursor.execute('SELECT id FROM songs')
        valid_song_ids = set(row[0] for row in cursor.fetchall())
        print(f"IDs de canciones válidas: {valid_song_ids}")

        # Obtener todos los favoritos
        cursor.execute('SELECT id, song_id FROM favorite_songs')
        favorites = cursor.fetchall()
        print(f"Favoritos encontrados: {favorites}")

        # Buscar favoritos inválidos
        invalid_favorites = [fav_id for fav_id, song_id in favorites if song_id not in valid_song_ids]
        print(f"Favoritos inválidos a eliminar: {invalid_favorites}")

        # Eliminar favoritos inválidos
        for fav_id in invalid_favorites:
            cursor.execute('DELETE FROM favorite_songs WHERE id = ?', (fav_id,))
            print(f"Eliminado favorito con id: {fav_id}")

        conn.commit()
        conn.close()
        print("Limpieza completada.")
    except sqlite3.Error as e:
        print(f"❌ Error al conectar o consultar la base de datos: {e}")

if __name__ == '__main__':
    clean_invalid_favorites()
