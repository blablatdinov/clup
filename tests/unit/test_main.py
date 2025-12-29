# SPDX-FileCopyrightText: Copyright (c) 2024-2026 Almaz Ilaletdinov <a.ilaletdinov@yandex.ru>
# SPDX-License-Identifier: MIT

"""Unit tests."""

from clup.clup import main


def test() -> None:
    """Test main function."""
    got = main(
        '\n'.join([
            '## [Unreleased]',
            '',
            '## [0.1.0] - 2023-05-16',
            '',
            '[unreleased]: https://github.com/olivierlacan/keep-a-changelog/compare/1.1.1...HEAD',
            '[0.1.0]: https://github.com/olivierlacan/keep-a-changelog/tag/0.1.0',
        ]),
        '0.1.1',
        '2023-05-20',
    )

    assert got.strip() == '\n'.join([
        '## [Unreleased]',
        '',
        '## [0.1.1] - 2023-05-20',
        '',
        '## [0.1.0] - 2023-05-16',
        '',
        '[unreleased]: https://github.com/olivierlacan/keep-a-changelog/compare/0.1.1...HEAD',
        '[0.1.1]: https://github.com/olivierlacan/keep-a-changelog/compare/0.1.0...0.1.1',
        '[0.1.0]: https://github.com/olivierlacan/keep-a-changelog/tag/0.1.0',
    ])
