# Anything starts with a hash is python comment
import math  # import math module
print('Everybody is here loves python.')
print(100)
print(True)
# Data types: Numbers(Int, Float, complex), strings, Booleans, list, tuples, dict
# set, named tuples
​
# Declaring variables
first_name = 'Asabeneh'  # Strings
last_name = 'Yetayeh'  # Strings
gravity = 9.8  # Number float
age = 250  # Number, Int
cpx = 1 + 1j  # Complex
country = 'Finland'
is_married = True  # Boolean
skills = ['Python', 'R', 'SQL', 'TensorFlow']  # list
person = {
    'first_name': 'Asabene',
    'last_name': 'Yetaye',
    'age': 250,
    'is_married': True,
    'skills': ['Python', 'R', 'SQL', 'TensorFlow']
}  # Dictionary
print(first_name)
print(last_name)
print(country)
print(is_married)
​
person_info = "I am {}. I am {}. I live in {}".format(first_name, age, country)
print(person_info)
​
# Checking data types
print(type(first_name))
print(type(age))
print(type(gravity))
print(type(cpx))
print(type(skills))
​
# Operators:+, -, *, /, %
num_one = 3
num_two = 2
total = num_one + num_two
diff = num_one - num_two
prod = num_one * num_two
div = num_one / num_two
remainder = num_one % num_two
exp = num_two ** num_one  # 2 * 2 * 2= 2^3
# Comparison operators: > , < , >= <= ==, !=
print(3 > 2)
print(3 >= 2)
print(2 < 3)
print(2 <= 3)
print(2 == 3)
print(2 != 3)
print(True)
# Comparison: and, or, |, !
​
# conditional
is_raining = True
if is_raining:
    print('Take you umbrella with you')
else:
    print('Go out freely')
​
weather = 'rainy'
if weather == 'rainy':
    print('Go with you umbrella')
elif weather == 'sunny':
    print('It is a shinny day.')
else:
    print('Go freely')
​
​
print('do something') if True else 'do something else '
​
print(type(first_name) == str)
# Loops
for i in range(0, 11, 3):
    print(i)
​
i = 0
while i < 10:
    print(i)
    i += 1
# List
​
names = ['David', 'John', 'Marta', 'Sara', 'James']
print(names)
​
print(len(names))
first_person = names[0]
print(first_person)
last_index = len(names) - 1
last_person = names[last_index]
print(last_person)
names[0] = 'Katja'
print(names)
names[last_index] = 'Alex'
print(names)
​
short_names = []
for name in names:
    if len(name) == 4:
        short_names.append(name)
        print(name)
print(short_names)
​
nums = [1, 2, 3]
another_nums = [6, 7, 8]
nums.append(4)
nums.append(5)
print(nums)
nums.extend(another_nums)
nums.pop()
print(nums)
nums.remove(1)
print(nums)
​
# Dictionary
countries_demo = {
    'country_name': 'Finland',
    'population': 16
}
​
country_name = countries_demo['country_name']
country_pop = countries_demo['population']
country_city = countries_demo.get('city')
​
print(country_name)
print(country_pop)
print(country_city)
# if country_city == None:
#     countries_demo['country_city'] = 'some where in where'
​
# print(countries_demo)
​
if country_city not in countries_demo:
    countries_demo['country_city'] = 'Hel'
​
print(countries_demo)
​
# Function: Function is a reusable block codes
​
# declaring a function


def do_something():
    print('I am doing something')


do_something()  # calling a function
​


def square(x=2):
    return x * x


print(square())
print(square(10))
print(square())
​


def addTwoNums(x=2, y=3):
    total = x + y
    return total


print(addTwoNums())
print(addTwoNums(99, 1))
​


def area_of_circle(r):
    area = math.pi * r ** 2
    result = 'The area of radius, {} is {}'.format(r, round(area, 2))
    return result


print(area_of_circle(10))
​
​


def sum_of_nums(n):
    total = 0
    for i in range(n+1):
        total += i
    return total


def sum_of_even_nums(n):
    total = 0
    for i in range(0, n + 1, 2):
        total += i
    return total


print(sum_of_even_nums(100))
​


def sum_of_odds_and_evens(n):
    sum_of_odds = 0
    sum_of_evens = 0
    for i in range(n+1):
        if(i % 2 == 0):
            sum_of_evens += i
        else:
            sum_of_odds += i
    return sum_of_evens, sum_of_odds


print(sum_of_odds_and_evens(100))
