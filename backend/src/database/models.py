from sqlalchemy import ARRAY, Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
from typing import Any, Dict
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .db_manager import Base

class User(Base):
    __tablename__ = 'users'
    
    user_id = Column(UUID, nullable=False, primary_key=True)
    username = Column(String, nullable=False)
    avatar = Column(String, nullable=True)
    password_hash = Column(String, nullable=False)
    refresh_token = Column(String, nullable=True)
    comments = relationship("Comments", back_populates="user", cascade="all, delete-orphan")

    def to_dict(self) -> Dict[str, Any]:
        return {
            'id': self.user_id,
            'username': self.username,
            'refresh_token': self.refresh_token,
        }

# class Comments(Base):
#     __tablename__ = 'comments'
    
#     comment_id = Column(UUID, nullable=False, primary_key=True)
#     user_id = Column(UUID, ForeignKey("users.user_id", ondelete='CASCADE'), nullable=False)
#     video_id = Column(UUID, ForeignKey("videos.video_id", ondelete='CASCADE'), nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)

#     user = relationship("User", back_populates="comments")
#     video = relationship("Video", back_populates="comments")



class Anime(Base):
    __tablename__ = 'anime'
    id = Column(Integer, primary_key=True)
    title_ru = Column(String(100), nullable=False)
    title_en = Column(String(100), nullable=False)
    posters = Column(String(200), nullable=True)  # URL или путь к постеру
    genres = Column(ARRAY(String(50)), nullable=True)  # Здесь может быть массив жанров, но в SQL это будет текст
    description = Column(Text, nullable=True)
    in_favorites = Column(Integer)
    
    series = relationship("Series", back_populates="anime")

class Series(Base):
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True)
    anime_id = Column(Integer, ForeignKey('anime.id'), nullable=False)
    number = Column(Integer, nullable=False)
    preview = Column(String(200), nullable=True)  # URL или путь к превью
    fhd_url = Column(String(200), nullable=True)  # URL для Full HD
    hd_url = Column(String(200), nullable=True)  # URL для HD
    sd_url = Column(String(200), nullable=True)  # URL для SD
    
    anime = relationship("Anime", back_populates="series")



