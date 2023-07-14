class staticinstance:
    def __init__(self, method):
        self.method = method
    def __set_name__(self, owner, name):
        self.cls = owner
    def __call__(self, *args, **kwargs):
        if(isinstance(args[0], self.cls)):
            return self.method(*args, **kwargs)
        return self.method(None, *args, **kwargs)