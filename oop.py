class BaseClass:
    def __init__(self):
        print("Initializing BaseClass")


class DerivedClass(BaseClass):
    def __init__(self):
        # Call the __init__ method of the base class
        super().__init__()
        print("Initializing DerivedClass")


# Creating an instance of the derived class
obj = DerivedClass()
