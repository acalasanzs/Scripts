def staticinstance(method, clsA = False):
    @classmethod
    def wrapper(cls, *args, **kwargs):
        if(clsA and isinstance(cls, clsA)):
            return method(cls,*args,*kwargs)
        return method(None, *args, *kwargs)
    return wrapper