VENV := .venv
PY := $(VENV)\Scripts\python.exe
REQ := requirements.txt
REQ_DEV := requirements-dev.txt
SCRIPT ?= main.py

.PHONY: help venv install install-dev run test lint format add clean debug

# ----- Help -----
help:
	@echo "Available commands:"
	@echo "  make venv          Create virtual environment"
	@echo "  make install       Install runtime dependencies to venv"
	@echo "  make install-dev   Install dev dependencies to venv"
	@echo "  make run           Run application"
	@echo "  make test          Run tests"
	@echo "  make lint          Run linters"
	@echo "  make format        Format code"
	@echo "  make add PKG=x     Add a dependency to venv"
	@echo "  make clean         Remove venv and caches"

# ----- Core -----
venv:
	@if not exist "$(VENV)" ( python -m venv $(VENV) && echo Virtual environment $(VENV) created! )

install: venv
	$(PY) -m pip install --upgrade pip
	$(PY) -m pip install -r $(REQ)

install-dev: venv
	if exist $(REQ_DEV) ( \
		$(PY) -m pip install -r $(REQ_DEV) \
	)

run: venv
	@$(PY) $(SCRIPT)

debug: venv
	@$(PY) -m pdb $(SCRIPT)

add: venv
	@if "$(PKG)"=="" ( \
		echo Usage: make add PKG=package_name & exit /b 1 \
	)
	@$(PY) -m pip install $(PKG)
	@$(PY) -m pip freeze > $(REQ)

clean:
	@if exist $(VENV) rmdir /s /q $(VENV)
	@if exist __pycache__ rmdir /s /q __pycache__
	@if exist .pytest_cache rmdir /s /q .pytest_cache
	@if exist .mypy_cache rmdir /s /q .mypy_cache
	@if exist *.pyc del /q *.pyc

# ----- Dev Tools -----
test: venv
	@$(PY) -m pytest

lint: venv
	@$(PY) -m flake8 . --exclude $(VENV)
	@$(PY) -m mypy . --strict \
		--warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs

format: venv
	@$(PY) -m black .
