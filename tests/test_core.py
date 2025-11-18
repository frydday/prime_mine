"""
Tests for the core module.
"""

import pytest
from myproject.core import MyClass
#from prime_mine.src.myproject.core import MyClass

class TestMyClass:
    """Test suite for MyClass."""
    
    def test_initialization_default(self):
        """Test default initialization."""
        obj = MyClass()
        assert obj.name == "default"
        assert obj.config == {}
    
    def test_initialization_with_params(self):
        """Test initialization with parameters."""
        config = {"key": "value"}
        obj = MyClass(name="test", config=config)
        assert obj.name == "test"
        assert obj.config == config
    
    def test_do_something(self):
        """Test the do_something method."""
        obj = MyClass()
        result = obj.do_something([1, 2, 3, 4])
        assert result == 10
    
    def test_do_something_empty_list(self):
        """Test do_something with empty list."""
        obj = MyClass()
        result = obj.do_something([])
        assert result == 0
    
    def test_repr(self):
        """Test string representation."""
        obj = MyClass(name="test")
        assert repr(obj) == "MyClass(name='test')"


if __name__ == "__main__":
    pytest.main([__file__])
