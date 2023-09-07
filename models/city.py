#!/usr/bin/python3
"""Module that contains the city class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
<<<<<<< HEAD
    """ The city class, contains state ID and name """
    if os.getenv("HBNB_STORAGE_TYPE") == "db":
        __table_name__ = "cities"

        state_id = Column(String(60), ForeignKey('states.id'),
                          nullable=False)
        name = Column(String(128), nullable=False)
    else:
        state_id = ""
        name = ""
=======
    """Defines class for City
    Attributes:
        state_id: The state id
        name: input name
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    places = relationship("Place", cascade='all, delete, delete-orphan',
                          backref="cities")
>>>>>>> 1296452808686fa2c67e13e4eae2ec62bbdeae86
