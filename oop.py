# superclasses order
class Dog(Animal, Pet):
    pass
print Dog.__mro__ # method resolution object

# supermethoding the right way
    def to_dict(self):
        data = super(self.__class__, self).to_dict()

## unpack arguments as a dict into line arguments
def say(what, **kargs):
    print what
say(what="ho ho ho!") 

# class of an instance
instance.__class__.__name__


