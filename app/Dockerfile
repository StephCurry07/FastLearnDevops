FROM ghcr.io/astral-sh/uv:python3.9-bookworm

WORKDIR /app

# Copy dependency files first
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --no-dev

# Copy only the app code (not the whole folder)
COPY main.py .

EXPOSE 8001

CMD ["uv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]

