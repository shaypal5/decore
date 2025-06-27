"""Common Python 3 decorators."""

import threading


class ThreadSafeIter:
    """Takes an iterator/generator and makes it thread-safe by locking on calls
    to the `next` method of the given iterator/generator.
    """

    def __init__(self, it):
        self.it = it
        self.lock = threading.Lock()

    def __iter__(self):  # pylint: disable=E0301
        return self

    def __next__(self):
        """Returns the next item in the wrapped iterator."""
        with self.lock:
            return self.it.__next__()


def threadsafe_generator(generator_func):
    """A decorator that takes a generator function and makes it thread-safe."""

    def decoration(*args, **keyword_args):
        """A thread-safe decoration for a generator function."""
        return ThreadSafeIter(generator_func(*args, **keyword_args))

    return decoration


def lazy_property(function):
    """Cache the first return value of a function for all subsequent calls.

    This decorator is usefull for argument-less functions that behave more like
    a global or static property that should be calculated once, but lazily
    (i.e. only if requested).

    """
    cached_val = []

    def _wrapper(*args):
        try:
            return cached_val[0]
        except IndexError:
            ret_val = function(*args)
            cached_val.append(ret_val)
            return ret_val

    return _wrapper
