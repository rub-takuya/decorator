from functools import wraps

def to_john(f):
    @wraps(f)
    def wrapper():
        return f() + ' John!'
    return wrapper

@to_john
def say_hello():
    return 'Hello!'

print(say_hello())