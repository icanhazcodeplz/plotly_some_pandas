"""
Go through https://www.w3schools.com/python/python_classes.asp, writing down code here and using
PyCharm to run the debugger and inspect the class as you build it
"""

"""
Problem 1:
In the w3 tutorial, you built a class called Person. Make a new class called Robot that does the 
same thing as Person, but includes an attribute called "processing_unit" that is printed after
"Hello my name is <name>". 

So, if the Robot has "name=zuckerberg" and "processing_unit=hpu_v3", when `myfunc` is called, the 
printed output should be:

Hello my name is zuckerberg
My processing unit is hpu_v3
"""
t = df1.groupby('SOURCE_KEY')['DAILY_YIELD'].resample("D").max()
t.groupby('SOURCE_KEY').mean()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def mymethod(self):
        print("Hello my name is " + self.name)

MULTIPLIER = 2

def add_with_multiplier(a, b):
    return (a +b) * MULTIPLIER




class Multiplier2:
    multiplier = 2

    def add(self, a, b):
        return add_with_multiplier()

    def sub_with_multiplier(self, a, b):
        return (a-b) * self.multiplier


class Multiplier3:
    multiplier = 3

    def add(self, a, b):
        return add_with_multiplier()

    def sub_with_multiplier(self, a, b):
        return (a-b) * self.multiplier



m2 = Multiplier2()
m3 = Multiplier3()
