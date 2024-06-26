#!/usr/bin/python3
"""
Class that defines a state
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """class to create a state"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    # Relationship for DBStorage
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')

    @property
    def cities(self):
        """Getter attribute cities that returns
        the list of City instances
        with state_id equals to the current
        State.id for FileStorage relationship.
        """
        from models import storage
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
