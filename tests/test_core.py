# -*- coding:utf-8 -*-

"""Users representation tests."""

from gendiff import generate_diff

a = '{\n  - follow: false\n    host: hexlet.io\n' \
    '  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'


def test_find_diff():  # Тест diff для линейных json
    assert generate_diff('tests/files/file1.json', 'tests/files/file2.json') == a


def test_find_diff_yml():  # Тест diff для линейных yml
    assert generate_diff('tests/files/file1.yml', 'tests/files/file2.yml') == a


def test_find_diff_yaml():  # Тест diff для линейных yaml
    assert generate_diff('tests/files/file1.yaml', 'tests/files/file2.yaml') == a


b = '''{\n    common: {\n      + follow: false\n        setting1: Value 1\n      - setting2: 200\n      - setting3: true\n      + setting3: null\n      + setting4: blah blah\n      + setting5: {\n            key5: value5\n        }\n        setting6: {\n            doge: {\n              - wow: \n              + wow: so much\n            }\n            key: value\n          + ops: vops\n        }\n    }\n    group1: {\n      - baz: bas\n      + baz: bars\n        foo: bar\n      - nest: {\n            key: value\n        }\n      + nest: str\n    }\n  - group2: {\n        abc: 12345\n        deep: {\n            id: 45\n        }\n    }\n  + group3: {\n        deep: {\n            id: {\n                number: 45\n            }\n        }\n        fee: 100500\n    }\n}'''


def test_find_diff_tree():  # Тест diff для рекурсивных файлов
    assert generate_diff('tests/files/filepath1.json', 'tests/files/filepath2.json') == b


c = '''Property 'common.follow' was added with value: false\nProperty 'common.setting2' was removed\nProperty 'common.setting3' was updated. From true to null\nProperty 'common.setting4' was added with value: 'blah blah'\nProperty 'common.setting5' was added with value: [complex value]\nProperty 'common.setting6.doge.wow' was updated. From '' to 'so much'\nProperty 'common.setting6.ops' was added with value: 'vops'\nProperty 'group1.baz' was updated. From 'bas' to 'bars'\nProperty 'group1.nest' was updated. From [complex value] to 'str'\nProperty 'group2' was removed\nProperty 'group3' was added with value: [complex value]'''


def test_find_diff_tree_plain():  # Тест diff для рекурсивных файлов с выводом строки формата plain
    assert generate_diff('tests/files/filepath1.json', 'tests/files/filepath2.json', 'plain') == c