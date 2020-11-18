"""
@file class_a.py
"""

import inspect
from pprint import pprint


class ClassA:
    def __init__(self):
        frame = inspect.currentframe()
        self.calling_namespace = frame.f_back.f_locals
        
    def show_globals(self):
        print("Calling namespace (encapsulating A):")
        pprint(self.calling_namespace)

    def print_b(self):
        cls_b = self.calling_namespace['b']
        cls_b.print_me("Hello from class A!")

    def print_me(self, msg: str):
        print(msg)



