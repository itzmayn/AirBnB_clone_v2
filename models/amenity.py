#!/usr/bin/python3
"""Amenity Module for HBNB project"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

STORAGE_TYPE = getenv('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    """Amenity class"""
    if STORAGE_TYPE == "db":
        from models.place import place_amenity
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity)
    else:
        name = ''
