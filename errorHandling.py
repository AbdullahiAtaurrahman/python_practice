try: 
    print(1/0)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Close calculator")

def add(a, b):
    assert b!=0, "zero error again"
    return a / b