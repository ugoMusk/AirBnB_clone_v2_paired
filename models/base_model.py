#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import os

# converts format to time object
time_format = "%Y-%m-%dT%H:%M:%S.%f"

# Set model data structure based on if storage env is set or not
if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""

    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        id = Column(String(60), nullable=False,
                    primary_key=True)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow)
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow)

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
                if type(self.created_at) is str:
                    self.created_at = datetime.strptime(
                        self.created_at, time_format)
                    if type(self.updated_at) is str:
                        self.updated_at = datetime.strptime(
                            self.updated_at, time_format)
                del kwargs['__class__']
                self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        if 'created_at' in dictionary:
            dictionary['created_at'] = self.created_at.isoformat()
        if 'updated_at' in dictionary:
            dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary.pop('_sa_instance_state', None)
        return dictionary

    def delete(self):
        """Delete current instance from storage by calling its delete method"""
        storage.delete(self)
