#!/usr/bin/python3
""" A module for the DB-storage class"""
from importlib.metadata import metadata
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  create_engine
from sqlalchemy.schema import MetaData
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import sys
from os import getenv



username = getenv('HBNB_MYSQL_USER')
db = getenv('HBNB_MYSQL_DB')
host = getenv('HBNB_MYSQL_HOST')
storage_type = getenv('HBNB_TYPE_STORAGE')
env = getenv('HBNB_ENV')
password = getenv('HBNB_MYSQL_PWD')


class DBStorge:
    """ Class  for DB-Storage """

    __engine = None
    __session = None

    def __init__(self):
        """ A public method that create an
            instance of the DBStorage class
        """
        #dialect+driver://username:password@host:port/database
        #dialect+driver://username:password@host/database
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(username, password, host, db),
                                      pool_pre_ping=True)
        #Base.metadata.create_all(self.__engine)
        if env == 'test':
            metadata = MetaData(self.__engine)
            metadata.reflect()
            metadata.drop_all()

    def all(self, cls=None):
        """_summary_

        Args:
            cls (_type_, optional): _description_. Defaults to None.
        """
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        dict = {}
        class_list = [State, City, Place, Review, User, Amenity]
        if cls is None:
            pass
        else:
            for class_obj in class_list:
                if isinstance(cls, class_obj):
                    print("good")