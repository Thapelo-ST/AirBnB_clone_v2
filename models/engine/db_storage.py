#!/usr/bin/python3
""" db storage for sql alchemy and for mysql """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.exc import UnmappedClassError
from models.base_model import Base
from os import getenv


class DBStorage:
    """ db storage for sql alchemy"""
    __engine = None
    __session = None

    def __init__(self):
        """ initialises the DB class"""
        # connecting to db from env variables
        db_user = getenv("HBNB_MYSQL_USER")
        db_password = getenv("HBNB_MYSQL_PWD")
        db_host = getenv("HBNB_MYSQL_HOST")
        db_database = getenv("HBNB_MYSQL_DB")

        # making an engine
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.
            format(db_user, db_password, db_host, db_database),
            pool_pre_ping=True)

        # session initialization
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False))

    def all(self, cls=None):
        """query all objs from db session"""
        obj_dict = {}
        classes = ["User", "State", "City", "Amenity", "Place", "Review"]

        if cls is not None and cls.__name__ not in classes:
            return {}

        for c in classes:
            try:
                if cls is None or cls.__name__ == c:
                    objs = self.__session.query(eval(c)).all()
                    for obj in objs:
                        key = "{}.{}".format(obj.__class__.__name__, obj.id)
                        obj_dict[key] = obj
            except UnmappedClassError:
                pass
            return obj_dict

    def new(self, obj):
        """ add an object to the existing db session """
        if obj:
            self.__session.add(obj)

    def save(self):
        """ Commit all changes of the existing db session """
        self.__session.commit()

    def delete(self, obj=None):
        """delete obj from current db session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """make tables and initialise the session"""
        Base.metadata.create_all(self.__engine)
        self.__session == scoped_session(sessionmaker(bind=self.__engine,
                                                      expire_on_commit=False))

    def close(self):
        """
        uses remove() method on the private session attribute or close() on Session
        """
        self.__session.close()

