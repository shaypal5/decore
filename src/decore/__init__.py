"""Utility pure-Python 3 decorators."""

from ._version import *  # noqa: F403
from .decore import (
    ThreadSafeIter as ThreadSafeIter,
)
from .decore import (
    lazy_property as lazy_property,
)
from .decore import (
    threadsafe_generator as threadsafe_generator,
)
