##Following sets of examples are originally from 'Corey Schafer's Python Guide', playlist from Youtube tweaked by me
for num in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
   print(num)
#-------------------------------------------------------------------------------------
message = "Hello World"

print(len(message))
print(message[:5])
print(message[6:])
#-------------------------------------------------------------------------------------
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[-2:1:-1])
#-------------------------------------------------------------------------------------
sample_url = "https://inventwithpython.com"
print(sample_url[8:-4:])
#-------------------------------------------------------------------------------------
message = "Hide a tree in a forest, Hide a ship in ships."
print(message.count("s"))
parallel_universe_message = message.replace('ships', 'docks')
print(parallel_universe_message)
#-------------------------------------------------------------------------------------
hello = "Greetings"
name = "dear customer"

automated_store_message = "{} {}! Would you like to have Senbei or Okaki?".format(hello, name)
print(automated_store_message)
#-------------------------------------------------------------------------------------
##formating
person = {'name': 'Jenn', 'age': 23}
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person)
print(sentence)
#-------------------------------------------------------------------------------------
tag = "hl"
text = "This is a headline"

sentence = "<{0}> {1} <{0}>".format(tag, text)
print(sentence)
#-------------------------------------------------------------------------------------
class Person():

   def __init__(self, name, age):
       self.name = name
       self.age = age

person_one = Person('Shanks', '39')
person_two = Person('Luffy', '19')

sentence_one = 'My name is {0.name} and I am {0.age} years old.'.format(person_one)
sentence_two = 'My name is {0.name} and I am {0.age} years old.'.format(person_two)
print(sentence_one)
print(sentence_two)
#-------------------------------------------------------------------------------------
person = {'name': 'Jenn', 'age': 23}
sentence = 'My name is {name} and I am {age} years old.'.format(**person)
print(sentence)
#-------------------------------------------------------------------------------------
for i in range(1, 11):
   counter = 'The value is {}'.format(i)
   print(counter)
#-------------------------------------------------------------------------------------
pi = 3.14159265

sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence)
#-------------------------------------------------------------------------------------
sentence = '1 MB is equal to {:,} bytes'.format(1000 ** 2)
print(sentence)
#-------------------------------------------------------------------------------------
import datetime

my_date = datetime.datetime(1513, 5, 5, 10, 20, 56)
print(my_date)
##Reshaping the output to example: 'Month XX, XXXX' format
reformatted = '{:%B %d, %Y}'.format(my_date)
print(reformatted)

##Reshaping the output to example: 'Month XX, XXXX fell on a Day and was the XXX day of the year' format
sentence = '{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year'.format(my_date)
print(sentence)
#-------------------------------------------------------------------------------------
##f string

greeting = 'Greetings dear customer'
statement = 'Welcome to the world of the future!'

message = f'{greeting}, {statement}. Please mark the locations you wished to visit and enjoy the ride.'

print(message)
#-------------------------------------------------------------------------------------
##Arithmetic Operators: # $ #
##Addition:             3 + 2
##Subtraction:          3 - 2
##Multiplication:       3 * 2
##Division:             3 / 2
##Floor Division:       3 // 2
##Exponent:             3 ** 2
##Modulus:              3 % 2

num = 1
num *= 10

print(num)

print(abs(-24))

print(round(3.53286575, 2))
#-------------------------------------------------------------------------------------
##Comparisons:          # ? # **returns Boolean**
##Equal:                3 == 2
##Not Equal:            3 != 2
##Greater Than:         3 > 2
##Less Than:            3 < 2
##Greater or Equal:     3 >= 2
##Less or Equal:        3 <= 2

num_1 = '56'
num_2 = '29'

print(num_1 + num_2) will end up concatenating strings
data type should be converted to an 'int'

n_1 = int(num_1)
n_2 = int(num_2)
print(n_1 + n_2)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Geography']
nums = [1, 6, 5, 7, 4, 9, 2, 3, 8]
#-------------------------------------------------------------------------------------
##Adding Values:
courses.append('Art')
courses.insert(0, 'Art')
courses.insert(0, courses_2) #Does not add elements individually but appends the list as a whole; hence the use of 'extend' method.
courses.extend(courses_2)
#-------------------------------------------------------------------------------------
##Removing Values:
courses.remove('Math')
popped = courses.pop()
print(popped)
#-------------------------------------------------------------------------------------
##Sorting Values:
courses.reverse()
courses.sort()
nums.sort()
Changing the order of sorting:
courses.sort(reverse=True)
nums.sort(reverse=True)
sorted_c = sorted(courses)
sorted_n = sorted(nums)

print(sorted_c)
print(sorted_n)
print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('CompSci'))
print('Art' in courses)
print('Math' in courses)
#-------------------------------------------------------------------------------------
courses = ['History', 'Math', 'Physics', 'CompSci']

