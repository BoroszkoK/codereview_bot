# CodeReview Bot

A GitHub App that listens for pull request events and posts automated code reviews powered by [Claude](https://www.anthropic.com/claude) (Anthropic API).

## Architecture

```
GitHub PR opened/updated
        │
        ▼
POST /api/webhooks/github/   ← GitHubWebhookView (Django)
        │
        ▼
  WebhookEvent saved
  Celery task enqueued
        │
        ▼
  Celery worker processes event
  Fetches PR diff via GitHub API
  Sends diff to Claude API
        │
        ▼
  Review posted back to GitHub PR
  Review saved to DB (Review model)
```

**Stack:** Django · Django REST Framework · Celery · Redis · PostgreSQL · Docker

## Getting Started

### Prerequisites

- Docker and Docker Compose
- A GitHub App with a webhook secret
- An Anthropic API key

### Setup

**1. Clone and configure environment variables:**

```bash
cp .env.example .env
```

Edit `.env` and fill in:

| Variable | Description |
|---|---|
| `DJANGO_SECRET_KEY` | Django secret key |
| `GITHUB_WEBHOOK_SECRET` | Secret set in your GitHub App settings |
| `GITHUB_APP_ID` | Your GitHub App's ID |
| `ANTHROPIC_API_KEY` | Anthropic API key for Claude |

**2. Build Docker images:**

```bash
make build
```

**3. Start all services:**

```bash
make up
```

This starts four containers: `web` (Django on port 8000), `db` (PostgreSQL), `redis`, and `celery` (worker).

**4. Apply database migrations:**

```bash
make migrate
```

The app is now running at `http://localhost:8000`.

### GitHub App configuration

Point your GitHub App's webhook URL to:

```
http://<your-host>/api/webhooks/github/
```

Subscribe to `pull_request` events.

## API Endpoints

| Method | Path | Description |
|---|---|---|
| `POST` | `/api/webhooks/github/` | Receives GitHub webhook events |
| `GET` | `/api/reviews/` | List generated reviews (auth required) |
| `GET` | `/api/reviews/<id>/` | Retrieve a single review (auth required) |
| `GET` | `/admin/` | Django admin |

## Development

| Command | Description |
|---|---|
| `make up` | Start all services |
| `make down` | Stop all containers |
| `make logs` | Tail logs from all services |
| `make migrate` | Apply DB migrations |
| `make makemigrations` | Create new migrations |
| `make shell` | Open a Django shell |
| `make test` | Run the test suite (pytest) |
| `make lint` | Run ruff + mypy |
| `make format` | Auto-format with black + ruff --fix |

## Project Structure

```
apps/
  github_integration/   # GitHubRepository model, GitHub API client
  reviews/              # Review model, read-only API
  webhooks/             # Webhook ingestion endpoint
config/
  settings/
    base.py             # Shared settings
    local.py            # Development overrides
    production.py       # Production overrides
  celery.py             # Celery app configuration
  urls.py               # Root URL configuration
requirements/
  base.txt              # Shared dependencies
  dev.txt               # Development-only dependencies
  prod.txt              # Production-only dependencies
```
