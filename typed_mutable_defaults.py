from typing import Optional

# Option 1: Using Optional (older syntax)
def add_to_set_optional(item: str, my_set: Optional[set[str]] = None) -> set[str]:
    if my_set is None:
        my_set = set()
    my_set.add(item)
    return my_set

# Option 2: Using union syntax (Python 3.10+)
def add_to_set_union(item: str, my_set: set[str] | None = None) -> set[str]:
    if my_set is None:
        my_set = set()
    my_set.add(item)
    return my_set

# For lists
def add_to_list_typed(item: str, my_list: list[str] | None = None) -> list[str]:
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

# For dicts
def add_to_dict_typed(key: str, value: int, my_dict: dict[str, int] | None = None) -> dict[str, int]:
    if my_dict is None:
        my_dict = {}
    my_dict[key] = value
    return my_dict

# Test the typed versions
print("Typed set function:")
result1 = add_to_set_union("a")
print(result1)  # {'a'}
result2 = add_to_set_union("b")
print(result2)  # {'b'} - fresh set each time!

print("\nPassing existing set:")
existing_set = {"x", "y"}
result3 = add_to_set_union("z", existing_set)
print(result3)  # {'x', 'y', 'z'}