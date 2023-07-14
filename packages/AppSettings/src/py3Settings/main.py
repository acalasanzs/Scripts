import os
from typing import Any, Callable, List
import file
from operator import itemgetter
# from packages.AppSettings.utils import staticinstance
import re
class Attribute:
    def __init__ (self, attr: str, typ : Any | None = None, validate:  Callable[[object], bool] | None = None, default: bool = False, getter: Callable[[], Any] = None):
        self.attr = attr
        if typ is None and validate is Callable[[object], bool]:
            self.validate = validate
        elif validate is None and typ is not None:
            self.typ = typ
            self.validate = lambda a: isinstance(a, typ) if not hasattr(self, 'get') else self.get
            if getter is not None:
                self.get = getter
        else:
            raise SystemExit("No type!")
        self.default = default
def printObjProps(theObject):
    for property, value in vars(theObject).items():
        print(property, ":", value)
class Option():
    def __init__(self, name: str, optionName: str = "name", optionID: str | None = None):
        self.name = name
        self.optionName = optionName
        self.attributes = []
        self.default = None
        if optionID is None:
            raise SystemExit("No optionID!")
        self.optionID = optionID
    def append(self, attribute: Attribute):
        if self.default is None:
            self.default = attribute
        if attribute.default:
            self.default = attribute
        self.attributes.append(attribute)
def getWithAttr(list: list, attr: str, name: str):
    for x in list:
        if getattr(x, name) == attr:
            return x
    return False
def handle(format, dict:dict):
    ins = Handler(format)
    itemgetter(dict)(ins.init)
    return ins
class Handler:
    invalid = r'[<>:"/\|?* ]'
    def __init__(self, format: str):
        self.format = format
    def init(self, load: Callable[[str,str], dict], save: Callable[[dict], str | bool]):
        self.load = Handler.safeCheck(load)
        self.save = Handler.safeCheck(save)
    @staticmethod
    def safeCheck(fun):
        def wrapper(filename:str, *args, **kwargs):
            assert Handler.fileStr(filename)
            fun(filename, *args, **kwargs)
        return wrapper
    @classmethod
    def fileStr(cls, file: str) -> bool:
        file = file.split(".")
        if(len(file) != 2):
            return False
        filename = file[0].decode('utf-8','ignore').encode("utf-8")
        original = file[0]
        if re.search(cls.invalid, filename):
            return False
        if original != filename:
            return False
        return True
formats = [handle('.json',file.JSON)]
class AppSettings():
    def __init__(self, options: List[Option]):
        self.options = options
        self.dict = dict()
        self.defaults = dict()
    def loadFile(self, type: str, filename = "settings.json", path = os.getcwd() ):
        for x in formats:
            if x.format == type:
                return x.load(filename, path)
        return False
    def saveFile(self, type: str, data: dict, filename = "settings.json", path = os.getcwd()):
        for x in formats:
            if x.format == type:
                return x.save(data, filename, path)
        return False
    def load(self, filename = "settings.json", path = os.getcwd()):
        json = FileHandlers.loadJson(filename, path)
        assert isinstance(json, list)
        for i,statement in enumerate(json):
            for option in self.options:
                if option.optionName in statement and statement[option.optionName] == option.optionID:
                    for attr in statement.keys():
                        attr_get = getWithAttr(option.attributes, attr, 'attr')
                        val = attr_get.validate(statement[attr])
                        if attr in [x.attr for x in option.attributes] and not val:
                            raise SystemExit(f"Value ({statement[attr]}) [{i}] Validation Failure for {attr_get.attr} of {option.name}")
                        if callable(val):
                            statement[attr] = val()
                    self.dict[option.name] = statement
                    self.defaults[option.name] = statement[option.default.attr]
    def getSetting(self, name: str, attr: str | None):
        if attr is None:
            return self.defaults[name]
        return self.dict[name][attr]
    def getSettings(self):
        return self.dict
    def getDefaultSettings(self):
        return self.defaults
    def __str__(self):
        text = ""
        for property, value in vars(self).items():
            text += " ".join([str(x) for x in [property, ":", value]])
            text += "\n"
        return text
        