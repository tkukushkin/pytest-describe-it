# pytest-describe-it

[![PyPI version](https://badge.fury.io/py/pytest-describe-it.svg)](https://pypi.org/project/pytest-describe-it/) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pytest-describe-it.svg?color=green) [![Build Status](https://travis-ci.org/tkukushkin/pytest-describe-it.svg?branch=master)](https://travis-ci.org/tkukushkin/pytest-describe-it)

## Example

Some simple test:
```python
import pytest


def add(x: int, y: int) -> int:
    return x + y


@pytest.mark.describe('add')
class TestAdd:

    @pytest.mark.parametrize(['x', 'y', 'expected'], [
        (1, 2, 3),
        (3, 4, 7),
        (5, 6, 10),
    ])
    @pytest.mark.it('returns {expected} for add({x}, {y})')
    def test_add(self, x, y, expected):
        assert add(x, y) == expected

```

Pytest output:
```python
collected 3 items

test_add.py ..F                                                                 [100%]

====================================== FAILURES =======================================
________________ TestAdd.test_add[[ add — returns 10 for add(5, 6) ]] _________________

self = <test_add.TestAdd object at 0x10b740b70>, x = 5, y = 6, expected = 10

    @pytest.mark.parametrize(['x', 'y', 'expected'], [
        (1, 2, 3),
        (3, 4, 7),
        (5, 6, 10),
    ])
    @pytest.mark.it('returns {expected} for add({x}, {y})')
    def test_add(self, x, y, expected):
>       assert add(x, y) == expected
E       assert 11 == 10
E        +  where 11 = add(5, 6)

test_add.py:18: AssertionError
========================= 1 failed, 2 passed in 0.05 seconds ==========================
```

With pytest-sugar:
```python
collecting ...
 test_add.py ✓✓                                                          67% ██████▋

―――――――――――――――― TestAdd.test_add[[ add — returns 10 for add(5, 6) ]] ―――――――――――――――――

self = <test_add.TestAdd object at 0x10e4e3550>, x = 5, y = 6, expected = 10

    @pytest.mark.parametrize(['x', 'y', 'expected'], [
        (1, 2, 3),
        (3, 4, 7),
        (5, 6, 10),
    ])
    @pytest.mark.it('returns {expected} for add({x}, {y})')
    def test_add(self, x, y, expected):
>       assert add(x, y) == expected
E       assert 11 == 10
E        +  where 11 = add(5, 6)

test_add.py:18: AssertionError

 test_add.py ⨯                                                          100% ██████████

Results (0.10s):
       2 passed
       1 failed
         - test_add.py:11 TestAdd.test_add[[ add — returns 10 for add(5, 6) ]]
```
