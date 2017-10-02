"""Testing the lazy_property decorator."""

from random import randint

from decore import lazy_property


@lazy_property
def cache_me():
    """We want this function's results to be cached."""
    return randint(1, 999999)


def test_lazy_property():
    """Basic test of the lazy_property decorator."""

    first_res = cache_me()
    sec_res = cache_me()
    assert first_res == sec_res
