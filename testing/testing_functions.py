import pytest_package
import pytest


def test_add():
    assert pytest_package.add(5, 4) == 9


def test_sub():
    assert pytest_package.sub(3, 2) == 1
