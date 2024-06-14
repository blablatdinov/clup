# The MIT License (MIT).
#
# Copyright (c) 2024 Almaz Ilaletdinov <a.ilaletdinov@yandex.ru>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.

import re

ChangelogStr = str
NewVersionNumStr = str
DateStr = str


def main(changelog: ChangelogStr, version: NewVersionNumStr, date: DateStr) -> ChangelogStr:
    res = []
    changelog_lines = changelog.splitlines()
    for idx, line in enumerate(changelog_lines):
        if line == '## [Unreleased]':
            res.append('## [Unreleased]\n')
            res.append('## [{0}] - {1}'.format(version, date))
            continue
        if line.startswith('[unreleased]: '):
            previous_version = re.findall(r'\[(.*)\]', changelog_lines[idx + 1])[0]
            repo = '/'.join(line.split(' ')[1].split('/')[:-2])
            res.append('[unreleased]: {0}/compare/{1}...HEAD'.format(repo, version))
            res.append('[{0}]: {1}/compare/{2}...{3}'.format(version, repo, previous_version, version))
            continue
        res.append(line)
    return '\n'.join(res) + '\n'
