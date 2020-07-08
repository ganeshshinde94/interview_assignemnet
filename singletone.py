
# 3. Code of a singleton using metaclasses.

class Metaclass(type):
     """This is Singletone design pattern"""
     _instance = {}

     def __call__(cls, *args, **kwargs):

         """If instance already exists don't create"""

         if cls not in cls._instance:
             cls._instance[cls] = super(Metaclass, cls).__call__(*args,**kwargs)
             return cls._instance[cls]

class check_singletone(metaclass=Metaclass):

    def __init__(self):
        pass

    def methodA(self):
        print("Method A")

first_object = check_singletone()
print(first_object)
second_object = check_singletone()
print(second_object)