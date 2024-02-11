# This is a comment, it will not be executed
# but it will show up in the code editor
# below are some examples of python code

# print example the simplest python program
print('Hello World')

# variable declaration
fooInt = 1  # int
print(fooInt)

fooFloat = 1.3  # float
print(fooFloat)

fooBool = True | False  # bool
print(fooBool)

fooString = 'Hello World'  # string
print(fooString)

fooFormatString = f'Hello World, {fooInt}'  # formatted string
fooBytes = b'Hello World'  # bytes

none = None  # None eg represents null, nil or undefined

sum = fooInt + fooFloat

# list and dictionary declaration
my_tuples = (1, 3)

# my_tuples[0] = 2
print(my_tuples)
my_list = [1, 2, 3, 4, 5]

my_list[0] = 2
print(my_list)

my_dict = {
    'a': 3,
    'b': 'biskit',
    'c': 5,
}

# loop examples

# for loop example
print('for loop example')
for i in range(5):
    print(i)

# while loop example
print('while loop example')
i = 0
while i < 5:
    print(i)
    i += 1

# loop over list example
print('loop over list example')
for i in my_list:
    print(i)

# loop over dictionary example
print('loop over dictionary keys example')
for k in my_dict.keys():
    print(k)

print('loop over dictionary values example')
for v in my_dict.values():
    print(v)

print('loop over dictionary items example')
for k, v in my_dict.items():
    print(k, v)
# Control Flow examples
# if example
if sum > 2:
    print('sum is greater than 2')

if sum < 2:
    print('sum is less than 2')
elif sum == 2:
    print('sum is equal to 2')
else:
    print('sum is not less than 2')
    # match case example
print('match case example')
for k in my_dict.keys():
    match(k):
        case 'a':
            print(my_dict[k] + 2)
        case 'b':
            print(my_dict[k])
        case 'c':
            print(my_dict[k] % 3)

# Walrus example,
if len(my_list) > 3:
    print(f'List is too long ({len(my_list)} elements, expected <= 3)')

# walrus operator example
if (n := len(my_list)) > 3:
    print(f'List is too long ({n} elements, expected <= 3)')

# Function Examples
# Functions are defined using the def keyword


def my_function():
    """
    This is a docstring it will show up in auto complete and helpers
    """
    print('Hello from my_function')


my_function()

# Functions can take arguments


def my_function_with_args(a, b):
    """
    a is a list, b is a dictionary
    """
    print(f'Hello from my_function_with_args, a = {a}, b = {b}')


my_function_with_args(my_list, my_dict)

# Functions can return values


def add(a, b):
    """
    Sums a and b
    """
    return a + b


c = add(3, 4)

print('c is ', c)

# Functions can return multiple values


def add_and_subtract(a, b):
    """
    Sums a and b, and subtracts a and b
    """
    return a + b, a - b


sum, difference = add_and_subtract(2, 4)

print(f'sum={sum}, difference={difference}')

# Class examples
# The purpose of a class is to define a blueprint for objects
# An object is an instance of a class that has attributes and methods
# An attribute is a variable that is part of the class
# A method is a function that is part of the class
# The __init__ method is a special method that is called when an object is created
# It is used to initialize the object's attributes
# The __init__ method is called a constructor
# The self parameter is a reference to the current instance of the class, and
# is used to access variables that belong to the class.


# To initialize a rat call its constructor with a name parameter
# rat = Rat('Fanny the smelly rat')
class Rat:
    name = 'Rat'
    age = 3

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f'Hello, my name is {self.name}, I am {self.age} years old')


rat = Rat('Fanny the smelly rat')

palm = Rat('Palm the dirty rat')

mur = Rat('Mur the awesome rat')

rat.greet()
palm.greet()
mur.greet()

# file reading
with open('test.txt') as f:
    print(f.read())

# file writing
with open('my_written.txt', 'w') as f:
    f.write('Hello World')


# Type Hints

# variable
anInt: int = 3
# uncomment to see the error
# anInt = '3'

# function parameters and return


def add_with_type_hints(a: int, b: int) -> int:
    return a + b

# class attributes and methods


class Dog:
    name: str
    age: int = 3

    # here you can define the type of the parameter to the constructor as well
    # as a default value
    def __init__(self, name: str = 'Dog'):
        self.name = name

    def greet(self) -> None:
        print(f'Hello, my name is {self.name}, I am {self.age} years old')


# will have the name 'Dog' and age '3' by default
dog = Dog()
dog.greet()
