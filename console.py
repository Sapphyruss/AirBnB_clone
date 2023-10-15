#!/usr/bin/python3
"""The console."""
import cmd
import re
import shlex
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
import sys


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    classes = {'BaseModel': BaseModel, 'Amenity': Amenity,
               'State': State, 'Place': Place, 'Review': Review,
               'User': User, 'City': City}

    def default(self, arg):
        """Default cmd"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Exit command"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit"""
        print()
        return True

    def emptyline(self):
        """To do n othing after receiving an empty line."""
        pass

    def do_create(self, arg):
        """Creates a new instance"""
        if arg:
            if arg in self.classes:
                # instance = models.base_model.BaseModel()
                get_class = getattr(sys.modules[__name__], arg)
                instance = get_class()
                print(instance.id)
                models.storage.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")
        return

    def do_show(self, arg):
        """string representation of a class of a given id"""
        tid = shlex.split(arg)
        if len(tid) == 0:
            print("** class name missing **")
        elif len(tid) == 1:
            print("** instance id missing **")
        elif tid[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            dic = models.storage.all()
            k = tid[0] + '.' + str(tid[1])
            if k in dic:
                print(dic[k])
            else:
                print("** no instance found **")
        return

    def do_destroy(self, arg):
        """Deletes a class instance"""
        tidd = shlex.split(arg)
        if len(tidd) == 0:
            print("** class name missing **")
            return
        elif len(tidd) == 1:
            print("** instance id missing **")
            return
        elif tidd[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            dic = models.storage.all()
            k = tidd[0] + '.' + tidd[1]
            if k in dic:
                del dic[k]
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Represents string of all instances of the class"""
        tida = shlex.split(arg)
        lst = []
        dic = models.storage.all()

        if len(tida) == 0:
            for k in dic:
                rep_Class = str(dic[k])
                lst.append(rep_Class)
            print(lst)
            return

        if tida[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            rep_Class = ""
            for k in dic:
                className = k.split('.')
                if className[0] == tida[0]:
                    rep_Class = str(dic[k])
                    lst.append(rep_Class)
            print(lst)

    def do_update(self, arg):
        """Updates an instance."""
        tidu = shlex.split(arg)
        if len(tidu) == 0:
            print("** class name missing **")
            return
        elif len(tidu) == 1:
            print("** instance id missing **")
            return
        elif len(tidu) == 2:
            print("** attribute name missing **")
            return
        elif len(tidu) == 3:
            print("** value missing **")
            return
        elif tidu[0] not in self.classes:
            print("** class doesn't exist **")
            return
        k = tidu[0] + "." + tidu[1]
        d = models.storage.all()
        try:
            instu = d[k]
        except KeyError:
            print("** no instance found **")
            return
        try:
            typeA = type(getattr(instu, tidu[2]))
            tidu[3] = typeA(tidu[3])
        except AttributeError:
            pass
        setattr(instu, tidu[2], tidu[3])
        models.storage.save()

    def do_count(self, arg):
        """Retrieves the number of instances of a given class """
        tida = shlex.split(arg)
        dic = models.storage.all()
        num_inst = 0
        if tida[0] not in self.classes:
            print("** class doesn't exist **")
            return
        else:
            for k in dic:
                className = k.split('.')
                if className[0] == tida[0]:
                    num_inst += 1

            print(num_inst)


if __name__ == '__main__':
    """infinite loop"""
    HBNBCommand().cmdloop()
