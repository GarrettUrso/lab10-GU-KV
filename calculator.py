# https://github.com/GarrettUrso/lab10-GU-KV
# Partner 1: Garrett Urso
# Partner 2: Kirk Andrew Vinas

import math

def square_root(a):
    if a < 0:
        raise ValueError("a must be positive.")
    try:
        return math.sqrt(a)
    except ValueError as e:
        print(f"Caught ValueError as: {e}")

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    if a = 0:
        raise ZeroDivisionError("a must not be 0.")
    try:
        return b / a
    except ZeroDivisionError as e:
        print("Caught ZeroDivisionError:", e)
def logarithm(a,b):
    if a <= 0:
        raise ValueError("a must be positive.")
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

