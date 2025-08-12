import os
import importlib.util

spec = importlib.util.spec_from_file_location("app_module", os.path.join(os.path.dirname(__file__), "app.py"))
app_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_module)
create_app = app_module.create_app

from app.models.database import db, Song

def main():
    assets_dir = os.path.join(os.path.dirname(__file__), 'assets')
    app, _ = create_app()
    with app.app_context():
        total = 0
        # Recorrer cada carpeta de artista/álbum
        for folder in os.listdir(assets_dir):
            folder_path = os.path.join(assets_dir, folder)
            if not os.path.isdir(folder_path):
                continue
            # Buscar cover.jpg en la carpeta
            cover_path = os.path.join(folder_path, 'cover.jpg')
            cover_url = f"http://localhost:5000/assets/{folder}/cover.jpg" if os.path.exists(cover_path) else None
            # Recorrer archivos de audio
            for filename in os.listdir(folder_path):
                if filename.lower().endswith('.flac'):
                    title = filename.replace('.flac', '').replace('01 - ', '').replace('02 - ', '').replace('03 - ', '').replace('04 - ', '').replace('05 - ', '').replace('06 - ', '').replace('07 - ', '').replace('08 - ', '').replace('09 - ', '').replace('10 - ', '').strip()
                    song = Song(
                        title=title,
                        artist=folder.split(' - ')[0],
                        album=folder,
                        duration=None,
                        file_path=f"http://localhost:5000/assets/{folder}/{filename}",
                        cover_url=cover_url,
                        artist_name=folder.split(' - ')[0],
                        artist_nickname=None,
                        nationality=None
                    )
                    db.session.add(song)
                    total += 1
        db.session.commit()
        print(f"Se cargaron {total} canciones en la base de datos con su imagen de portada.")

if __name__ == "__main__":
    main()
