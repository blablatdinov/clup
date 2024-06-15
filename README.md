# Clup (Change log upper)

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
