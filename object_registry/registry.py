component_registry = {}

def registry_add_component(obj: object, name: str):
    # First check - object by same name exists?
    if name in component_registry.keys():
        print("ERROR: cannot add component - component already registered with same name!")
        return
    # Second check - same object already registered?
    for val in component_registry.values():
        if val is obj: 
            print("ERROR: cannot add component - same component object already in registry!")
            return
    # Checks OK - register object:
    component_registry[name] = obj
    print("Component successfully registered!:-)")


def registry_get_component(name: str):
    if name in component_registry.keys():
        return component_registry[name]
    else:
        print(f"No component named '{name}' in registry!")
        return None


# ******************* TEST ***********************
if __name__ == "__main__":
    from class_a import ClassA
    from class_b import ClassB
    from pprint import pprint

    a = ClassA('A1')
    b = ClassB('B1')
    registry_add_component(a, 'a')
    registry_add_component(b, 'a')   # First failing test ...
    registry_add_component(b, 'b')
    registry_add_component(a, 'c')   # Second failing test ...
    pprint(component_registry)
    aref = registry_get_component('a')
    aref.print_me('hellu')
    bref = registry_get_component('b')
    bref.print_me('halla')
    cref = registry_get_component('c')   # Fail ...


