# To create a regular class
class Coffee:
    def __init__(self, name, price):
        """__init__ is a special dunder method* to add values to the object

        Unlike other programming language, python classes do not need to be initialized and
        the __init__ method simply acts as an initializer

        Note: __init__ always returns None, do not return any value(s)
        """

        # The variable below is known as instance property as it's unique to an object
        self.name = name
        self.price = price

    # Similarly the method is known as instance method as it's also unique to the object
    def get_name(self):
        return self.name

    # The method will print out the price depending upon the discount applied  (or not applied)
    def get_price(self):

        # hasattr returns true if a class object has the property within it.
        if hasattr(self, '_discount'):
            return self.price - self._discount
        else:
            return self.price

    # Another way of initializing property other than using __init__
    def add_discount(self, discount):
        """This method creates a property outside of the __init__ method.

        This method has a _ in front of _discount which is used to denote other developers that this property
        is similar to a private scope property and should not be used outside of the class's logic

        Possible error occurs if the property is called before executing this function
        """
        self._discount = discount

    # Use __ to make a private variable (so that the method is hidden from other classes)
    __coffeelist = None

    # Static method is a method that is independent to the class and can be only invoked once
    # thus to access a singleton object

    @staticmethod
    def get_coffee_list():
        if Coffee.__coffeelist == None:
            Coffee.__coffeelist = []
        return Coffee.__coffeelist

    # This is a class variable since it's unique to the class and not the instantiated object
    PRODUCT_TYPE = ("Coffee", "Cakes", "Sandwich")

    # Class methods are declared using @classmethod decorator, the cls parameter represents the cls object
    # class variables can be accessed using the cls.variablename as given below
    @classmethod
    def get_products_list(cls):
        return cls.PRODUCT_TYPE


# The class below inherits the coffee class
class Cafe(Coffee):
    pass


# Create instance of the class
sc = Coffee("Cafe Latte", 3.75)
print(sc.get_name())
print(sc.get_price())

cof2 = Coffee("Mocha", 4.25)
print(cof2.get_name())
cof2.add_discount(.35)
print(cof2.get_price())
print(cof2.get_products_list())

coffeelist = Coffee.get_coffee_list()
print(coffeelist)
coffeelist.append(sc)
coffeelist = Coffee.get_coffee_list()
coffeelist.append(cof2)
print(coffeelist)
# type functions allows to determine the class of the instance
# returns a object
print(type(cof2))

# isinstance function can be used to determine if a object is an instance of a class
# returns a boolean
print(isinstance(sc, Coffee))


"""Notes

Dunder Methods or double underscore methods:
These methods are unique method which python interprets as 

"""
