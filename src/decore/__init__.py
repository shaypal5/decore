"""Utility pure-Python 3 decorators."""

from .decore import (
    ThreadSafeIter,
    threadsafe_generator,
    lazy_property
)
try:
    del decore
except NameError: # pragma: no cover
    pass

from ._version import *  # noqa: F403
