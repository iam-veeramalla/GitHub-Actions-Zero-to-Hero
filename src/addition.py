# app.py
# This is a test commit
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0

def multiply(a,b):
    return a*b

def test_multiplication(a,b):
    assert multiply(1,2) == 2
    assert multiply(10,20) == 200
