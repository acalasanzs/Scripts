import os
import json
def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]
def sure(all: bool = False, yes: chr = "y", no: chr = "N", always: chr = "O"):
    text = ""
    if all:
        text = f"/{always}"
    res = input(f"Continue({yes}/{no}{text})?")
    if (res.lower() == no.lower()):
        raise SystemExit()
    if all and (res == always):
        return True
    return False
