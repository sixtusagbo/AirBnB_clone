#!/usr/bin/python3
"""
Module that contains the entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
import shlex


class HBNBCommand(cmd.Cmd):
    """ entry point for command interpreter """
    prompt = '(hbnb) '
    l_classes = ['BaseModel', 'User']
    l_commands = ['create', 'show', 'update', 'destroy', 'all']

    def do_create(self, model):
        """ Creates an instance according to a given class """
        if not model:
            print("** class name missing **")
        elif model not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        else:
            dict_models = {'BaseModel': BaseModel, 'User': User}
            new_model = dict_models[model]()
            new_model.save()
            print(new_model.id)

    def do_show(self, arg):
        """ Shows string representation of an instance passed """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """ Deletes an instance passed """

        if not arg:
            print("** class name missing **")
            return

        args = arg.split(' ')

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                ob_id = value.id
                if ob_name == args[0] and ob_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """
        if not arg:
            print("** class name missing **")
            return

        a = ""
        for argument in arg.split(','):
            a = a + argument

        args = shlex.split(a)

        if args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, obj in all_objs.items():
                obj_name = obj.__class__.__name__
                obj_id = obj.id
                if obj_name == args[0] and obj_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(obj, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints string represention of all instances of a given class """
        args = arg.split(' ')

        if args[0] and args[0] not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_instances = []
            if not args[0]:
                for value in all_objs.values():
                    list_instances += [str(value)]
            else:
                for key, value in all_objs.items():
                    ob_name = value.__class__.__name__
                    if ob_name == args[0]:
                        list_instances += [str(value)]
            print(list_instances)

    def emptyline(self):
        pass

    def do_quit(self, line):
        """ Quit command to exit the command interpreter """
        return True

    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
