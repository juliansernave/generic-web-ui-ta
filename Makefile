.PHONY: install test report lint fmt hooks ci

install:
	poetry install
	poetry run playwright install --with-deps

test:
	poetry run pytest -n auto --maxfail=1 --dist=loadfile -q

report:
	poetry run pytest -n auto --maxfail=1 --dist=loadfile \
		--html=report.html --self-contained-html

lint:
	poetry run ruff check .
	poetry run mypy src

fmt:
	poetry run ruff check . --fix
	poetry run black .

hooks:
	poetry run pre-commit install
