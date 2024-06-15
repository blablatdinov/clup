# Clup (Change log upper)

[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![PyPI version](https://badge.fury.io/py/clup.svg)](https://badge.fury.io/py/clup)
![CI status](https://github.com/blablatdinov/clup/actions/workflows/pr-check.yml/badge.svg?branch=master)
[![Lines of code](https://tokei.rs/b1/github/blablatdinov/clup)](https://github.com/XAMPPRocky/tokei_rs)
[![Hits-of-Code](https://hitsofcode.com/github/blablatdinov/clup)](https://hitsofcode.com/github/blablatdinov/clup/view)

This Python script updates a CHANGELOG.md file by adding a new version entry with the specified version number and date.

## Features:

- Adds a new version entry under the "Unreleased" section.
- Updates the link for the "Unreleased" section to point to the new version.
- Generates a comparison link for the new version against the previous one.

## Installation

```bash
pip install clup
```

## Usage

To run the script, use the following command:

```bash
python script.py <path_to_changelog> <new_version> <release_date>
```

Arguments:

- <path_to_changelog>: Path to the CHANGELOG.md file. (Default: CHANGELOG.md)
- <new_version>: New version number to be added. (e.g., 1.0.1)
- <release_date>: Release date for the new version. (e.g., 2024-06-15)

Example

```bash
python script.py CHANGELOG.md 1.0.1 2024-06-15
```

This command will update the CHANGELOG.md file by adding an entry for version 1.0.1 with the release date 2024-06-15.

## License

This project is licensed under the MIT License.
