'''
This is a simple program to understand the basics of github actions
'''
def add(a, b):
    return a + b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

def test_add():
    assert add(1, 2) == 3
    assert sub(1, -1) == 2
    assert mult(5,5) == 25
    assert div(-1,-1) == 1
