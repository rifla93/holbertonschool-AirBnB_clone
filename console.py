import cmd

class HBNBCommand(cmd.Cmd):
    """Command line interpreter for HBNB project."""
    
    prompt = "(hbnb) "  # Custom prompt
    
    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True
    
    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("\nExiting the program. Goodbye!")
        return True
    
    def emptyline(self):
        """Empty line + ENTER shouldn't execute anything."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
