# < Project Name >

## Description

< Service description here >

## Overview

This project is comprised of the following languages and libraries:

* Language: [Python 3.10](https://www.python.org/)
* Package management: [Poetry](https://python-poetry.org/)
* Web framework: [FastAPI](https://fastapi.tiangolo.com/)
* Production web server: [Uvicorn](https://www.uvicorn.org/)
* Dependency injection: [Dependency Injector](https://python-dependency-injector.ets-labs.org/index.html)
* Data parsing and validation: [Pydantic](https://pydantic-docs.helpmanual.io/)
* Functional programming utilities: [Toolz](https://toolz.readthedocs.io/en/latest/)
* Formatter: [Black](https://github.com/psf/black)
* Linter: [Flake8](https://flake8.pycqa.org/en/latest/)
* Static type checker: [Mypy](https://mypy.readthedocs.io/en/stable/index.html)
* Testing: [Pytest](https://docs.pytest.org/en/latest/)

Auxiliary libraries and plugins were omitted but can be found in the `pyproject.toml` file.

## Development

To start development it is recommended to have these utilities installed in a local development machine:

* [Python 3.10](https://www.python.org/)
* [Docker](https://www.docker.com/)
* [Docker Compose 1.29.2](https://docs.docker.com/compose/install/)
* [Git](https://git-scm.com/)
* [Plis](https://github.com/IcaliaLabs/plis)

For better development experience, it is recommended these tools:

* [Visual Studio Code](https://code.visualstudio.com/)
* [Poetry](https://python-poetry.org/)
* [commitizen](https://github.com/commitizen/cz-cli)
* [pre-commit](https://pre-commit.com/)

Be certain that you are installing Poetry with the correct version of Python in your machine, that is, Python 3.

This project is configured with VS Code in mind. To have access of tools and code analysis utilities, you only need to install project dependencies locally with `poetry install` and open the project workspace file on VS Code.

You will need python-dev/python3-dev packages to install packages locally. Please, consult your Linux distribution documentation.

The IDE should be automatically configured with standard rules and options for optimal development experience.

Any other IDE can be supported. If necessary, request a merge with a configuration file in the repository, considering that the development experience is consistent between IDEs and that it doesn't break compatibility and standardization with others.

### Pre-commit hooks

This repository defines pre-commit hooks to help with development.

* To install hooks, run: `pre-commit install`
* To execute hooks, run: `pre-commit run`
* To update hooks run: `pre-commit clean` followed by `pre-commit install`

Hooks will run before each commit when hooks are installed.

### Running the API

To run the API in development mode, follow these steps:

* Build/update image with: `plis build`
* Start a container with: `plis run --service-ports app bash`
* Configure your .env file, example in `.env.example`
* Seed DB data with: `poetry run seeder`
* Start the web server with: `poetry run server`
* Check code style with: `black --check app/ tests/`
* Format code with: `black app/ tests/`
* Lint the code with: `flake8 app/ tests/`
* Run static analysis with: `mypy app/ tests/`
* Test the API with: `pytest -n auto`
* Run entire validation stack with: `black app tests && flake8 app tests && mypy app tests && pytest -n auto`

### Linting, static check and code style guide

Flake8 is the tool of choice for linting. It is configured to warn about code problems, complexity problems, common bugs and to help developers write better code.

Mypy is the tool of choice for static type checking. This project adopts gradual typing as the metodology for code typing. The rules of Mypy will be updated periodically to ensure that the entire code base is typed and consistent.

Black is the tool of choice for formating and code style guide. Black is an uncompromising formatter for Python code, that is, no code style discussions are necessary, the tool is always correct.

Linter and static type checking rules can be discussed and reviewed with the entire team. Any merge request that tries to change these rules without consent is automatically rejected and closed.
