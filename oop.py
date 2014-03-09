# superclasses order
class Dog(Animal, Pet):
    pass
print Dog.__mro__ # method resolution object

## unpack arguments as a dict into line arguments
def say(what, **kargs):
    print what
say(what="ho ho ho!") 