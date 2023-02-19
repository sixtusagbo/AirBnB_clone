#!/usr/bin/python3
"""
Module that contains the entry point of the command interpreter
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex
import json
import os


class HBNBCommand(cmd.Cmd):
    """ entry point for command interpreter """
    prompt = '(hbnb) '
    l_classes = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place',
                 'Review']
    l_commands = ['create', 'show', 'update', 'destroy', 'all', 'count']

    def precmd(self, arg):
        """parses command input"""
        if '.' in arg and '(' in arg and ')' in arg:
            class_ = arg.split('.')
            command = class_[1].split('(')
            args = command[1].split(')')
            if (class_[0] in HBNBCommand.l_classes and
                    command[0] in HBNBCommand.l_commands):
                arg = command[0] + ' ' + class_[0] + ' ' + args[0]
        return arg

    def do_create(self, model):
        """ Creates an instance according to a given class """
        if not model:
            print("** class name missing **")
        elif model not in HBNBCommand.l_classes:
            print("** class doesn't exist **")
        else:
            dict_models = {"BaseModel": BaseModel, "User": User, "State":
                           State, "City": City, "Amenity": Amenity, "Place":
                           Place, "Review": Review}
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

        initial_split = arg.split(',', maxsplit=1)
        if (len(initial_split) > 1 and '{' in initial_split[1] and
            '}' in initial_split[1] and
            type(eval(initial_split[1])) is dict):
            args = initial_split[0].split()
            i_string = json.dumps(eval(initial_split[1]))
            args += [json.loads(i_string)]
        else:
            a = "" # string for shlex
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
                    # determine if am updating from dictionary
                    if type(args[2]) is dict:
                        for key, value in args[2].items():
                            setattr(obj, key, value)
                        storage.save()
                    elif len(args) == 2:
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

    def do_count(self, class_name):
        """counts number of instances of a class"""
        count = 0
        all_objs = storage.all()
        for k, v in all_objs.items():
            cls = k.split('.')
            if cls[0] == class_name:
                count = count + 1
        print(count)

    def do_shell(self, command):
        """ shell access """
        os.system(command)

    def postloop(self):
        print('GoodBye!')

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
