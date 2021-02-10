target = -5
num = 3

target =- num  # Noncompliant; target = -3. Is that really what's meant?
target =+ num # Noncompliant; target = 3


def foo(strings, param):
    param = 1  # NonCompliant


def myfunc1(foo="Noncompliant"):
    pass

class MyClass:
    def mymethod1(self, foo="Noncompliant"):
        pass

toto = -2
