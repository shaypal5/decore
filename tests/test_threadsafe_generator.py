"""Test the threadsafe_generator decorator."""

from queue import Queue
from threading import Thread

from decore import threadsafe_generator


@threadsafe_generator
def make_me_threadsafe():
    """A non-thread-safe generator function."""
    for i in range(0, 10):
        yield i


def read_items(source, n, target):
    """Read and print n items from an iterable, putting them in a queue."""
    for i in range(0, n):
        item = source.__next__()
        print((i, item))
        target.put((i, item))


def test_threadsafe_generator():
    """Test the threadsafe_generator decorator."""
    gen = make_me_threadsafe()
    q1 = Queue(maxsize=10)
    q2 = Queue(maxsize=10)

    t1 = Thread(target=read_items, args=(gen, 4, q1))
    t2 = Thread(target=read_items, args=(gen, 6, q2))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    assert q1.qsize() == 4
    assert q2.qsize() == 6


def test_threadsafe_generator_as_iterator():
    """Test the threadsafe_generator decorator as an iterator."""
    gen = make_me_threadsafe()
    for i in gen:
        print(i)
