# Generic Web UI Test Automation 🎭

[![CI](https://github.com/juliansernave/generic-web-ui-ta/workflows/CI/badge.svg)](https://github.com/juliansernave/generic-web-ui-ta/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

A modern, production-ready test automation framework for web UI testing using Python, Playwright, Pytest, and Allure. This project demonstrates professional testing practices with clean architecture, comprehensive reporting, and CI/CD integration.

## 🎯 Project Overview

This framework targets the [Sauce Demo](https://www.saucedemo.com/) eCommerce application, providing a scalable foundation for UI test automation with:

- **Page Object Model (POM)** architecture for maintainability
- **Allure reporting** for detailed test execution insights
- **Parallel test execution** for faster feedback
- **CI/CD ready** with GitHub Actions integration
- **Modern Python tooling** (Poetry, Ruff, Black, pre-commit)

## ✨ Key Features

- **🎭 Playwright Integration**: Fast, reliable cross-browser testing (Chromium, Firefox, WebKit)
- **📊 Allure Reports**: Rich test reporting with screenshots, videos, and detailed logs
- **⚡ Parallel Execution**: Run tests concurrently using pytest-xdist
- **🎨 Code Quality**: Automated linting (Ruff) and formatting (Black) with pre-commit hooks
- **🔧 Flexible Configuration**: Environment-based settings via .env files
- **📦 Dependency Management**: Poetry for reproducible builds and dependency resolution
- **🏗️ Clean Architecture**: Separation of concerns with pages, services, and core utilities

## 📋 Prerequisites

Before running this project, ensure you have the following installed:

- **Python 3.11+** ([Download](https://www.python.org/downloads/))
- **Poetry** (Python dependency management tool)
- **Git**

### Installing Poetry

If you don't have Poetry installed, use one of these methods:

**macOS/Linux/WSL:**
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

**Windows (PowerShell):**
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

For more installation options, visit the [official Poetry documentation](https://python-poetry.org/docs/#installation).

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/juliansernave/generic-web-ui-ta.git
cd generic-web-ui-ta
```

### 2. Install Dependencies
```bash
# Install project dependencies
poetry install

# Install Playwright browsers
poetry run playwright install --with-deps
```

Alternatively, use the Makefile:
```bash
make install
```

### 3. Configure Environment Variables
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your preferred settings (optional)
```

### 4. Run Tests
```bash
# Run all tests
poetry run pytest

# Or use the Makefile
make test
```

## 📁 Project Structure

```
generic-web-ui-ta/
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD pipeline
├── src/
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py         # Application settings and environment configuration
│   ├── core/
│   │   ├── builder.py          # Builder patterns for test data
│   │   ├── logging.py          # Centralized logging utilities
│   │   └── wait_strategies.py  # Custom wait strategies for Playwright
│   ├── pages/
│   │   ├── base_page.py        # Base page class with common methods
│   │   ├── login_page.py       # Login page objects
│   │   ├── inventory_page.py   # Product inventory page objects
│   │   ├── cart_page.py        # Shopping cart page objects
│   │   └── checkout_info_page.py # Checkout flow page objects
│   └── services/
│       └── user_flows.py       # Reusable user journey flows
├── tests/
│   ├── __init__.py
│   ├── conftest.py             # Pytest fixtures and configuration
│   ├── test_login.py           # Login functionality tests
│   └── test_checkout_smoke.py  # Checkout smoke tests
├── allure-results/             # Allure test results (generated)
├── .env.example                # Example environment variables
├── .gitignore                  # Git ignore patterns
├── .pre-commit-config.yaml     # Pre-commit hooks configuration
├── Makefile                    # Convenient command shortcuts
├── poetry.lock                 # Locked dependency versions
├── pyproject.toml              # Poetry configuration and dependencies
└── README.md                   # Project documentation
```

## 🧪 Running Tests

### Basic Test Execution

```bash
# Run all tests
poetry run pytest

# Run specific test file
poetry run pytest tests/test_login.py

# Run tests with specific marker
poetry run pytest -m smoke

# Run tests in headed mode (visible browser)
poetry run pytest --headed

# Run tests in a specific browser
poetry run pytest --browser chromium
poetry run pytest --browser firefox
poetry run pytest --browser webkit
```

### Parallel Execution

```bash
# Run tests in parallel (automatic worker count)
poetry run pytest -n auto

# Run tests with specific number of workers
poetry run pytest -n 4

# Run tests with load balancing by file
poetry run pytest -n auto --dist=loadfile
```

### Test Reporting

```bash
# Generate HTML report
poetry run pytest --html=report.html --self-contained-html

# Generate Allure report
poetry run pytest --alluredir=allure-results
allure serve allure-results

# Or use the Makefile
make report
```

### Using Makefile Commands

```bash
# Install dependencies
make install

# Run tests (parallel, fast-fail)
make test

# Generate HTML report
make report

# Run linting
make lint

# Format code
make fmt

# Setup pre-commit hooks
make hooks
```

> **Tip**: If you're inside the Poetry shell (`poetry shell`), you can omit the `poetry run` prefix and just use commands like `pytest` directly.

## ⚙️ Configuration

### Environment Variables

Configure the test execution via the `.env` file:

```bash
# Application Under Test
BASE_URL=https://www.saucedemo.com

# Test Users (Sauce Demo credentials)
STANDARD_USER=standard_user
LOCKED_OUT_USER=locked_out_user
PROBLEM_USER=problem_user
PERFORMANCE_GLITCH_USER=performance_glitch_user
PASSWORD=secret_sauce

# Browser Configuration
BROWSER=chromium              # chromium | firefox | webkit
HEADLESS=true                 # true | false
SLOWMO_MS=0                   # Slow down actions (ms) for demo/debug
VIDEO=false                   # Record video per test

# Test Configuration
LOG_LEVEL=INFO                # DEBUG | INFO | WARNING | ERROR
DEFAULT_TIMEOUT_MS=5000       # Default timeout for Playwright actions
```

### Pytest Configuration

The project uses `pytest.ini` options defined in `pyproject.toml`:

```toml
[tool.pytest.ini_options]
addopts = "-q --alluredir=allure-results"
markers = [
  "smoke: high-value, fast checks",
  "ui: UI tests",
  "regression: broader coverage",
]
pythonpath = ["src"]
testpaths = ["tests"]
```

## 🏗️ Architecture

### Page Object Model (POM)

The framework follows the Page Object Model pattern to separate test logic from page implementation:

```python
# Example: Login Page Object
from pages.login_page import LoginPage

def test_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_logged_in()
```

### User Flows

Common user journeys are abstracted into reusable flows in `src/services/user_flows.py`:

```python
from services.user_flows import login_flow

def test_valid_login(page):
    inv = login_flow(page, "standard_user", "secret_sauce")
    assert inv.item_count() > 0
```

### Test Data Management

The framework uses:
- **Faker** for dynamic test data generation
- **Pydantic** for data validation and settings management
- **Builder patterns** for complex test data construction

## 📊 Reporting

### Allure Reports

Generate comprehensive Allure reports with test execution details, screenshots, and videos:

```bash
# Run tests with Allure
poetry run pytest --alluredir=allure-results

# Generate and serve Allure report
allure serve allure-results
```

Allure reports include:
- Test execution timeline
- Test case history and trends
- Categorized failures
- Screenshots on failure
- Request/response logs
- Environment information

### HTML Reports

Generate standalone HTML reports using pytest-html:

```bash
poetry run pytest --html=report.html --self-contained-html
```

## 🔄 CI/CD Integration

### GitHub Actions

The project includes a GitHub Actions workflow (`.github/workflows/ci.yml`) that:

1. Sets up Python 3.11
2. Installs Poetry and dependencies
3. Installs Playwright browsers
4. Runs tests in parallel with fast-fail
5. Uploads test reports as artifacts

```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:

jobs:
  tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install Poetry
        uses: abatilo/actions-poetry@v3
        with:
          poetry-version: "1.8.3"

      - name: Install deps
        run: |
          poetry install --no-interaction --no-ansi
          poetry run playwright install --with-deps

      - name: Run tests (headless)
        run: poetry run pytest -n auto --maxfail=1 --dist=loadfile --html=report.html --self-contained-html

      - name: Upload Test Report
        uses: actions/upload-artifact@v4
        with:
          name: test-report
          path: report.html
```

## 🛠️ Development Tools

### Dependency Management with Poetry

Poetry provides several advantages for dependency management:

- **Deterministic builds**: The `poetry.lock` file ensures everyone uses identical dependency versions
- **Dependency resolution**: Automatic conflict resolution between dependencies
- **Simplified workflow**: Single tool for dependency management, virtual environments, and packaging
- **Isolated environments**: Automatic virtual environment creation and management

### Common Poetry Commands

```bash
# Add a new dependency
poetry add package-name

# Add a development dependency
poetry add --group dev package-name

# Update dependencies
poetry update

# Update specific package
poetry update package-name

# Show installed packages
poetry show

# Show dependency tree
poetry show --tree
```

### Code Quality Tools

#### Ruff (Linting)
Fast Python linter with extensive rule coverage:

```bash
# Run linter
poetry run ruff check .

# Auto-fix issues
poetry run ruff check . --fix
```

#### Black (Formatting)
Opinionated code formatter for consistent style:

```bash
# Format code
poetry run black .

# Check formatting without changes
poetry run black . --check
```

#### Pre-commit Hooks
Automatically run quality checks before commits:

```bash
# Install pre-commit hooks
make hooks
# or
poetry run pre-commit install

# Run manually on all files
poetry run pre-commit run --all-files
```

## 🎓 Best Practices

### Test Design
- ✅ Write independent, isolated tests
- ✅ Use descriptive test names that explain behavior
- ✅ Follow AAA pattern (Arrange, Act, Assert)
- ✅ Use Page Object Model for UI interactions
- ✅ Leverage fixtures for setup and teardown

### Wait Strategies
- ✅ Use Playwright's built-in auto-waiting
- ✅ Implement custom wait strategies when needed
- ✅ Avoid hard-coded sleeps (`time.sleep()`)
- ✅ Use explicit waits with meaningful timeouts

### Data Management
- ✅ Keep test data separate from test logic
- ✅ Use data builders for complex objects
- ✅ Leverage Faker for dynamic data generation
- ✅ Store sensitive data in environment variables

### Maintainability
- ✅ Follow the Single Responsibility Principle
- ✅ Keep page objects focused and cohesive
- ✅ Extract reusable flows into service layer
- ✅ Document complex logic with clear comments
- ✅ Review and refactor tests regularly

## 🐛 Troubleshooting

### Common Issues

**Issue**: Playwright browsers not installed
```bash
Solution: Run `poetry run playwright install --with-deps`
```

**Issue**: Tests failing due to timeout
```bash
Solution: Increase timeout in .env file or use custom wait conditions
```

**Issue**: Element not found errors
```bash
Solution: Check selectors and ensure proper wait conditions are implemented
```

**Issue**: Poetry installation fails
```bash
Solution: Update pip first: `pip install --upgrade pip`
Then retry: `poetry install`
```

**Issue**: Pre-commit hooks failing
```bash
Solution: Run `poetry run pre-commit run --all-files` to see specific errors
Auto-fix with: `make fmt`
```

## 📚 Test Coverage

Current test coverage includes:

- ✅ **Login functionality**: Valid/invalid credentials, locked users
- ✅ **Product inventory**: Product listing, filtering, sorting
- ✅ **Shopping cart**: Add/remove items, cart persistence
- ✅ **Checkout flow**: Information entry, order completion
- ✅ **Error handling**: Validation messages, error states

## 📖 Resources

### Official Documentation
- [Playwright Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Allure Framework](https://docs.qameta.io/allure/)
- [Poetry Documentation](https://python-poetry.org/docs/)

### Related Tools
- [pytest-playwright Plugin](https://github.com/microsoft/playwright-pytest)
- [Faker Documentation](https://faker.readthedocs.io/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Ruff Linter](https://docs.astral.sh/ruff/)

### Sauce Demo Application
- [Sauce Demo Website](https://www.saucedemo.com/)
- Test credentials and scenarios available in `.env.example`

## 👤 Author

**Julian Serna**
- GitHub: [@juliansernave](https://github.com/juliansernave)

## 🙏 Acknowledgments

- Built with [Playwright](https://playwright.dev/) by Microsoft
- Test framework powered by [Pytest](https://pytest.org/)
- Reporting by [Allure Framework](https://qameta.io/)
- Dependency management by [Poetry](https://python-poetry.org/)
- Target application: [Sauce Demo](https://www.saucedemo.com/)

---

**Happy Testing! 🎭✨**
