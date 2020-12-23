"""
lambda_attr_set.py
"""

class Testo:

    def __init__(self, a_val: int, b_val: int, c_val: int):
        self._a_val = a_val
        self._b_val = b_val
        self._c_val = c_val
        self.attr_map = {'a': self._a_val, 'b': self._b_val, 'c': self._c_val}

        self.attr_setter = {
            'a': (lambda val:  setattr(self, '_a_val', val)), 
            'b': (lambda val:  setattr(self, '_b_val', val)), 
            'c': (lambda val:  setattr(self, '_c_val', val))
            }

    def set_props(self, name: str, value: int):
        # Set value from name:
        try:
            self.attr_map[name] = value
        except KeyError:
            print(f"No property mapping to name = '{name}'!!")
        
    def print_props(self):
        for key in self.attr_map.keys():
            print(f"'{key}' = {self.attr_map[key]}")   # NOTE: prints INITIAL value of properties!

    def set_props_properly(self, name: str, val: int):
        self.attr_setter[name](val)


# ******************** TEST ***********************
if __name__ == "__main__":
    tst = Testo(3, 5, 7)
    tst.print_props()
    tst.set_props('a', 123)
    tst.print_props()
    tst.set_props('b', 357)
    tst.set_props('c', 579)
    tst.print_props()
    tst.set_props('a', -666)
    print(f"'a' = {tst._a_val}")    # Prints value '3' - so the internal props have NOT been modified!
    # Test using lambda:
    tst.set_props_properly('a', -666)
    print(f"'a' = {tst._a_val}")




