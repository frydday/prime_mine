"""
Core functionality for MyProject.
"""

from typing import Any, Dict, List, Optional


class MyClass:
    """
    A class that demonstrates the structure of the project.
    
    Attributes:
        name: The name of the instance.
        config: Configuration dictionary.
    """
    
    def __init__(self, name: str = "default", config: Optional[Dict[str, Any]] = None):
        """
        Initialize MyClass.
        
        Args:
            name: The name for this instance.
            config: Optional configuration dictionary.
        """
        self.name = name
        self.config = config or {}
    
    def do_something(self, data: List[int]) -> int:
        """
        Process data and return a result.
        
        Args:
            data: A list of integers to process.
            
        Returns:
            The sum of the input data.
            
        Example:
            >>> obj = MyClass()
            >>> obj.do_something([1, 2, 3])
            6
        """
        return sum(data)
    
    def __repr__(self) -> str:
        return f"MyClass(name='{self.name}')"
