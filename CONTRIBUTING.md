# Contributing to FastAPI Template

Thank you for your interest in contributing to the FastAPI Template! This document provides guidelines and information about contributing to this project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Submitting Changes](#submitting-changes)
- [Coding Standards](#coding-standards)
- [Testing](#testing)
- [Documentation](#documentation)
- [Issue Reporting](#issue-reporting)
- [Feature Requests](#feature-requests)

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please be respectful, inclusive, and considerate in all interactions.

## Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:

   ```bash
   git clone https://github.com/YOUR_USERNAME/fastapi-template.git
   cd fastapi-template
   ```

3. Add the upstream repository as a remote:

   ```bash
   git remote add upstream https://github.com/kupras06/fastapi-template.git
   ```

## Development Setup

1. **Python Environment**: Ensure you have Python 3.8+ installed
2. **Virtual Environment**: Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Dependencies**: Install development dependencies:

   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Pre-commit Hooks**: Install pre-commit hooks (if available):

   ```bash
   pre-commit install
   ```

## Making Changes

### Branch Naming Convention

Create a new branch for your changes using one of these prefixes:

- `feature/` - for new features
- `fix/` - for bug fixes
- `docs/` - for documentation changes
- `refactor/` - for code refactoring
- `test/` - for adding or updating tests

Example: `feature/add-authentication` or `fix/database-connection-issue`

### Commit Message Guidelines

Write clear, concise commit messages following this format:

```git
type(scope): brief description

Detailed explanation if necessary

Closes #issue-number
```

Types:

- `feat`: new feature
- `fix`: bug fix
- `docs`: documentation changes
- `style`: formatting changes
- `refactor`: code refactoring
- `test`: adding or updating tests
- `chore`: maintenance tasks

Examples:

- `feat(auth): add JWT authentication middleware`
- `fix(database): resolve connection pool timeout issue`
- `docs(readme): update installation instructions`

## Submitting Changes

1. **Sync with upstream**: Before submitting, ensure your branch is up to date:

   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run tests**: Ensure all tests pass:

   ```bash
   pytest
   ```

3. **Check code quality**: Run linting and formatting:

   ```bash
   black .
   flake8
   mypy .
   ```

4. **Push your changes**:

   ```bash
   git push origin your-branch-name
   ```

5. **Create a Pull Request**:
   - Go to GitHub and create a pull request
   - Use a clear, descriptive title
   - Fill out the pull request template
   - Link any related issues

### Pull Request Guidelines

- **Single Purpose**: Each PR should address a single feature or bug fix
- **Size**: Keep PRs reasonably sized (< 500 lines when possible)
- **Description**: Provide a clear description of what changes were made and why
- **Testing**: Include tests for new functionality
- **Documentation**: Update documentation if needed

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://pep8.org/) style guidelines
- Use [Black](https://black.readthedocs.io/) for code formatting
- Use [isort](https://pycqa.github.io/isort/) for import sorting
- Maximum line length: 88 characters (Black default)

### FastAPI Specific Guidelines

- Use type hints for all function parameters and return values
- Follow FastAPI best practices for route organization
- Use Pydantic models for request/response validation
- Include proper error handling and HTTP status codes
- Document API endpoints with clear descriptions and examples

### Code Organization

- Keep related functionality in appropriate modules
- Use descriptive variable and function names
- Add docstrings for all public functions and classes
- Include type hints throughout the codebase

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_specific_module.py
```

### Writing Tests

- Write tests for all new functionality
- Use descriptive test names
- Follow the Arrange-Act-Assert pattern
- Mock external dependencies
- Aim for high test coverage (>80%)

### Test Structure

```python
def test_function_name_should_expected_behavior():
    # Arrange
    setup_data = create_test_data()
    
    # Act
    result = function_under_test(setup_data)
    
    # Assert
    assert result == expected_result
```

## Documentation

### API Documentation

- All endpoints should have clear docstrings
- Use FastAPI's automatic documentation features
- Include request/response examples
- Document error cases and status codes

### Code Documentation

- Add docstrings to all public functions and classes
- Use clear, concise comments for complex logic
- Keep README.md up to date
- Update CHANGELOG.md for significant changes

## Issue Reporting

### Bug Reports

When reporting bugs, please include:

- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Environment details (Python version, OS, etc.)
- Error messages or stack traces
- Minimal code example if applicable

### Use the Bug Report Template

```markdown
**Describe the bug**
A clear description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior.

**Expected behavior**
What you expected to happen.

**Environment**
- OS: [e.g., Ubuntu 20.04]
- Python version: [e.g., 3.9.0]
- FastAPI version: [e.g., 0.68.0]

**Additional context**
Any other context about the problem.
```

## Feature Requests

### Before Submitting

- Check if the feature already exists
- Search existing issues and discussions
- Consider if the feature fits the project's scope
- Think about backward compatibility

### Feature Request Template

```markdown
**Is your feature request related to a problem?**
A clear description of what the problem is.

**Describe the solution you'd like**
A clear description of what you want to happen.

**Describe alternatives you've considered**
Alternative solutions or features you've considered.

**Additional context**
Any other context or screenshots about the feature request.
```

## Project Maintainers

For questions or additional guidance, feel free to reach out to the project maintainers:

- [@kupras06](https://github.com/kupras06)

## Recognition

Contributors will be recognized in the project's README.md and release notes. We appreciate all contributions, whether they're code, documentation, bug reports, or feature suggestions!

## Getting Help

- Check the [documentation](README.md)
- Search existing [issues](https://github.com/kupras06/fastapi-template/issues)
- Join our [discussions](https://github.com/kupras06/fastapi-template/discussions)
- Ask questions in issues with the "question" label

Thank you for contributing to the FastAPI Template! 🚀
