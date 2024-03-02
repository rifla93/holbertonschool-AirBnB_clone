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
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
