"""
Test file to verify the mutable default arguments examples work correctly.
"""

import pytest
from typed_mutable_defaults import add_to_set_union, add_to_list_typed, add_to_dict_typed


# Define problematic functions for testing (isolated from demo)
def problematic_set(item, my_set=set()):
    my_set.add(item)
    return my_set

def problematic_list(item, my_list=[]):
    my_list.append(item)
    return my_list

def problematic_dict(key, value, my_dict={}):
    my_dict[key] = value
    return my_dict


def test_mutable_defaults_persist():
    """Test that mutable defaults persist between calls (demonstrating the problem)."""
    result1 = problematic_set("a")
    result2 = problematic_set("b")
    
    # The second call should contain both items due to persistence
    assert "a" in result2
    assert "b" in result2
    assert len(result2) == 2


def test_safe_defaults_dont_persist():
    """Test that the safe None-based defaults create fresh objects."""
    result1 = add_to_set_union("a")
    result2 = add_to_set_union("b")
    
    # Each call should only contain its own item
    assert result1 == {"a"}
    assert result2 == {"b"}


def test_safe_defaults_with_provided_object():
    """Test that providing an object to safe functions works correctly."""
    existing_set = {"x", "y"}
    result = add_to_set_union("z", existing_set)
    
    assert "x" in result
    assert "y" in result
    assert "z" in result
    assert len(result) == 3


def test_list_safe_defaults():
    """Test safe list defaults."""
    result1 = add_to_list_typed("a")
    result2 = add_to_list_typed("b")
    
    assert result1 == ["a"]
    assert result2 == ["b"]


def test_dict_safe_defaults():
    """Test safe dict defaults."""
    result1 = add_to_dict_typed("key1", 1)
    result2 = add_to_dict_typed("key2", 2)
    
    assert result1 == {"key1": 1}
    assert result2 == {"key2": 2}


if __name__ == "__main__":
    pytest.main([__file__, "-v"])