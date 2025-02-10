# Custom Decorator

def log_execution(func):
    print("FIRST")
    def wrapper(*args, **kwargs):
        print("THIRD")
        result = func(*args, **kwargs)
        print("FOURTH")
        return result
    print("SECOND")
    return wrapper # only goes into wrapper when we call it 

@log_execution
def add(a, b):
    return a + b

print(add(3, 2))