#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ Getter of cities"""
            cities = models.storage.all(City)
            list_cities = []

            for c in cities.values():
                if self.id == c.place_id:
                    list_cities.append(c)

            return list_cities
