from functools import wraps

def announce(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting", func.__name__)
        result = func(*args, **kwargs)
        print("Finished", func.__name__)
        return result
    return wrapper

@announce
def greet(name):
    return f"Hello, {name}!"

print(greet("Rahim"))
