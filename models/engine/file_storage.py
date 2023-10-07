#!/usr/bin/python3
"""This module defines a class to manage file storage for the HBNB clone"""
import json
from models import city, place, review, state, amenity, user, base_model



class FileStorage:
    """This class gitmanages storage of HBNB models in JSON format"""
    __file_path = 'file.json'
    __objects = {}
    CLASSES = {
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'Amenity': amenity.Amenity,
        'User': user.User
    }

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage.
        If cls specified, only returns that class."""
        if cls:
            if cls in self.CLASSES:
                cls = self.CLASSES[cls]
            specific_instances = {}
            for key, value in self.__objects.items():
                if isinstance(value, cls):
                    specific_instances[key] = value
            return specific_instances
        return self.__objects

    def new(self, obj):
        """Adds a new object to storage dictionary"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Saves the storage dictionary to a file"""
        serialized_objects = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Loads the storage dictionary from a file"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                serialized_objects = json.load(file)
                self.__objects = {
                    key: self.CLASSES[val['__class__']](**val) for key, val in serialized_objects.items()
                }
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an object from __objects if it exists"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects.pop(key, None)

    def close(self):
        """Calls reload() method"""
        self.reload()
