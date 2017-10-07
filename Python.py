#!/usr/bin/python
# -*- coding: latin-1 -*-

"""Example of using documentation strings."""

import sys
import os
# Add a relative path for imports
include_path = os.path.abspath(os.path.dirname(os.path.realpath(__file__)) + "\\includes")
sys.path = [include_path] + sys.path

import comtypes.client as CC
from legacy_module import *
from classes.dir import Dir
from .session import ( # import from current directory
    make_transient,
    make_transient_to_detached
)
from legacy_module import ClassA as ClassB
from builtins import range

# types: 
bool, int, float, long, complex,  str, unicode, list, tuple, bytearray, buffer, xrange, dict, set, frozenset
# see also collections
from datetime import datetime

# Constants:
None, True, False

# Bitwise operators:
<<, >>, &, |, ~, and ^

# Comparision:
==, !=, is, is not, >, <, >=, <=

# * and ** operators:
values1 = (1, 2)
values2 = { 'c': 10, 'd': 15 }
s = sum(*values1, **values2)
# would execute as:
s = sum(1, 2, c=10, d=15)
# ** as argument:
def get_a(**values):
    return values['a']
s = get_a(a=1, b=2)      # returns 1
def sum(*values):
    s = 0
    for v in values:
        s = s + v
    return s # returns the sum
s = sum(1, 2, 3, 4, 5)

# Assignments:
# Call by reference { C++ example: GetSize(&left, &right, &top, &bottom); }
left, right, top, bottom = GetSize() # Exception indicates error.
i = 2
j = i # copies 2 in j
i = [1,2,3]
j = i # copies the reference to [1,2,3]
del j # empty j
*elem, = range(5) # same as [*elem,]= and (*elem,)=   # results in elem=[0, 1, 2, 3, 4]
import copy
j = copy.copy(i) # makes a copy of [1,2,3]
j = copy.deepcopy(i) # used for copying an object and objects within

# String '' == ""
sz = r'\allo\'' # string is as is except \' that is transformed to '
sz = '\allo\'' # the \ are treated as escape sequences \' -> ' and \a -> \x07
s = ("this is a very"
     "long string too"
     "for sure ..."
     )

# printing
print("{0}, {1}".format(x[0], x[1], y))
print '%d,%d,%s' % (*x, y) # % sign and tupple 

# tupple
a = (1,) # tupple of one element
x = (2, 3) # tupple of 2 elements
y = 3
(x[0], x[1], y) == (x + (y,)) == (*x, y) # * = iterable unpacking operator

# dictionnary
old_list = {} # initialisation of a dict preferred
new_list = dict() # initialisation of a dict (do not use)
from collections import OrderedDict
ord_list = OrderedDict()
dictData = {
            'item1': 1,
            'item2': 2,
}
dictData['item3'] = 3
dictData.update({'item4': 4, 'item5': 5})
item3 = dictData['item3']
if 'item3' in dictData:
    print(dictData['item3'])
if not dictData:
  print("dict is empty")
my_dict.pop('key', None) # return my_dict[key] if key exists and None otherwise
for team, runs in league.iteritems():
    pass
  
# list
old_list = [] # initialisation of a list
if not old_list:
  print("List is empty")
xi = [None] * 10 # create empty list of 10 elements
xi = [x*x for x in range(30)]
old_list.append('object')
new_list = old_list # !!!! This does not actually copy the list !!!!
new_list = list(old_list) # This does copy the list
new_list = old_list[:] # copy the list but weird syntax not to be used?
new_list = old_list[:-1] # copy the list except the last element (or character)
a = xi[:10,None] # create a list of list with 10 elements from xi
r = [float(i) for i in lst] # conversion list of string to list of float
[ EXP for x in seq if COND ] # list with filter
[x for x in range(1, 10) if x % 2] # outputs: [1, 3, 5, 7, 9]
[False, True][Expression] # another form
[[x*100, x][x % 2 != 0] for x in range(1,11)] # outputs: [1, 200, 3, 400, 5, 600, 7, 800, 9, 1000]
3 in [1, 2, 3] # => True (Checking if something is inside)
[1,2,3].index(2) # => 1

# named tuple:
from collections import namedtuple
Record = namedtuple("MyNamedTuple", ["ID", "Value", "Name"])
tPoint = namedtuple('Point', ['x', 'y'], verbose=True, rename=True) # rename in case of an invalid identifier
Point.__new__.__defaults__ = (None,) * len(Point._fields)
p=Point()
x = p.x
tuplePi = (1, 3.14, "pi") # normal tuple
name = tuplePi[2]
p=Record(*tuplePi) # == MyNamedTuple(ID=1, Value=3.14, Name='pi')
p=Record._make(tuplePi) # == MyNamedTuple(ID=1, Value=3.14, Name='pi') But like a cast?
print Record._fields
dict = p._asdict()

