import SomeClass


def greet_me(**kwargs):
    """
    kwargs example
    """
    if "key" in kwargs:
        print("key = ", kwargs["key"])
    else:
        print("Missing key")


def get_info(*args):
    return "Test data"

greet_me(name="suzy")

SomeClass.get_info = get_info
print(SomeClass.get_info("Hello"))
