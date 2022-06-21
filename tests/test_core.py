# -*- coding:utf-8 -*-

"""Users representation tests."""

from gendiff import generate_diff


def test_find_diff():  # Тест diff для линейных json
    a = '{\n  - follow: false\n    host: hexlet.io\n' \
        '  - proxy: 123.234.53.22\n  + timeout: 20\n  - timeout: 50\n  + verbose: true\n}'
    assert generate_diff('tests/files/file1.json', 'tests/files/file2.json') == a
