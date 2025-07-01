# llm_course

A Python project with modern tooling

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd llm_course

	2.	Create a virtual environment:

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

	3.	Install dependencies:

pip install -e ".[dev]"

	4.	Set up pre-commit hooks:

pre-commit install

	5.	Copy environment file:

cp .env.template .env
# Edit .env with your actual values

Development

Running Tests

pytest

Code Formatting and Linting

ruff check .
ruff format .
mypy .

Pre-commit Hooks

Pre-commit hooks will automatically run on each commit to ensure code quality.

Project Structure

llm_course/
├── src/
│   └── llm_course/
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .env.template
├── .gitignore
├── .pre-commit-config.yaml
├── .envrc
├── pyproject.toml
└── README.md

License

This project is licensed under the MIT License.
