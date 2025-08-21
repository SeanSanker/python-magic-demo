def add_to_set(item, my_set=set()):
    my_set.add(item)
    return my_set

def add_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list

def add_to_dict(key, value, my_dict={}):
    my_dict[key] = value
    return my_dict

# Test sets
print("Testing sets:")
print(add_to_set("a"))  # {'a'}
print(add_to_set("b"))  # {'a', 'b'} - persists!
print(add_to_set("c"))  # {'a', 'b', 'c'} - still persists!

print("\nTesting lists:")
print(add_to_list("x"))  # ['x']
print(add_to_list("y"))  # ['x', 'y'] - persists!

print("\nTesting dicts:")
print(add_to_dict("key1", "val1"))  # {'key1': 'val1'}
print(add_to_dict("key2", "val2"))  # {'key1': 'val1', 'key2': 'val2'} - persists!