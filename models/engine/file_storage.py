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
        key_val = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key_val] = obj

    def save(self):
        with open(FileStorage.__file_path, "w") as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as file:
                dict_obj = json.load(file)
                FileStorage.new(self, dict_obj)
