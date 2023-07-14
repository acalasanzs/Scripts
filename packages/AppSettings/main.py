import json, os
from typing import Any, Callable, List
# from packages.AppSettings.utils import staticinstance

class Attribute:
    def __init__ (self, attr, typ : type | None, validate:  Callable[[object], bool] | None]):
        self.attr = attr
        if typ is None and validate is Callable[[object], bool]:
            self.validate = validate
        elif validate is None and typ is type:
            self.validate = lambda a: a is typ
        else:
            raise SystemExit("No type!")
class Option():
    def __init__(self, name: str):
        self.name = name
        self.attributes = []
    def append(self, attribute: Attribute):
        self.attributes.append(attribute)
class AppSettings():
    def __init__(self, options: List[Option]):
        pass
    @staticmethod
    def load(filename = "settings.json", path = os.getcwd()):
        return json.load(open(os.path.join(path,filename)))
        