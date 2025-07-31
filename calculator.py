import math

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    try:
        return b / a
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)
def log(a,b):
    try:
        return math.log(b, a)
    except ValueError as e:
        print("Caught ValueError:", e)
def exp(a, b):
    return a ** b

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def log(a, b):
    try:
        return math.log(b, a)
    except ValueError as e:
        print("Caught ValueError as:", e)

