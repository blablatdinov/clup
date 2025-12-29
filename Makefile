# SPDX-FileCopyrightText: Copyright (c) 2024-2026 Almaz Ilaletdinov <a.ilaletdinov@yandex.ru>
# SPDX-License-Identifier: MIT

lint:
	poetry run isort clup tests
	poetry run ruff check clup tests --fix
	poetry run flake8 clup tests
	poetry run mypy clup tests --strict

test: unit it

unit:
	poetry run pytest tests/unit --cov=clup --cov-report=term-missing:skip-covered -vv

it:  # integration tests
	poetry run pytest tests/it -s -vv

clean:
	git clean -f -d -x
