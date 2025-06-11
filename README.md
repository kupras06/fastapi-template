# 🚀 FastAPI Copier Template

A modern, production-ready FastAPI project template using [Copier](https://copier.readthedocs.io/) for scaffolding and [UV](https://docs.astral.sh/uv/) for dependency management.

## ✨ Features

- **⚡ FastAPI**: Modern, fast web framework with automatic API documentation
- **🐍 Modern Python**: Support for Python 3.10, 3.11, and 3.12
- **📦 UV Package Manager**: Lightning-fast dependency resolution and management
- **🔧 Flexible Configuration**: Choose only the features you need
- **🔄 Template Updates**: Update existing projects when template evolves
- **🐳 Docker Ready**: Optional Docker and Docker Compose configuration
- **🗄️ Database Support**: SQLite, PostgreSQL, or MySQL with async support
- **🔐 Authentication**: Optional JWT-based authentication system
- **⚡ Redis & Celery**: Optional caching and background task processing
- **🧪 Testing**: Comprehensive test suite with pytest
- **📝 Code Quality**: Pre-configured Black, isort, Ruff, and MyPy
- **🔄 Database Migrations**: Optional Alembic integration
- **📚 Auto Documentation**: Swagger UI and ReDoc included

## 🎯 Quick Start

### Prerequisites

- Python 3.10+
- [UV](https://docs.astral.sh/uv/getting-started/installation/) package manager
- [Copier](https://copier.readthedocs.io/en/stable/installing/) template engine

### Installation

```bash
# Install copier if you haven't already
pip install copier

# Or with UV
uv tool install copier
```

### Generate a New Project

```bash
# From GitHub (recommended)
copier copy https://github.com/yourusername/fastapi-copier-template my-awesome-api

# From local template
copier copy /path/to/fastapi-copier-template my-awesome-api
```

### Project Setup

```bash
cd my-awesome-api

# Install dependencies
uv sync

# Copy environment template
cp .env.example .env

# Edit .env with your settings
vim .env

# Run database migrations (if database is enabled)
uv run alembic upgrade head

# Start the development server
uv run fastapi dev
```

Your API will be available at:

- **API**: <http://localhost:8000>
- **Interactive Docs**: <http://localhost:8000/docs>
- **Alternative Docs**: <http://localhost:8000/redoc>

## 🎛️ Configuration Options ( Work in Progress )

The template will prompt you for the following options:

| Option | Description | Default |
|--------|-------------|---------|
| `project_name` | Human-readable project name | "My FastAPI Project" |
| `project_slug` | Python package name (auto-generated) | - |
| `description` | Brief project description | - |
| `author_name` | Your full name | "Your Name" |
| `author_email` | Your email address | "<your.email@example.com>" |
| `python_version` | Python version (3.10, 3.11, 3.12) | "3.12" |
| `include_database` | Database type (none, sqlite, postgresql, mysql) | "none" |
| `include_auth` | JWT authentication | `false` |
| `include_async_database` | Async database operations | `auto` |
| `include_alembic` | Database migrations | `auto` |
| `include_tests` | Test suite with pytest | `true` |
| `include_docker` | Docker configuration | `true` |
| `include_redis` | Redis for caching/sessions | `false` |
| `include_celery` | Background tasks with Celery | `false` |
| `api_prefix` | API route prefix | "/api/v1" |
| `cors_origins` | CORS allowed origins | "<http://localhost:3000,http://localhost:8080>" |

## 📁 Generated Project Structure

```md
my-awesome-api/
├── 📄 pyproject.toml          # Project configuration & dependencies
├── 📄 README.md               # Project-specific documentation
├── 📄 .env.example            # Environment variables template
├── 📄 .gitignore              # Git ignore rules
├── 🐳 Dockerfile              # Docker configuration (optional)
├── 🐳 docker-compose.yml      # Docker Compose (optional)
├── 📁 app/
│   ├── 📄 __init__.py
│   ├── 📄 main.py             # FastAPI application entry point
│   ├── 📁 api/
│   │   ├── 📄 __init__.py
│   │   └── 📄 routes.py       # API route definitions
│   ├── 📁 core/
│   │   ├── 📄 __init__.py
│   │   ├── 📄 config.py       # App configuration
│   │   ├── 📄 database.py     # Database setup (optional)
│   │   └── 📄 security.py     # Authentication (optional)
│   ├── 📁 models/             # SQLAlchemy models (optional)
│   ├── 📁 schemas/            # Pydantic schemas
│   └── 📁 crud/               # Database operations (optional)
└── 📁 tests/                  # Test suite (optional)
    ├── 📄 __init__.py
    ├── 📄 conftest.py
    └── 📄 test_main.py
```

## 🔄 Updating Existing Projects

One of Copier's best features is the ability to update existing projects when the template evolves:

```bash
# Update project with latest template changes
cd my-existing-project
copier update

# Reconfigure project with different options
copier reconfigure
```

## 🐳 Docker Usage

If you enabled Docker support:

```bash
# Development with Docker Compose
docker-compose up --build

# Production build
docker build -t my-awesome-api .
docker run -p 8000:8000 my-awesome-api
```

## 🧪 Development Workflow

### Code Quality

```bash
# Format code
uv run black .
uv run isort .

# Lint code
uv run ruff check .
uv run mypy .

# Fix linting issues
uv run ruff check --fix .
```

### Testing

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=app --cov-report=html

# Run specific test file
uv run pytest tests/test_main.py -v
```

### Database Operations

```bash
# Create new migration
uv run alembic revision --autogenerate -m "Add new table"

# Apply migrations
uv run alembic upgrade head

# Rollback migration
uv run alembic downgrade -1
```

## 🎨 Customization

### Adding New Features

1. Fork this template repository
2. Modify the template files in `{{ project_slug }}/`
3. Update `copier.yml` with new configuration options
4. Test your changes with `copier copy . /tmp/test-project`
5. Submit a pull request

### Template Development

```bash
# Test template locally
copier copy . /tmp/test-project --data project_name="Test Project"

# Answer prompts programmatically
copier copy . /tmp/test-project --data-file test-data.yml
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **🐛 Report Issues**: Found a bug? Open an issue with details
2. **💡 Feature Requests**: Have an idea? Let's discuss it
3. **🔧 Pull Requests**:
   - Fork the repository
   - Create a feature branch (`git checkout -b feature/amazing-feature`)
   - Make your changes
   - Test thoroughly
   - Submit a pull request

### Development Setup

```bash
# Clone the template repository
git clone https://github.com/yourusername/fastapi-copier-template
cd fastapi-copier-template

# Test the template
copier copy . /tmp/test-project --data project_name="Test Project"
cd /tmp/test-project
uv sync
uv run uvicorn app.main:app --reload
```

## 📋 Roadmap

- [ ] Support for more databases (MongoDB, etc.)
- [ ] WebSocket support
- [ ] GraphQL integration
- [ ] Kubernetes deployment templates
- [ ] CI/CD pipeline templates
- [ ] More authentication providers (OAuth, SAML)
- [ ] API versioning strategies
- [ ] Monitoring and observability setup

## 🙏 Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - The amazing web framework
- [Copier](https://copier.readthedocs.io/) - Template engine that makes this possible
- [UV](https://docs.astral.sh/uv/) - Fast Python package management
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation using Python type hints

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Show Your Support

If this template helped you build something awesome, please give it a ⭐ on GitHub!

---

**Happy coding! 🚀**

*Built with ❤️ for the Python community*
