SHELL := /bin/bash

ROOT := $(shell git -C "$(CURDIR)" rev-parse --show-toplevel 2>/dev/null || pwd)
VENV ?= $(ROOT)/.venv
PYTHON ?= python3

VENV_PYTHON := $(VENV)/bin/python
PIP_STAMP := $(VENV)/.requirements-installed
BLACK := $(VENV)/bin/black
PYLINT := $(VENV)/bin/pylint
PYTEST := $(VENV)/bin/pytest
PYLINT_FLAGS ?= --disable=all --enable=syntax-error,parse-error --persistent=n
PYLINT_FULL_FLAGS ?= --disable=R,C --persistent=n

.PHONY: all venv install format format-check lint lint-full test check clean

all: install format lint

venv: $(VENV_PYTHON)

$(VENV_PYTHON):
	test -x "$(VENV_PYTHON)" || "$(PYTHON)" -m venv "$(VENV)"

install: $(PIP_STAMP)

$(PIP_STAMP): $(ROOT)/Python/requirements.txt | venv
	"$(VENV_PYTHON)" -m pip install -r "$(ROOT)/Python/requirements.txt"
	touch "$(PIP_STAMP)"

format: install
	cd "$(ROOT)" && git ls-files -z '*.py' | xargs -0 "$(BLACK)"

format-check: install
	cd "$(ROOT)" && git ls-files -z '*.py' | xargs -0 "$(BLACK)" --check

lint: install
	cd "$(ROOT)" && git ls-files -z '*.py' | xargs -0 "$(PYLINT)" $(PYLINT_FLAGS)

lint-full: install
	cd "$(ROOT)" && git ls-files -z '*.py' | xargs -0 "$(PYLINT)" $(PYLINT_FULL_FLAGS)

test: install
	cd "$(ROOT)" && "$(PYTEST)"

check: format-check lint test

clean:
	rm -rf "$(VENV)" .pytest_cache .coverage htmlcov
