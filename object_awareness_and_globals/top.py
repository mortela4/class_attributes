from class_a import ClassA
from class_b import ClassB


if __name__ == "__main__":
    a = ClassA()
    b = ClassB()
    # Show globals:
    a.show_globals()
    b.show_globals()
    # Call each other's 'print_me()' method:
    a.print_b()
    b.print_a()

