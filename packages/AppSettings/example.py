from main import AppSettings, Option, Attribute
from typing import Callable, List
import os
options: List[Option] = list()
content = Option("content","warn","Already with content in it!")
content.append(Attribute("ask", bool))
exists = Option("exists","warn","{x} already exists!")
exists.append(Attribute("ask", bool))
settingsProxy = AppSettings([content,exists])
settingsProxy.load("sure.json", r"G:\Documents\Scripts\packages\AppSettings")
print(settingsProxy)