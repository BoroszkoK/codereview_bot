# syntax=docker/dockerfile:1
FROM python:3.12-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app

# System deps required by psycopg and Pillow (if added later).
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements/base.txt requirements/base.txt
RUN pip install -r requirements/base.txt


# ---------- development ----------
FROM base AS dev

COPY requirements/dev.txt requirements/dev.txt
RUN pip install -r requirements/dev.txt

# Source is bind-mounted at runtime; copy here for image-only use.
COPY . .


# ---------- production ----------
FROM base AS prod

COPY requirements/prod.txt requirements/prod.txt
RUN pip install -r requirements/prod.txt

COPY . .

EXPOSE 8000
CMD ["gunicorn", "config.wsgi:application", \
     "--bind", "0.0.0.0:8000", \
     "--workers", "2", \
     "--timeout", "60"]
