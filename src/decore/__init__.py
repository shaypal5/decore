"""Utility pure-Python 3 decorators."""

from ._version import *  # noqa: F403
from .decore import (
    ThreadSafeIter as ThreadSafeIter,
    threadsafe_generator as threadsafe_generator,
    lazy_property as lazy_property,
)
