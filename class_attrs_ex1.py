import json


class Testo:
    def __init__(self, a_field, b_field, c_field):
        self._a_field = a_field
        self._b_field = b_field
        self._c_field = c_field

    def get_val(self, attr_name: str):
        attr = None
        if hasattr(self, attr_name):
            attr = getattr(self, attr_name)
        else:
            print(f"No attribute by name {attr_name}!")
        return attr
    

if __name__ == "__main__":
    tst1 = Testo(1357, "aqua", 3.748)
    print(f"{tst1.get_val('_a_field')}")
    print(f"{tst1.get_val('_b_field')}")
    print(f"{tst1.get_val('_c_field')}")
    print(f"{tst1.get_val('_d_field')}")

