"""CI test module"""

def hello():
    """Return a greeting message"""
    return "Hello, CI World!"

def add(a, b):
    """Return the sum of the 2 numbers"""
    return a + b

if __name__ == "__main__":
    print(hello())
    print(f"1 + 2 = {add(1, 2)}")