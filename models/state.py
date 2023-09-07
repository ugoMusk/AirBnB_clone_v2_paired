#!/usr/bin/python3
"""Module that defines  the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
<<<<<<< HEAD
    """ State class """
    if os.getenv("HBNB_STORAGE_TYPE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
=======
    """Defines the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")
>>>>>>> 1296452808686fa2c67e13e4eae2ec62bbdeae86

    @property
    def cities(self):
        var = models.storage.all()
        list_array = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                list_array.append(var[key])
        for elem in list_array:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)
