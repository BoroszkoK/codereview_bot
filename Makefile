.DEFAULT_GOAL := help
.PHONY: help build up down logs migrate makemigrations shell test lint format

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-18s\033[0m %s\n", $$1, $$2}'

build: ## Build all Docker images
	docker compose build

up: ## Start all services (foreground)
	docker compose up

down: ## Stop and remove all containers
	docker compose down

logs: ## Tail logs from all services
	docker compose logs -f

migrate: ## Apply Django database migrations
	docker compose run --rm web python manage.py migrate

makemigrations: ## Create new Django migrations
	docker compose run --rm web python manage.py makemigrations

shell: ## Open a Django shell_plus (falls back to shell)
	docker compose run --rm web python manage.py shell

test: ## Run the test suite with pytest
	docker compose run --rm web pytest

lint: ## Run ruff + mypy
	docker compose run --rm web sh -c "ruff check . && mypy ."

format: ## Auto-format with black + ruff --fix
	docker compose run --rm web sh -c "black . && ruff check --fix ."
