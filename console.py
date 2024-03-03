<<<<<<< HEAD
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
=======
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command line interpreter for HBNB project."""

    prompt = "(hbnb) "  # Custom prompt

    def do_quit(self, arg):
        """Quit command to exit the program."""
        exit()

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        exit()

    def emptyline(self):
        """Empty line + ENTER shouldn't execute anything."""
        pass


class Console:
    def __init__(self):
        self.commands = {
            "create": self.create,
            "show": self.show,
            "destroy": self.destroy,
            "all": self.all,
            "update": self.update,
        }
        self.models = {"BaseModel": BaseModel}

    def create(self, args):
        if len(args) < 1:
            print("** class name missing **")
            return
        model_name = args[0]
        if model_name not in self.models:
            print("** class doesn't exist **")
            return
        model = self.modelsmodel_name
        model.save()
        print(model.id)

    def show(self, args):
        if len(args) < 1:
            print("** class name missing **")
            return
        model_name = args[0]
        if model_name not in self.models:
>>>>>>> dd7b085bfbc14d890787ee3a2ef45cb8e64813ec
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
<<<<<<< HEAD

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
=======
        model_id = args[1]
        # Assuming you have a method to get a model instance by id
        model = self.models[model_name].get_by_id(model_id)
        if model is None:
            print("** no instance found **")
            return
        print(str(model))

    def destroy(self, args):
        if len(args) < 1:
            print("** class name missing **")
            return
        model_name = args[0]
        if model_name not in self.models:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        model_id = args[1]
        # Assuming you have a method to delete a model instance by id
        success = self.models[model_name].delete_by_id(model_id)
        if not success:
            print("** no instance found **")

    def all(self, args):
        if len(args) > 0:
            model_name = args[0]
            if model_name not in self.models:
                print("** class doesn't exist **")
                return
            models = self.models[model_name].all()
        else:
            models = [
                model
                for model_class in self.models.values()
                for model in model_class.all()
            ]
        print([str(model) for model in models])

    def update(self, args):
        if len(args) < 1:
            print("** class name missing **")
            return
        model_name = args[0]
        if model_name not in self.models:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        model_id = args[1]
        model = self.models[model_name].get_by_id(model_id)
        if model is None:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        attr_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return
        attr_value = args[3]
        setattr(model, attr_name, attr_value)
        model.save()

    def run(self):
        while True:
            command = input("(hbnb) ")
            args = command.split()
            if len(args) == 0:
                continue
            command_name = args.pop(0)
            if command_name in self.commands:
                self.commandscommand_name
            else:
                print("** command doesn't exist **")
>>>>>>> dd7b085bfbc14d890787ee3a2ef45cb8e64813ec


if __name__ == "__main__":
    HBNBCommand().cmdloop()
