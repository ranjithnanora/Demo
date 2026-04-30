print(dir(Exception))

class MyFirstException(Exception):
    def __init__(self,message):
        super().__init__(message)


try:
    e=MyFirstException("first exception")
    e.add_note("this is extra note")
    raise e
except MyFirstException as a:
    print(a)
    if hasattr(a, "__notes__"):
        for note in a.__notes__:
            print(f"note: {note}")