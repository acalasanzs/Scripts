import json, os
from packages.AppSettings.utils import staticinstance

class Attribute():
    def __init__(self, attr, validate):
        self.attr = attr
        self.validate = validate
class Option():
    def __init__(self, name: str):
        self.name = name
    def append(self, name, option):
        pass
class AppSettings():
    def __init__(self, options: list):
        pass
    @staticinstance
    def load(self, filename = "settings.json", path = os.getcwd()):
        return json.load(open(os.path.join(path,filename)))
        