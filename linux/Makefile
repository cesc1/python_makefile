VENV := .venv
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
REQ := requirements.txt
REQ_DEV := requirements-dev.txt
SCRIPT ?= main.py

.PHONY: help venv install install-dev run test lint format add clean debug


# ----- Help -----
help:
	@echo "Available commands:"
	@echo "  make venv			Create virtual environment"
	@echo "  make install		Install runtime dependencies to venv"
	@echo "  make install-dev	Install dev dependencies to venv"
	@echo "  make run			Run application"
	@echo "  make test			Run tests"
	@echo "  make lint			Run linters"
	@echo "  make format		Format code"
	@echo "  make add PKG=x		Add a dependency to venv"
	@echo "  make clean			Remove venv and caches"
# ----- Core -----

venv: $(VENV)

$(VENV):
	python3 -m venv $(VENV)

install: venv
	@$(PIP) install --upgrade pip
	@$(PIP) install -r $(REQ)

install-dev: venv
	@if [ -f $(REQ_DEV) ]; then $(PIP) install -r $(REQ_DEV); fi

run: venv
	@$(PY) $(SCRIPT)

debug: venv
	@$(PY) -m pdb $(SCRIPT)

add: venv
	@if [ -z "$(PKG)" ]; then echo "Usage: make add PKG=package_name"; exit 1; fi
	@$(PIP) install $(PKG)
	@$(PIP) freeze > $(REQ)

clean:
	@rm -rf $(VENV) __pycache__ .pytest_cache .mypy_cache


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


