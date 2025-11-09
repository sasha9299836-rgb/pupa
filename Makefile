install:
	uv sync

VD-games:
	uv run pupa-game

build:
	uv build

package-install:
	uv tool install dist/*.whl

lint:
	uv run ruff check games_project_lazarenko

lint-fix:
	uv run ruff check --fix games_project_lazarenko
