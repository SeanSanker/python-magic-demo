# Mutable Default Arguments in Python

## The Problem

In Python, mutable objects (lists, dictionaries, sets) used as default arguments persist between function calls. This happens because the default argument is evaluated only once when the function is defined, not each time the function is called.

## Examples of the Problem

```python
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
print(add_to_set("a"))  # {'a'}
print(add_to_set("b"))  # {'a', 'b'} - persists!
print(add_to_set("c"))  # {'a', 'b', 'c'} - still persists!

# Test lists
print(add_to_list("x"))  # ['x']
print(add_to_list("y"))  # ['x', 'y'] - persists!

# Test dicts
print(add_to_dict("key1", "val1"))  # {'key1': 'val1'}
print(add_to_dict("key2", "val2"))  # {'key1': 'val1', 'key2': 'val2'} - persists!
```

## The Solution: Use None as Default

The safe pattern is to use `None` as the default and create a new mutable object inside the function:

```python
def add_to_set(item, my_set=None):
    if my_set is None:
        my_set = set()
    my_set.add(item)
    return my_set
```

## Type Safety with Type Hints

To maintain type safety, use `Optional[T]` or union syntax `T | None`:

```python
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
```

## Key Points for Type Safety

1. **Parameter type**: `set[T] | None` or `Optional[set[T]]`
2. **Return type**: `set[T]` (since you always return a set)
3. **Runtime check**: `if my_set is None:` to create the new container

This pattern works for all mutable containers:
- `list[T] | None`
- `dict[K, V] | None`
- `set[T] | None`

Type checkers like mypy will understand that after the `None` check, the variable is guaranteed to be the non-None type.

## Summary

- **All mutable objects** (lists, dicts, sets) persist as default arguments
- **Use `None` as default** and create the object inside the function
- **Use union types** (`T | None`) for proper type hints
- **Always check for `None`** before using the parameter