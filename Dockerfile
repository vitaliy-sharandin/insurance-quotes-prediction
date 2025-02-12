FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

COPY src/app/ /app
COPY pyproject.toml uv.lock /

WORKDIR /
RUN uv sync --frozen --no-cache

CMD ["/.venv/bin/fastapi", "run", "app/main.py", "--port", "80", "--host", "0.0.0.0"]