for index, course in enumerate(courses, start= 1):
   print(index, course)
#-------------------------------------------------------------------------------------
##Refactoring a list into a string
course_str = ' - '.join(courses)
print(course_str)
Converting a string into a list
new_list = course_str.split(' - ')
print(new_list)

##*** Consider using 'list/s' upon the need of modification***
##*** Consider using 'tuple/s' upon the need of looping through and access***
#-------------------------------------------------------------------------------------
##Mutable:
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'
print(list_1)
print(list_2)
#-------------------------------------------------------------------------------------
##Immutable:
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art' #Tuple does not support item assignment hence there will be a Type Error
print(tuple_1)
print(tuple_2)
#-------------------------------------------------------------------------------------
##***Sets are values that are unordered have no duplicates***
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))
#-------------------------------------------------------------------------------------
##Creating empty; lists, tuples, sets:
Empty Lists
empty_list = []
empty_list_2 = list()

Empty Tuples
empty_tuple = ()
empty_tuple_2 = tuple()

Empty Sets **
empty_set = {} # NOT an empty set, an empty dictionary
empty_set_2 = set()
#-------------------------------------------------------------------------------------
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}

print(student['name'])
print(student['age'])
print(student['courses'])
print(student.get('name'))
print(student.get('phone', 'Not Found'))
student['phone'] = '555-5555'
student['name'] = 'Franky'
print(student.get('phone', 'Not Found'))                ##***Takes the second argument as a value only if there is none given by default***
print(student)

##Update method allows user to have more configuration over the specific dictionary
student.update({'name': 'Franky', 'age': 35, 'courses': ['Physics', 'CompSci', 'Math', 'Chemistry'], 'phone': '568-8888'})
del student['age'] removes the key directly
print(len(student))
print(student.keys())
print(student.values())
print(student.items())            ##**Returns key and value pairs**
#-------------------------------------------------------------------------------------
##Looping through key and values
for key in student:
    print(key)        #We don't want just keys

for key, value in student.items():
    print(key, value)
#-------------------------------------------------------------------------------------
##If / else statements
##Comparisons:
##Equal:            ==
##Not Equal:        !=
##Greater Than:     >
##Less Than:        <
##Greater or Equal: >=
##Less or Equal:    <=
##Object Identity:  is

language = 'Java'

if language == 'Python':
    print('Conditional was True')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')
#-------------------------------------------------------------------------------------
## 'and', 'or', 'not':
user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

user = 'Admin'
logged_in = False

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

user = 'Admin'
logged_in = False

if not logged_in:
    print('Please Log In')
else:
    print('Welcome')
#-------------------------------------------------------------------------------------
##***Difference between '==' and 'is'*** is checks for id
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(id(a))
print(id(b))
print(a is b)

a = b
print(a is b)
#-------------------------------------------------------------------------------------
##Values that evaluate to False: ***Everything else by default evaluate to True***
##False
##None
##Zero of any numeric type
##Any empty sequence. For example, '', (), [].
##Any empty mapping. For example, {}.

condition = ''

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
#-------------------------------------------------------------------------------------
##loops
##***'break' quits the loop, while 'continue' moves on with the next iteration***
nums = [1, 2, 3, 4, 5]

for num in nums:
    for letter in 'abc':
        print(num, letter)

x = 0

while x < 10:
    print(x)
    x +=1
#-------------------------------------------------------------------------------------
##Functions
##Keep your code 'DRY' --do not repeat yourself
def hello_func():
    print('Hello Function!')

hello_func()

*****We can treat the 'return' value just like the data type which it is, understanding this will allow users to chain together some functionality.*****
def hello_func(greeting):
    return '{} Function.'.format(greeting)

print(hello_func('Greeting'))
#-------------------------------------------------------------------------------------
def student_info(*args, **kwargs):
    print(args)               # A tuple with positional arguments
    print(kwargs)             # A dictionary with all of our keyword values

student_info('Math', 'Art', name='John', age=22)

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(courses, info)        # if we do not use '*' or '**' with our arguments, function won't unpack the values and pass them in individually
student_info(*courses, **info)      #***** 'args' represent positional arguments whereas 'kwargs' represent keyword arguments. When a '*' or '**' used in this context it will unpack a sequence or a dictionary and pass those values to the function individually.*****
#-------------------------------------------------------------------------------------
##Let's manually create two functions; one calculating if a year is a leap year or not, and the other calculates how many days are there in a specific month
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
##Number of days per month. First value placeholder for indexing purposes.

def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month and in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


print(is_leap(1524))
print(days_in_month(1122, 2))
print(days_in_month(1524, 2))
#-------------------------------------------------------------------------------------
##Importing Modules
## Let's consider the code underneath to be our module which we wish to import.
## 'CompSci' module
print('Imported my_module...')

test = 'Test String'

def find_index(to_search, target):
    """Find the index of a value in a sequence"""
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
