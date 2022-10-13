#!/usr/bin/python3
""" A module for the DB-storage class"""
from importlib.metadata import metadata
from sqlalchemy.orm import sessionmaker
from sqlalchemy import  create_engine
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
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
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """_summary_

        Args:
            cls (_type_, optional): _description_. Defaults to None.
        """

        dict = {}
        class_list = [State, City, Place, Review, User, Amenity]
        if cls is None:
            for c in class_list:
                objects = self.__session.query(c)
                for obj in objects:
                    key = "{}.{}".format(
                        obj.__class__.__name__,
                        obj.id
                    )
                    dict[key] = obj
        else:
            if type(cls) == str:
                cls = eval(cls)
            objects = self.__session.query(cls)
            for obj in objects:
                key = "{}.{}".format(
                    obj.__class__.__name__,
                    obj.id
                )
                dict[key] = obj

    def new(self, obj):
        """
        adds the obj to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commits all change in the session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        deletes from current db session

        obj: the object to delete
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ create all table in the db """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()