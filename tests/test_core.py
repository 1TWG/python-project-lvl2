# -*- coding:utf-8 -*-

"""Users representation tests."""

from gendiff import generate_diff

a = open('./tests/files/answer1.txt').read().rstrip()


def test_find_diff():  # Тест diff для линейных json
    assert generate_diff('tests/files/file1.json', 'tests/files/file2.json') == a


def test_find_diff_yml():  # Тест diff для линейных yml
    assert generate_diff('tests/files/file1.yml', 'tests/files/file2.yml') == a


def test_find_diff_yaml():  # Тест diff для линейных yaml
    assert generate_diff('tests/files/file1.yaml', 'tests/files/file2.yaml') == a


b = open('./tests/files/answer2.txt').read().rstrip()


def test_find_diff_tree():  # Тест diff для рекурсивных файлов
    assert generate_diff('tests/files/filepath1.json', 'tests/files/filepath2.json') == b


d = open('./tests/files/answer2_2.txt').read().rstrip()


def test_find_diff_treeq():  # Тест diff для рекурсивных файлов
    assert generate_diff('tests/files/filepath1_2.json', 'tests/files/filepath2_2.json') == d


c = open('./tests/files/answer3.txt').read().rstrip()


def test_find_diff_tree_plain():  # Тест diff для рекурсивных файлов с выводом строки формата plain
    assert generate_diff('tests/files/filepath1.json', 'tests/files/filepath2.json', 'plain') == c
