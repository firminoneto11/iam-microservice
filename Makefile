env:
	rm -rf venv/
	python3.12 -m venv venv

deps:
	pip install --upgrade pip setuptools
	poetry install --no-root

dev:
	uvicorn src.presentation.api.rest.asgi:app --reload --port 8000
