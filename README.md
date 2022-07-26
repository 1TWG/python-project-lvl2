### Hexlet tests and linter status:
[![Actions Status](https://github.com/1TWG/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/1TWG/python-project-lvl2/actions)
<br>
[![Actions Status](https://github.com/1TWG/python-project-lvl2/workflows/linter-test-check/badge.svg)](https://github.com/1TWG/python-project-lvl2/actions)
<br>
[![Maintainability](https://api.codeclimate.com/v1/badges/e2fc300ec1b30d21e3e5/maintainability)](https://codeclimate.com/github/1TWG/python-project-lvl2/maintainability)
<br>
[![Test Coverage](https://api.codeclimate.com/v1/badges/e2fc300ec1b30d21e3e5/test_coverage)](https://codeclimate.com/github/1TWG/python-project-lvl2/test_coverage)

## Installation:
```sh
pip install --user git+https://github.com/1TWG/python-project-lvl2.git
```

### Usage as a cli utility
```
gendiff [-h] [-f [--format] FORMAT] first_file second_file
```
Supported file formats: JSON, YAML

'stylish' format:
```
gendiff --format stylish first_file second_file
```

'plain' format
```
gendiff --format plain first_file second_file
```

inner json representation of diff AST: 
```
gendiff --format json first_file second_file
```
<a href="https://asciinema.org/a/6SdFcQmIj8tmFKhYnlZwJSKCr" target="_blank"><img src="https://asciinema.org/a/6SdFcQmIj8tmFKhYnlZwJSKCr.svg" /></a>
