"""
test file
"""
from project.main import demo


def test_demo() -> None:
    """
    test function of demo
    """
    # Secure one
    if __debug__:
        if demo() != 200:
            raise AssertionError("status code error!")
