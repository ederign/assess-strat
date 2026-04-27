.PHONY: install test clean

install:            ## Install all dependencies via uv
	uv sync

test:               ## Run all tests
	uv run pytest tests/ -v --tb=short

clean:              ## Remove build artifacts
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
