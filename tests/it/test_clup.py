# SPDX-FileCopyrightText: Copyright (c) 2024-2026 Almaz Ilaletdinov <a.ilaletdinov@yandex.ru>
# SPDX-License-Identifier: MIT

"""Integraiton tests."""

from pathlib import Path

from clup.clup import main


def test() -> None:
    """Test with text files examples."""
    got = main(Path('tests/fixtures/changelog.md').read_text(), '1.1.2', '2024-06-15')

    assert got == Path('tests/fixtures/expected_out.md').read_text()
