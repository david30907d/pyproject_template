import pytest

from project.main import demo


def test_demo():
    if __debug__:
        if demo() != 200:
            raise AssertionError("status code error!")
