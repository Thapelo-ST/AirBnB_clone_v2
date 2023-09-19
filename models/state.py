#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if storage_type == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        @property
        def cities(self):
            """getter for list of city instances"""
            cities = models.storage.all(City)
            return [city for city in cities.values()
                    if city.state_id == self.id]
