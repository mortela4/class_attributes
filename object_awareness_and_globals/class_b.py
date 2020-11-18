"""
@file class_b.py
"""

import inspect
from pprint import pprint


class ClassB:
    def __init__(self):
        frame = inspect.currentframe()
        self.calling_namespace = frame.f_back.f_locals
        
    def show_globals(self):
        print("Calling namespace (encapsulating B):")
        pprint(self.calling_namespace)
        
    def print_a(self):
        cls_b = self.calling_namespace['a']
        cls_b.print_me("Hello from class B!")

    def print_me(self, msg: str):
        print(msg)


