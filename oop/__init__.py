class Machine:

    def set_date_manufactured(self, date_manufactured):
        self.date_manufactured = 'Machine is manufactured on - ' + date_manufactured

    def print_date_manufactured(self):
        print(self.date_manufactured)


class Vehicle:

    # If no __init__ is present, class calls return an empty instance, without initializing it
    def __init__(self, num_of_wheels):
        self.num_of_wheels = num_of_wheels

    # class methods automatically receives a special first argument—called self by convention that provides a handle back to the instance to be processed
    def set_num_wheels(self, num_of_wheels):
        self.num_of_wheels = num_of_wheels

    def description(self):
        print('This is a Vehicle')

    def set_date_manufactured(self, date_manufactured):
        self.date_manufactured = 'Vehicle is manufactured on - ' + date_manufactured

    def print_date_manufactured(self):
        print(self.date_manufactured)

    def __str__(self):
        return 'This is a Vehicle!'


# In Python, if there is more than one superclass listed in parentheses in a class statement, their left-to-right order gives the order in which those superclasses will be searched for attributes by inheritance
class Plane(Vehicle, Machine):
    def __init__(self, num_of_wheels):
        Vehicle.__init__(self, num_of_wheels)       # call superclass's constructor

    def description(self):
        print('This is a Plane')
        Vehicle.description(self)           # call the superclass's description method

    def __str__(self):
        return 'This is a Plane, king of the skies!'

    def __repr__(self):
        """
        __repr__ method is often used to provide an as-code low-level display of an object when present, and __str__ is reserved for more user-friendly informational displays like ours here.
        Sometimes classes provide both a __str__ for user-friendly displays and a __repr__ with extra details for developers to view. Because printing runs __str__ and the interactive prompt
        echoes results with __repr__, this can provide both target audiences with an appropriate display.
        """
        return '[Plane] This is a Plane, king of the skies! Number of wheels - {}'.format(self.num_of_wheels)

    def __add__(self, other):
        return Plane(self.num_of_wheels + other)


Vehicle(5).description()
plane = Plane(2)
plane.description()

# plane.print_date_manufactured()                   # will thorw AttributeError: 'Plane' object has no attribute 'date_manufactured'

# class’s method can always be called either through an instance (the usual way, where Python sends the instance to the self argument automatically) or through the class
plane.set_date_manufactured('2019-09')
Plane.set_date_manufactured(plane, '2019-09')

plane.print_date_manufactured()
plane.date_manufactured = '1999-99'                 # Bypassing setter
plane.print_date_manufactured()

# Operator overloading
print(plane)                            # will execute __str__()
new_plane = plane + 99                  # Operator overloading at play, will execute __add__()
print(new_plane.num_of_wheels)
print(new_plane is plane)               # will return a new object because of the way __add__() is implemented

# Instances begin their lives as completely empty namespace objects. Because they remember the class from which they were made, though, they will obtain the attributes we attached to the class by inheritance
before_attr_assignment = Machine()
Machine.key = [1, 2, 3]       # Can set new attributes to class instance
after_attr_assignment = Machine()

# in this case, instances have no attributes of their own; they simply fetch the name attribute from the class object where it is stored
print('Machine.key - ', Machine.key)          # When looking for a name, Python checks the instance, then its class, then all superclasses.
print('before_attr_assignment - ', before_attr_assignment.key)
print('after_attr_assignment - ', after_attr_assignment.key)

Machine.key = None
print('\nbefore_attr_assignment - ', before_attr_assignment.key)
print('Machine.key - ', Machine.key)
print('after_attr_assignment - ', after_attr_assignment.key)

# If we do assign an attribute to an instance, though, it creates (or changes) the attribute in that object, and no other
Machine.key = (1, 2, 3)
before_attr_assignment.key = (1, 2, 3)
after_attr_assignment.key = (1, 2, 3)
Machine.key = None
print('\nbefore_attr_assignment - ', before_attr_assignment.key)
print('Machine.key - ', Machine.key)
print('after_attr_assignment - ', after_attr_assignment.key)

# Normally, __dict__ literally is an instance’s attribute namespace.
print('\nattribute namespace of before_attr_assignment = ', before_attr_assignment.__dict__.keys())
print('each instance has a link to its class - ', before_attr_assignment.__class__)


def upper(x):
    return x.__str__().upper()


# If we assign this simple function to an attribute of our class, though, it becomes a method, callable through any instance, as well as through the class name itself as long as we pass in an instance manually
plane.upper = upper
print('upper - ', plane.upper(plane))
