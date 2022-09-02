#!/usr/bin/python3
"""Modules that contains the entry point of the command interpreter."""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class represent the command processor"""

    prompt = '(hbnb) '

    def do_help(self, arg):
        """This action is provided by default by cmd,
        type help <topic>.
        """
        return super().do_help(arg)

    def do_quit(self, line):
        """The command to exit the program"""
        return True

    def do_EOF(self, line):
        """The command to exit the program"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
