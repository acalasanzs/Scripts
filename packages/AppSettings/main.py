import json, os
from typing import Any, Callable, List
# from packages.AppSettings.utils import staticinstance

class Attribute:
    def __init__ (self, attr, typ : type | None, validate:  Callable[[object], bool] | None, default: bool = False):
        self.attr = attr
        if typ is None and validate is Callable[[object], bool]:
            self.validate = validate
        elif validate is None and typ is type:
            self.validate = lambda a: a is typ
        else:
            raise SystemExit("No type!")
class Option():
    def __init__(self, name: str, optionName: str = "name"):
        self.name = name
        self.optionName = optionName
        self.attributes = []
        self.default = None
    def append(self, attribute: Attribute):
        if self.default is not None:
            self.default = attribute
        if self.default is None and attribute.default:
            self.default = attribute
        self.attributes.append(attribute)
class AppSettings():
    def __init__(self, options: List[Option]):
        self.options = options
        self.dict = dict()
    def load(self, filename = "settings.json", path = os.getcwd()):
        json = AppSettings.loadJson(filename, path)
        assert json is list
        for i,statement in enumerate(json):
            for option in self.options:
                if option.optionName in statement:
                    for attr in statement.keys():
                        if attr in option.attributes and not option.attributes[attr].validate(statement[attr]):
                            raise SystemExit(f"{statement[attr]} [{i}] Validation Failure for {option.attributes[attr].attr}")
                    self.dict[option.name] = statement
    def getSetting(self, name: str, attr: str | None):
        return self.dict[attr]
    @staticmethod
    def loadJson(filename = "settings.json", path = os.getcwd()):
        return json.load(open(os.path.join(path,filename)))
        