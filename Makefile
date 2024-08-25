env:
	rm -rf .venv/
	uv venv --python 3.12

deps:
	poetry install --no-root

dev:
	uvicorn src.presentation.api.http.asgi:app --reload --port 8000
