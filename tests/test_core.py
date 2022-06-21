# -*- coding:utf-8 -*-

"""Users representation tests."""

import pytest
from gendiff.core import find_diff


@pytest.fixture
def file1():
    a = '''{
            "host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22",
            "follow": false
            }'''
    return a


@pytest.fixture
def file2():
    a = '''{
            "timeout": 20,
            "verbose": true,
            "host": "hexlet.io"
            }'''
    return a


@pytest.fixture
def res():
    a = '{\n- follow: false\nhost: hexlet.io\n- proxy: 123.234.53.22\n- timeout: 50\n+ timeout: 20\n+ verbose: true\n}'
    return a


def test_find_diff():
    assert find_diff(file1, file2) == res
