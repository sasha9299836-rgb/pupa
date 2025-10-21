install:
	uv sync

VD-games:
	uv run pupa-game

build:
	uv build

package-install:
	uv tool install dist/*.whl
