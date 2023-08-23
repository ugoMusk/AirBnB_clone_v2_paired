#!/usr/bin/python3
""" new Storage engine module """

import models
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """ class the defines a database engine """
    __engine = None
    __session = None

    def __init__(self):
        """ class intitialization method for the storage object"""
        usr = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            usr, pwd, host, database), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
            
    def all(self, cls=None):
        """ methods that querries class objects based of whether cls is provide and if not, querries all object types """
