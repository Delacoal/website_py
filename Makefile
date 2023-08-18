.PHONY: install local lint flake8 black black-fix isort isort-fix bandit safety test build lint-fix

install:
	poetry install

update:
	poetry update

local: install
	poetry run pre-commit install

lint: flake8 black isort cfn-lint

lint-fix: black-fix isort-fix

flake8:
	poetry run flake8

black:
	poetry run black --diff --check .

black-fix:
	poetry run black .

isort:
	poetry run isort --diff --check .

isort-fix:
	poetry run isort .

safety:
	poetry export -f requirements.txt | poetry run safety check --stdin

test:
	pytest 