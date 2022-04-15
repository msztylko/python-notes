# the metaclass will automatically get passed the same argument
# that you usually pass to `type`

def upper_attr(future_class_name, future_class_parents, future_class_attrs):
    """
    Return a class object, with the list of its attributes turned into uppercase
    """
    # pick any attribute that doesn't start with '__' and uppercase it
    uppercase_attrs = {
        attr if attr.startswith('__') else attr.upper(): v
        for attr, v in future_class_attrs.items()
    }
    # let `type` do the class creation
    print(uppercase_attrs)
    return type(future_class_name, future_class_parents, uppercase_attrs)

__metaclass__ = upper_attr # this will affect all classes in the module

class Foo():
    bar = 'baz'
    
print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))
print(Foo.BAR)