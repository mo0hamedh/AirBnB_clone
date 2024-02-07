#!/usr/bin/python3
import json
class FileStorage :
    __file_path = "file.json"
    __objects = {}
    def all(self) :
        """returns the dictionary __objects"""
        return FileStorage.__objects
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj
    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        for obj in FileStorage.__objects.values():
            obj_dic = obj.to_dict()
            with open(FileStorage.__file_path, 'w') as json_file:
                json.dump(obj_dic, json_file)
    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists)."""
        try:
            with open(FileStorage.__file_path) as json_file:
                objects_dict = json.load(json_file) 
                for obj in objects_dict.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name) (**obj))
        except FileNotFoundError:
            return
         