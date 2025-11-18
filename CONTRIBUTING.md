# Contributing to MyProject

Thank you for your interest in contributing to MyProject! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in [Issues](https://github.com/yourusername/myproject/issues)
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - Python version and OS information

### Suggesting Enhancements

1. Check existing issues and pull requests first
2. Create a new issue describing:
   - The enhancement and its benefits
   - Possible implementation approach
   - Any breaking changes

### Pull Requests

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes
4. Add or update tests as needed
5. Ensure all tests pass: `pytest`
6. Format your code: `black src tests`
7. Check linting: `flake8 src tests`
8. Type check: `mypy src`
9. Commit your changes with a clear message
10. Push to your fork and submit a pull request

## Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/myproject.git
cd myproject

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"
```

## Coding Standards

- Follow PEP 8 style guide
- Use type hints for function parameters and returns
- Write docstrings for all public functions and classes
- Keep functions focused and maintainable
- Add tests for new functionality

## Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=myproject

# Run specific test file
pytest tests/test_core.py
```

## Questions?

Feel free to open an issue for any questions or concerns!
