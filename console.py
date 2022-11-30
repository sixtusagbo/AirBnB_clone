#!/usr/bin/python3
"""
Module that contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ entry point for command interpreter """
    prompt = '(hbnb) '

    def emptyline(self):
        pass

    def do_quit(self, line):
        """ Quit command to exit the command interpreter """
        return True

    do_EOF = do_quit

if __name__ == '__main__':
    HBNBCommand().cmdloop()
