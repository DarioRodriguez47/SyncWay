from flask import Blueprint, request, jsonify
from app.models.database import db
from app.models.playlist import Playlist

playlists_bp = Blueprint('playlists', __name__)

@playlists_bp.route('/create', methods=['POST'])
def create_playlist():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({'success': False, 'message': 'Nombre requerido'}), 400
    playlist = Playlist(name=name)
    db.session.add(playlist)
    db.session.commit()
    return jsonify({'id': playlist.id, 'name': playlist.name, 'tracks': []})

@playlists_bp.route('/user/<int:user_id>', methods=['GET'])
def get_user_playlists(user_id):
    playlists = Playlist.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': p.id, 'name': p.name, 'tracks': []} for p in playlists])

@playlists_bp.route('/<int:playlist_id>/add-track', methods=['POST'])
def add_track_to_playlist(playlist_id):
    data = request.get_json()
    track_id = data.get('track_id')
    # Aquí deberías agregar la lógica para asociar el track a la playlist
    return jsonify({'success': True})
