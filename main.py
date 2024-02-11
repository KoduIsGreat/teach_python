# printing hello world

print('Hello World')

# variable declaration
fooInt = 1
print(fooInt)
fooFloat = 1.3
print(fooFloat)
fooBool = True
print(fooBool)
fooString = 'Hello World'
print(fooString)
fooFormatString = f'Hello World, {fooInt}'
fooBytes = b'Hello World'
fooBinaryString = b'Hello World'

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


def my_function():
    """
    This is a docstring it will show up in auto complete and helpers
    """
    print('Hello from my_function')


my_function()


def my_function_with_args(a, b):
    """
    a is a list, b is a dictionary
    """
    print(f'Hello from my_function_with_args, a = {a}, b = {b}')


my_function_with_args(my_list, my_dict)


def add(a, b):
    """
    Sums a and b
    """
    return a + b


c = add(3, 4)

print('c is ', c)

# functions can return multiple values (tuples)


def add_and_subtract(a, b):
    """
    Sums a and b, and subtracts a and b
    """
    return a + b, a - b


sum, difference = add_and_subtract(2, 4)

print(f'sum={sum}, difference={difference}')

# Class examples


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
