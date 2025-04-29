#!/usr/bin/env bash

set -x

poetry run black rcs_pydantic_automata --check
poetry run isort --check-only rcs_pydantic_automata
poetry run ruff check --exit-zero rcs_pydantic_automata
