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

# Allure Reporting Guide 📊

Esta guía explica cómo usar Allure para generar reportes detallados de tus tests.

## 🎯 ¿Qué es Allure?

Allure es un framework de reporting flexible y ligero que muestra una representación clara de lo que se ha probado de manera concisa. Permite a todos los miembros del equipo (stakeholders, desarrolladores, QA) extraer la máxima información del proceso de testing diario.

## 📦 Instalación de Allure Commandline

### macOS
```bash
brew install allure
```

### Windows
```bash
scoop install allure
```

### Linux
```bash
# Descargar la última versión
wget https://github.com/allure-framework/allure2/releases/download/2.25.0/allure-2.25.0.tgz

# Extraer
tar -zxvf allure-2.25.0.tgz

# Agregar al PATH
export PATH=$PATH:/path/to/allure-2.25.0/bin
```

Verifica la instalación:
```bash
allure --version
```

## 🚀 Uso Rápido

### Opción 1: Generar y servir reporte en un comando
```bash
make allure-serve
```

Este comando:
1. Ejecuta todos los tests
2. Genera resultados en `allure-results/`
3. Abre automáticamente el reporte en tu navegador

### Opción 2: Generar reporte HTML estático
```bash
make allure-report
```

Luego abre `allure-report/index.html` en tu navegador.

### Opción 3: Comandos individuales
```bash
# 1. Ejecutar tests y generar resultados
poetry run pytest --alluredir=allure-results

# 2. Generar reporte HTML
allure generate allure-results --clean -o allure-report

# 3. Abrir reporte
allure open allure-report
```

## 📝 Decoradores de Allure

### Organización de Tests

```python
import allure

@allure.epic("E-Commerce Platform")        # Nivel más alto - módulo completo
@allure.feature("Shopping Cart")           # Feature específica
@allure.story("Add to Cart")               # User story
@allure.title("User can add items to cart")
def test_add_to_cart():
    pass
```

### Severidad

```python
@allure.severity(allure.severity_level.BLOCKER)    # Bloquea todo el sistema
@allure.severity(allure.severity_level.CRITICAL)   # Funcionalidad crítica
@allure.severity(allure.severity_level.NORMAL)     # Funcionalidad normal
@allure.severity(allure.severity_level.MINOR)      # Funcionalidad menor
@allure.severity(allure.severity_level.TRIVIAL)    # Cosmético
def test_example():
    pass
```

### Tags y Labels

```python
@allure.tag("smoke", "authentication", "api")
@allure.label("owner", "julian.serna")
@allure.label("layer", "ui")
def test_example():
    pass
```

### Links

```python
@allure.link("https://jira.company.com/browse/PROJ-123", name="JIRA Ticket")
@allure.issue("PROJ-456", "Bug Report")
@allure.testcase("TC-789", "Test Case")
def test_example():
    pass
```

## 🎬 Steps (Pasos)

Los steps hacen que el reporte sea más legible:

```python
import allure

def test_login():
    with allure.step("Navigate to login page"):
        page.goto("/login")

    with allure.step("Enter credentials"):
        page.fill("#username", "user@example.com")
        page.fill("#password", "password123")

    with allure.step("Click login button"):
        page.click("#login-btn")

    with allure.step("Verify successful login"):
        assert page.locator(".welcome-message").is_visible()
```

## 📎 Attachments (Adjuntos)

Agrega evidencia a tus tests:

```python
import allure

# Screenshot
allure.attach(
    page.screenshot(),
    name="screenshot",
    attachment_type=allure.attachment_type.PNG
)

# HTML
allure.attach(
    page.content(),
    name="page_html",
    attachment_type=allure.attachment_type.HTML
)

# JSON
allure.attach(
    json.dumps(data),
    name="response_data",
    attachment_type=allure.attachment_type.JSON
)

# Text
allure.attach(
    "Some important information",
    name="notes",
    attachment_type=allure.attachment_type.TEXT
)
```

## 🔄 Fixtures con Allure

```python
import allure
import pytest

@pytest.fixture
def setup_user():
    with allure.step("Create test user"):
        user = create_user()

    yield user

    with allure.step("Cleanup test user"):
        delete_user(user)
```

## 📊 Parametrización

```python
import allure
import pytest

@pytest.mark.parametrize(
    "username,password,expected_error",
    [
        pytest.param(
            "invalid@test.com",
            "wrong",
            "Invalid credentials",
            id="invalid_credentials",
            marks=allure.label("test_type", "negative")
        ),
    ]
)
def test_login_failures(username, password, expected_error):
    with allure.step(f"Try login with {username}"):
        # Test code here
        pass
```

