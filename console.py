#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program when EOF (Ctrl+D) is reached"""
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print(" class name missing ")
            return
        try:
            obj = eval(arg)()
            obj.save()
            print(obj.id)
        except NameError:
            print(" class doesn't exist ")

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not arg:
            print(" class name missing ")
            return
        elif args[0] not in storage.classes():
            print(" class doesn't exist ")
            return
        elif len(args) == 1:
            print(" instance id missing ")
            return
        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in objects:
            print(" no instance found ")
        else:
            print(objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("class name missing")
            return
        elif args[0] not in storage.classes():
            print(" class doesn't exist ")
            return
        elif len(args) == 1:
            print(" id missing ")
            return
        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in objects:
            print(" not found ")
        else:
            del objects[key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return
        elif arg not in storage.classes():
            print("class doesn't exist")
            return
        print([str(obj) for key, obj in objects.items() if arg in key])

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not arg:
            print("class name missing")
            return
        elif args[0] not in storage.classes():
            print("class doesn't exist")
            return
        elif len(args) == 1:
            print("instance id missing")
            return
        elif len(args) == 2:
            print("attribute name missing")
            return
        elif len(args) == 3:
            print(" value missing ")
            return
        objects = storage.all()
        key = "{}.{}".format(args[0], args[1])
        if key not in objects:
            print(" not found ")
            return
        obj = objects[key]
        setattr(obj, args[2], args[3].strip('"'))
        storage.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
