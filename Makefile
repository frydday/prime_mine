.PHONY: help install install-dev test lint format type-check clean build docs

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install package in production mode
	pip install .

install-dev:  ## Install package in development mode with dev dependencies
	pip install -e ".[dev]"

test:  ## Run tests with pytest
	pytest tests/ -v --cov=myproject --cov-report=term-missing

test-fast:  ## Run tests without coverage
	pytest tests/ -v

lint:  ## Run flake8 linter
	flake8 src tests

format:  ## Format code with black
	black src tests

format-check:  ## Check code formatting without modifying
	black --check src tests

type-check:  ## Run mypy type checker
	mypy src

isort:  ## Sort imports with isort
	isort src tests

isort-check:  ## Check import sorting without modifying
	isort --check-only src tests

clean:  ## Remove build artifacts and cache files
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

build:  ## Build distribution packages
	python -m build

check: format-check lint type-check test  ## Run all checks (format, lint, type, test)

docs:  ## Build documentation
	@echo "Building documentation..."
	@echo "Add your documentation build command here (e.g., sphinx-build)"
