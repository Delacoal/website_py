.PHONY: install local lint cfn-lint flake8 black black-fix isort isort-fix bandit safety test build lint-fix

install: poetry-config
	poetry install

update:
	poetry update

local: install
	poetry run pre-commit install

lint: flake8 black isort cfn-lint

lint-fix: black-fix isort-fix

cfn-lint:
	poetry run cfn-lint

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
