from typing import Iterator, Optional

import pytest
from _pytest.config import Config
from _pytest.nodes import Item
from _pytest.python import Class, Function


def pytest_configure(config):
    # type: (Config) -> None
    config.addinivalue_line('markers', 'describe(what)')
    config.addinivalue_line('markers', 'it(what)')


@pytest.mark.trylast
def pytest_itemcollected(item):
    # type: (Function) -> None
    test_path = item._nodeid.rsplit('::', 1)[0]
    params = item.callspec.params if hasattr(item, 'callspec') else {}
    test_description = next(
        (marker.args[0] for marker in item.own_markers if marker.name == 'it'),
        '',
    ).format(**params)
    if not test_description:
        return
    nodes = [
        *filter(None, map(_get_describe_text, _iter_ancestors(item))),
        test_description,
    ]
    item.name = f'{item.function.__name__}[[ {" — ".join(nodes)} ]]'
    item._nodeid = f'{test_path}::{item.name}'


def _iter_ancestors(item):
    # type: (Item) -> Iterator[Item]
    while item.parent is not None:
        yield item.parent
        item = item.parent


def _get_describe_text(item):
    # type: (Item) -> Optional[str]
    return next(
        (marker.args[0] for marker in item.own_markers if marker.name == 'describe'),
        None,
    )