# does variable exists:
try:
    thevariable
except NameError:
    print "well, it WASN'T defined after all!"
else:
    print "sure, it was defined."

# generator
mygenerator = (x*x for x in range(3)) # can only be used once!?
# Yield is a keyword that is used like return, except the function will return a generator
def iter_integers(): # function that returns as soon as it its yield and resumes at yield if called again
    """Infinite sequence of integers."""
    i = 1
    while True:
        yield i
        i = i + 1

output = type(argsList[0])() # define a variable of a certain type (e.g. int() float()...)
if type(i) is long: break
print(repr(output)) # print the type of output in text

# if-then-else
if fruit == 'Apple':
    isApple = True
elif fruit == None:
    isApple = None
else:
    isApple = False
# value_when_true if condition else value_when_false
isApple = True if fruit == 'Apple' else False

# for-loop:
for element in [1, 2, 3]:
    print element
    if element == 2: break
    if element == 1: continue
for element in (1, 2, 3):
    print element
for key in {'one':1, 'two':2}: # This loops over the keys
    print key
for char in "123":
    print char
for line in open("myfile.txt"): # Loops over the lines of the file
    print line
for x, y in itertools.izip(["a", "b", "c"], [1, 2, 3]):
    print(x,y)
for i, value in enumerate(["a", "b", "c"]):
    print(i, c)
[thing for thing in list_of_things] # one line
    
# do-while:
while True:
    i=i+1
    if i == 10: continue
    if(i>20): break
    time.sleep(0.5)

# with:
with open('out.txt', 'w') as of: 
    #This makes sure the file is properly closed when the block inside with exits, even if exceptions are thrown. 
    of.write('222')

# Generate exception:
raise ValueError('A very specific bad thing happened')

# try:
import traceback
try:
# Generate exception:
    assert (Temperature >= 0),"Colder than absolute zero!" # generates AssertionError
    raise EOFError
    raise IndexError
    raise KeyError('non-alphanumeric character in input')
    raise NameError
    raise NotImplementedError
    raise SyntaxError('%s/%s does not define class %s' % (__name__, py, clsn))
    raise ValueError('A very specific bad thing happened')
except (ValueError, KeyError):
    tb = traceback.format_exc() # get the trace stack
except Exception as e: # Exception is the base class of all exceptions
    print(e)
else:
    tb = "No error"
finally:
    print(a)
    
# unamed function:
g = lambda x: expint(3, x)
g(8) # equal 64
adder_lambda = lambda parameter1,parameter2: parameter1+parameter2

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
    return 1
for char in reverse('golf'):
    print char

def outer():
    x = 1
    def inner():
        nonlocal x  
        x = 2 # changes outer.x
        global x
        x=3 # changes global.x
    
def deferred(*args, **kwargs):
    r"""
    :param \*args: columns to be mapped passed as list  
    :param \**kwargs: additional keyword arguments passed as dict
    """
    return ColumnProperty(deferred=True, *args, **kwargs)

def __private(self): # __ = Private function : cannot be called outside of module
    return True

import weakref

##### @ decorator: #####

def decorator(func):
   return func
@decorator
def some_func():
    pass

#>>>> Is equivalent to this code:
def decorator(func):
    return func
def some_func():
    pass
some_func = decorator(some_func)

##### class: #####
class Person:
   'Common base class for all employees'
    empCount = 0
    
    def __init__(self, name, parent):
        self.name = name
        self.parent = weakref.ref(parent) # avoid circular reference to make sure destructor is called
        Person.empCount += 1

    def displayCount(self):
        print("Total Persons %d" % Person.empCount)
    
    def displayPerson(self):
        print("Name : ", self.name)
       
    @classmethod # used to provide another constructor for the class 
    def from_string(cls, person_as_string):
        name, parent = split(person_as_string)
        ret1 = cls(name, parent) # use the standard init 
        return ret1

    @staticmethod # used to add a static function to the class
    def is_name_valid(person_as_string): 
        name, parent = split(person_as_string)
        return name.len > 0 and parent.len > 0
    
    # @property(fget=None, fset=None, fdel=None, doc=None):
    def get_temperature(self):
        return self._temperature
    temperature = property(get_temperature) # adds a temperature property to the class
    ############ OR (recommended): #############
    @property   # see also @temperature.setter
    def temperature(self):
        return self._temperature

      
