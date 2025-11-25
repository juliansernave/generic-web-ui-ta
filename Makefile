.PHONY: install test report lint fmt fix hooks ci clean

install:
	poetry install
	poetry run playwright install --with-deps

test:
	poetry run pytest -n auto --maxfail=1 --dist=loadfile -q

report:
	poetry run pytest -n auto --maxfail=1 --dist=loadfile \
		--html=report.html --self-contained-html

allure-report:
	poetry run pytest --alluredir=allure-results
	allure generate allure-results --clean -o allure-report

allure-serve:
	poetry run pytest --alluredir=allure-results
	allure serve allure-results

allure-clean:
	rm -rf allure-results allure-report

# Lint: Check for issues without modifying files
lint:
	poetry run ruff check .

# Fix: Auto-fix ALL issues (imports, formatting, style)
fix:
	poetry run ruff check . --fix
	poetry run ruff format .
	poetry run black .

# Format only (no linting)
fmt:
	poetry run ruff format .
	poetry run black .

hooks:
	poetry run pre-commit install

# Run pre-commit on all files (useful before big commits)
pre-commit-all:
	poetry run pre-commit run --all-files

clean:
	rm -rf allure-results allure-report .pytest_cache .ruff_cache __pycache__ .coverage

hooks:
	poetry run pre-commit install
