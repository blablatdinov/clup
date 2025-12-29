# SPDX-FileCopyrightText: Copyright (c) 2024-2026 Almaz Ilaletdinov <a.ilaletdinov@yandex.ru>
# SPDX-License-Identifier: MIT

"""Integration test with installation."""

import os
import shutil
import subprocess
from collections.abc import Generator
from pathlib import Path

import pytest
from _pytest.legacypath import TempdirFactory


@pytest.fixture(scope='module')
def current_dir() -> Path:
    """Current directory for installing actual clup."""
    return Path().absolute()


# flake8: noqa: S603, S607. Not a production code
@pytest.fixture(scope='module')
def test_dir(tmpdir_factory: TempdirFactory, current_dir: Path) -> Generator[Path, None, None]:
    """Testing directory."""
    tmp_path = tmpdir_factory.mktemp('clup-test')
    shutil.copy(current_dir / 'tests/fixtures/changelog.md', tmp_path / 'changelog.md')
    os.chdir(tmp_path)
    subprocess.run(['python', '-m', 'venv', 'venv'], check=True)
    subprocess.run(['venv/bin/pip', 'install', 'pip', '-U'], check=True)
    subprocess.run(['venv/bin/pip', 'install', str(current_dir)], check=True)
    yield tmp_path
    os.chdir(current_dir)


def test(current_dir: Path, test_dir: Path) -> None:
    """Test run via subprocess."""
    got = subprocess.run(
        ['venv/bin/clup', 'changelog.md', '1.1.2', '2024-06-15'],
        stdout=subprocess.PIPE,
        check=False,
    )

    assert got.returncode == 0
    assert (
        (test_dir / 'changelog.md').read_text(encoding='utf-8')
        == (current_dir / 'tests/fixtures/expected_out.md').read_text(encoding='utf-8')
    )
