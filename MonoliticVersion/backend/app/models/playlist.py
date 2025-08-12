from app.models.database import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Playlist(db.Model):
    __tablename__ = 'playlists'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    # tracks = relationship('Track', secondary='playlist_tracks', back_populates='playlists')