## 🎨 Mejores Prácticas

### ✅ DO's

1. **Usa steps descriptivos**
   ```python
   with allure.step("User fills checkout form with valid data"):
       # código
   ```

2. **Adjunta evidencia relevante**
   ```python
   allure.attach(screenshot, name="error_state", attachment_type=PNG)
   ```

3. **Organiza jerárquicamente**
   - Epic → Feature → Story → Test

4. **Agrega contexto**
   ```python
   allure.attach(f"User ID: {user_id}", name="Test Data", attachment_type=TEXT)
   ```

5. **Usa severidad apropiada**
   - BLOCKER para funcionalidad crítica
   - CRITICAL para features importantes
   - NORMAL para funcionalidad estándar

### ❌ DON'Ts

1. **No uses steps para cada línea**
   ```python
   # ❌ Demasiado granular
   with allure.step("Click button"):
       page.click("#btn")

   # ✅ Mejor
   with allure.step("Complete checkout process"):
       page.click("#checkout")
       page.fill("#card", "1234")
       page.click("#submit")
   ```

2. **No adjuntes archivos innecesarios**
   - Solo adjunta en caso de fallo o información crítica

3. **No uses titles genéricos**
   ```python
   # ❌ Malo
   @allure.title("Test 1")

   # ✅ Bueno
   @allure.title("User can successfully complete checkout with valid credit card")
   ```

## 📈 Características del Reporte

El reporte de Allure incluye:

1. **Overview**: Vista general con estadísticas
2. **Categories**: Clasificación de fallos
3. **Suites**: Tests organizados por suites
4. **Graphs**: Gráficos de tendencias y distribución
5. **Timeline**: Línea de tiempo de ejecución
6. **Behaviors**: Organización por BDD (Epic/Feature/Story)
7. **Packages**: Organización por estructura de carpetas

## 🔧 Configuración Avanzada

### Categorías de Fallos

Crea `categories.json` en `allure-results/`:

```json
[
  {
    "name": "Product defects",
    "matchedStatuses": ["failed"],
    "messageRegex": ".*AssertionError.*"
  },
  {
    "name": "Test defects",
    "matchedStatuses": ["broken"],
    "messageRegex": ".*RuntimeError.*"
  },
  {
    "name": "Ignored tests",
    "matchedStatuses": ["skipped"]
  }
]
```

### Environment Info

Ya está configurado en `conftest.py`, pero puedes personalizarlo:

```python
@pytest.fixture(scope="session", autouse=True)
def configure_allure_environment():
    allure_results_dir = Path("allure-results")
    environment_properties = {
        "Browser": "Chrome",
        "Environment": "QA",
        "Build": "1.0.0",
        # Agrega más propiedades
    }
    # Escribir al archivo
```

## 🚀 CI/CD Integration

### GitHub Actions

Ya incluido en `.github/workflows/ci.yml`:

```yaml
- name: Run tests
  run: poetry run pytest --alluredir=allure-results

- name: Get Allure history
  uses: actions/checkout@v2
  if: always()
  continue-on-error: true
  with:
    ref: gh-pages
    path: gh-pages

- name: Allure Report action
  uses: simple-elf/allure-report-action@master
  if: always()
  with:
    allure_results: allure-results
    allure_history: allure-history
    keep_reports: 20
```

## 📚 Recursos Adicionales

- [Documentación Oficial de Allure](https://docs.qameta.io/allure/)
- [Allure Python Integrations](https://docs.qameta.io/allure/#_python)
- [Allure Report Examples](https://demo.qameta.io/allure/)

## 🔍 Ejemplos en el Proyecto

Revisa estos archivos para ver ejemplos completos:

- `tests/test_login.py` - Decoradores básicos
- `tests/test_checkout_smoke.py` - Steps y attachments
- `tests/additional_test_cases.py` - Ejemplos avanzados
- `tests/conftest.py` - Configuración de Allure

## 💡 Tips Profesionales

1. **Usa dynamic titles** para tests parametrizados:
   ```python
   @allure.title("Login with {username} should return {expected_status}")
   def test_login(username, expected_status):
       pass
   ```

2. **Documenta tu API** con descriptions:
   ```python
   @allure.description("""
   This test verifies:
   - User authentication
   - Session creation
   - Token generation
   """)
   ```

3. **Agrupa tests relacionados** con tags:
   ```python
   @allure.tag("smoke", "regression", "auth")
   ```

---

**🎉 ¡Listo! Ahora tienes Allure completamente configurado.**

Para generar tu primer reporte:
```bash
make allure-serve
```

**Happy Testing! 🎭✨**
