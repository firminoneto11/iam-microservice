env:
	rm -rf .venv/
	rye sync

deps:
	pip install --upgrade pip setuptools
	poetry install --no-root

dev:
	uvicorn src.presentation.api.http.asgi:app --reload --port 8000
