import json


class Testo:
    fields = ['a', 'b', 'c', 'd']
    fieldname_to_attrname = {
                        'a': '_a_field', 
                        'b': '_b_field', 
                        'c': '_c_field', 
                    }

    def __init__(self, a_field, b_field, c_field):
        self._a_field = a_field
        self._b_field = b_field
        self._c_field = c_field

    def build_dict(self) -> dict:
        attr_dict = dict()
        # Build dict from fields:
        for field_name in self.fields:
            try:
                attr_name = self.fieldname_to_attrname[field_name]
                if hasattr(self, attr_name):
                    attr_dict[field_name] = getattr(self, attr_name)
                else:
                    print(f"No attribute by name {attr_name}!")
                    attr_dict[field_name] = None
            except KeyError:
                print(f"No corresponding attribute to field named '{field_name}' ...")
                attr_dict[field_name] = None
                # NOTE: may raise 'NotImplemented'-exception here??
        # 
        return attr_dict

    def build_json(self, field_names: list) -> str:
        data_map = self.build_dict()
        return json.dumps(data_map)


if __name__ == "__main__":
    tst1 = Testo(1357, "aqua", 3.748)
    dikt = tst1.build_dict()
    print(f"{dikt}")
    print("")
    json_data = tst1.build_dict()
    print(f"{json_data}")
