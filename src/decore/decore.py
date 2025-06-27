"""Common Python 3 decorators."""

import threading


class ThreadSafeIter:
    """Make an iterator/generator thread-safe.

    Take an iterator/generator and makes it thread-safe by
    locking on calls to the `next` method of the given iterator/generator.

    """

    def __init__(self, it):
        """Initialize the ThreadSafeIter with the given iterator."""
        self.it = it
        self.lock = threading.Lock()

    def __iter__(self):  # pylint: disable=E0301
        """Return the iterator itself."""
        return self

    def __next__(self):
        """Return the next item in the wrapped iterator."""
        with self.lock:
            return self.it.__next__()


def threadsafe_generator(generator_func):
    """Make a generator function thread-safe."""

    def decoration(*args, **keyword_args):
        """Decorate a generator function, thread-safe."""
        return ThreadSafeIter(generator_func(*args, **keyword_args))

    return decoration


def lazy_property(function):
    """Cache the first return value of a function for all subsequent calls.

    This decorator is useful for argument-less functions that behave more like
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
