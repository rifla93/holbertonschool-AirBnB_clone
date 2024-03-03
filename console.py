#!/usr/bin/python3
"""
Defines the HBNBCommand class.
"""
import models
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    Class HBNB
    """

    prompt = "(hbnb) "

    valid_classes = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def do_create(self, line):
        """Create a new instance, save it, and print its ID."""
        if not line:
            print("** class name missing **")
            return

        args = line.split()
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        new_instance = eval(args[0])()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        """Print the string representation of an instance
        based on class name and ID."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(args[0], obj_id)
        obj_dict = models.storage.all()
        if key in obj_dict:
            obj = obj_dict[key]
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Delete an instance based on class name and ID."""
        args = line.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)

        obj_dict = models.storage.all()
        if key in obj_dict:
            del obj_dict[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Print string representations of all instances
        based or not on the class name."""
        args = line.split()

        if not args:
            instances = []
            for class_name in self.valid_classes:
                if class_name in self.valid_classes:
                    instances += [
                        str(obj)
                        for obj in models.storage.all().values()
                        if obj.__class__.__name__ == class_name
                    ]
            print(instances)
        else:
            class_name = args[0]
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
            else:
                instances = [
                    str(obj)
                    for obj in models.storage.all().values()
                    if obj.__class__.__name__ == class_name
                ]
                print(instances)

    def do_update(self, line):
        """Updates an instance based on the class name
        and id by adding or updating an attribute."""
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]
        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)

        obj_dict = models.storage.all()

        if key not in obj_dict:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        value = args[3]

        if attribute_name in ["id", "created_at", "updated_at"]:
            return

        obj = obj_dict[key]
        setattr(obj, attribute_name, value)
        models.storage.save()

    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        exit(0)

    def do_EOF(self, arg):
        """
        EOF command to exit the program
        """
        print()
        exit(0)

    def emptyline(self):
        """
        Empty line + enter
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
