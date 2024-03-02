from models.base_model import BaseModel
import json
import os
""" file storage """

class FileStorage:
    """ file storage """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key_val = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key_val] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(self.__file_path, "r") as file:
                serialized_objects = json.load(file)
                for key, value in serialized_objects.items():
                    class_name = eval(value["__class__"])(**value)
                    self.__objects[key] = class_name
        else:
            pass
