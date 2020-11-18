import json


fieldname_to_attrname = {
                        'a': '_a_field', 
                        'b': '_b_field', 
                        'c': '_c_field', 
                    }


class Testo:
    def __init__(self, a_field, b_field, c_field):
        self._a_field = a_field
        self._b_field = b_field
        self._c_field = c_field

    def build_dict(self, field_names: list) -> dict:
        # Helper func:
        def get_attr_val(attr_name: str):
            attr = None
            if hasattr(self, attr_name):
                attr = getattr(self, attr_name)
            else:
                print(f"No attribute by name {attr_name}!")
            return attr

        attr_dict = dict()
        # Build dict from fields:
        for field_name in field_names:
            try:
                attr_name = fieldname_to_attrname[field_name]
                attr_dict[field_name] = get_attr_val(attr_name)
            except KeyError:
                attr_dict[field_name] = None
                # NOTE: may raise 'NotImplemented'-exception here??
        # 
        return attr_dict

    def build_json(self, field_names: list) -> str:
        data_map = self.build_dict(field_names=field_names)
        return json.dumps(data_map)


if __name__ == "__main__":
    fields = ['a', 'b', 'c', 'd']

    tst1 = Testo(1357, "aqua", 3.748)
    dikt = tst1.build_dict(fields)
    print(f"{dikt}")
    print("")
    json_data = tst1.build_dict(fields)
    print(f"{json_data}")
