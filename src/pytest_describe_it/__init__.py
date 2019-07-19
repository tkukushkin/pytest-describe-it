import pytest
from _pytest.mark.structures import MarkDecorator


__all__ = ['describe', 'it']


def describe(what: str) -> MarkDecorator:
    return pytest.mark.describe(what)


def it(what: str) -> MarkDecorator:
    return pytest.mark.it(what)