class builtinclass(object):
    __slots__ = ("filled", "used", "mask", "table") # Fix the number of attributes no dict will be used
    """Class methods are similar to regular functions.
    
    object: builtin base class for all classes
    
    Note:
        Do not include the `self` parameter in the ``Args`` section.
    
    Args:
        param1: The first parameter.
        param2: The second parameter.
    
    Returns:
        True if successful, False otherwise.
    
    """
    def __new__(cls): # called before init 
        # create our object and return it
        obj = super().__new__(cls)  # must be derived from at least object for this to work.
        return obj
    
    def __init__(self, *args, **kwargs):  # called after __new__ when class has been created
        super().__init__(*args, **kwargs) # super() refers to the parent class
        self.__dict__ = dict([('bibi', 1), ('df',2)]) # Wow: creates attributes to this class
        
    def _private(self): # _ = Private function (actually callable, this is only a convention)
        return True

    def __unique(self): # __ = Not Overloadable function (actually callable with _builtinclass__private)
        return True      # Otherwise the function is overloadable by parent class
        
    def __class__(self):
        return(type(builtinclass))
    
    def __call__(self): # Overload () operator
        return True
    
    def __str__(self): # for print(), Optionnal if __repr__ defined.
     return "foo"
 
    def __repr__(self, *args, **kwargs):
        return object.__repr__(self, *args, **kwargs)
    
    def __doc__(self):
        return builtinclass.__doc__(self)
    
    def __setitem__(self, key, item): # dict type assignment
        self.data[key] = item
    
    def __getitem__(self, key, item): 
        return(self.data[key])
    
    def __getattr__(self, name):
        raise AttributeError
    
    def __setattr__(self, name, value):
        raise AttributeError
    
    def __len__(self): # used by the len() function
        return self._data_len
    
    def __iter__(self): # for iterations see http://anandology.com/python-practice-book/iterators.html
        # see also yield
        return self

    def next(self): # goes with __iter__
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration() # no more elements
    
    def __del__(self):
        print self.id, 'died'
    
    # Operators overloading: __sub__, __sum__
    def __sub__(self, other):               # on instance - other
        return Number(self.data - other)    # result is a new instance
    
    __dict__ # Contains all attributes of the object -> Can be changed!
    __rsub__ = __sub__ # for 'int * self' per example
    __class__.__name__ # Contains the name of the class

# Wrapping:

def trace_in(func, *args, **kwargs):
   print "Entering function",  func.__name__
def trace_out(func, *args, **kwargs):
   print "Leaving function", func.__name__

@wrap(trace_in, trace_out)
def calc(x, y):
   return x + y

# neat functions:
# https://docs.python.org/2/library/functions.html
a = [25.75443, 26.7803, 25.79099, 24.17642, 24.3526, 22.79056, 20.84866, 19.49222, 18.38086, 18.0358, 16.57819, 15.71255, 14.79059, 13.64154, 13.09409, 12.18347, 11.33447, 10.32184, 9.544922, 8.813385, 8.181152, 6.983734, 6.048035, 5.505096, 4.65799]
min(iterable, *)
min(range(len(a)), key=lambda i: abs(a[i]-11.5))
range([start], stop[, step])
enumerate(sequence, start=0) # returns a generator with a tuple(n, elem) (see yield)
', '.join(row) # joins all components of row with ,
itercars = iter(cars) # can be used in for loops
next(itercars) # skip first item in iteration
[a*b for a,b in zip(lista,listb)]
Table = sorted(Table, key=lamdba element: element[3])
v = memoryview(b'abcefg')

# Conditionnal includes:
import sys
modulename = 'csv'
if modulename not in sys.modules:
    'You have not imported the csv module' 
else:
    def ReadCSVtoTable(szFilename):
        pass
    
# See https://blog.ionelmc.ro/2013/06/05/python-debugging-tools/    
if __debug__: # This is like preprocessed
    import pdb; pdb.set_trace()
    try:
        pass
    except ZeroDivisionError: # debugger with (c)ontinue, (n)ext, (s)tep, <ctrl-D>:
        import IPython; IPython.embed()
    print "If this prints, you're not running python -O."
else:
    print "If this prints, you are running python -O!"
dir(__builtins__) # Lists all functions of an object
vars(__builtins__) # List all variables of an object
import inspect
inspect.getsourcelines(foo) # get source code of foo function

if __name__ == "__main__":
    # execute only if run as a script
    main()
    

