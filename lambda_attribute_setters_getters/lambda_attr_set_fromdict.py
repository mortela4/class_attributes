"""
lambda_attr_set_fromdict.py
"""

class Testo:

    def __init__(self, a_val: int, b_val: int, c_val: int):
        self._a_val = a_val
        self._b_val = b_val
        self._c_val = c_val
        self.attr_map = {'a': '_a_val', 'b': '_b_val', 'c': '_c_val'}

    def print_props_properly(self):
        for key in self.attr_map.keys():
            print(f"'{key}' = { getattr(self, self.attr_map[key])}")

    def set_props_fromdict(self, prop_set: dict):
        attr_setter = {
            'a': (lambda val:  setattr(self, '_a_val', val)), 
            'b': (lambda val:  setattr(self, '_b_val', val)), 
            'c': (lambda val:  setattr(self, '_c_val', val))
            }
        for name, val in prop_set.items():
            print(f"Setting '{name}' to value={val} ...")
            attr_setter[name](val)


# ******************** TEST ***********************
if __name__ == "__main__":
    tst = Testo(3, 5, 7)
    tst.print_props_properly()
    config1 = {'a': 123, 'b': 357, 'c': 5790}
    tst.set_props_fromdict(prop_set=config1)
    tst.print_props_properly()
    print(f"'a' = {tst._a_val}")    
    # Test using shorter dict:
    config2 = {'a': -666, 'b': -3}
    tst.set_props_fromdict(prop_set=config2)
    print(f"'a' = {tst._a_val}")
    tst.print_props_properly()

