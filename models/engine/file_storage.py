#!/usr/bin/python3
"""this module contains a class file_storage"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.review import Review
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity


class FileStorage:
    """serializes instances to a json file
    and deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage
        If a class is specified, only returns objects of that class.
        """
        if cls is None:
            return self.__objects
        else:
            filtered_objects = {
                    key: value for key, value in self.__objects.items()
                    if isinstance(value, cls)
            }
            return filtered_objects

    def new(self, obj):
        """
            sets the obj with a key in the dictionary of __objects
        Args:
            obj: the object to be added to the dictionary
        """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """serialize objects to the json file"""
        objects = {
                obj_id: obj.to_dict()
                for obj_id, obj in self.__objects.items()
        }
        with open(self.__file_path, "w") as f:
            json.dump(objects, f)

    def reload(self):
        """deserializes Json files"""
        if os.path.isfile(FileStorage.__file_path):
            with open(self.__file_path, "r") as f:
                objects = json.load(f)
                for obj_id, obj_dict in objects.items():
                    class_name = obj_dict["__class__"]
                    cls = eval(class_name)
                    obj = cls(**obj_dict)
                    self.__objects[obj_id] = obj

    def count(self, cls=None):
        """
        Count the number of instances of a given class,
        or all instances if no class is specified.
        Args:
            cls (type, optional): The class type to count instances of.
        Returns:
            int: The number of instances.
        """
        if cls:
            return sum(
                1 for obj in self.__objects.values()
                if isinstance(obj, cls)
            )
        return len(self.__objects)

    def delete(self, obj=None):
        """
        Deletes obj from __objects if it's inside.
        If obj is None, the method does nothing.
        """
        if obj is None:
            return
        key = "{}.{}".format(type(obj).__name__, obj.id)
        if key in self.__objects:
            del self.__objects[key]

    def close(self):
        """
        Call reload() method for deserializing the JSON file to objects
        """
        self.reload()
