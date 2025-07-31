import math

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a,b):
    a * b
def div(a,b):
    try:
        return b / a
    except ZeroDivisionError as e:
        raise
        print("Caught ZeroDivisionError:", e)
def log(a,b):
    try:
        math.log(a,b)
    except ValueError as e:
        print("Caught ValueError:", e)
def exp(a,b):
    return a ** b