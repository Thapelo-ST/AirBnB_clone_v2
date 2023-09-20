#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


# Check the type of storage (db or file)
storage_type = models.storage.__class__.__name__


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if storage_type == 'DBStorage':
        cities = relationship('City', backref='state',
                              cascade='all, delete')
    else:
        @property
        def cities(self):
            """getter for list of city instances"""
            cities = models.storage.all(City)
            return [city for city in cities.values()
                    if city.state_id == self.id]
