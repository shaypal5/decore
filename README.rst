decore
#########
|PyPI-Status| |PyPI-Versions| |Build-Status| |Codecov| |LICENCE|

A small pure-python package for utility decorators.

.. code-block:: python

  from decore import lazy_property

  @lazy_property
  def paramless_big_calc():
    sub_res = [big_func(const) for const in array_of_constants]
    return sum(sub_res)

.. contents::

.. section-numbering::


Decorators
==========

lazy_property
-------------

The ``lazy_property`` decorator is meant to decorate functions that compute some constant value or property that you only want to compute once. The first call to the decorated function will run it and save the value (in memory) before returning it; subsequent calls will get this value without trigerring the calculation.

You can think on it like ``functools.lru_cache(maxsize=1)`` for functions with no parameters.

.. code-block:: python

  from decore import lazy_property

  @lazy_property
  def paramless_big_calc():
    sub_res = [big_func(const) for const in array_of_constants]
    return sum(sub_res)


threadsafe_generator
--------------------

The ``threadsafe_generator`` decorator makes iterables - both generators and iterators - threadsafe. This means multiple threads can be given references to the decorated iterable and it is guarenteed that each item will be yielded (or returned) to only a single thread.

.. code-block:: python

  from decore import threadsafe_generator

  @threadsafe_generator
  def user_documents(day):
    client = get_mongodb_client(some_params)
    dt_obj = translate_day_to_dt(day)
    user_document_cursor = client.some_mongodb_query(dt_obj, some_const)
    return user_document_cursor


Installation
============

Install ``decore`` with:

.. code-block:: bash

  pip install decore


Credits
=======
Created by Shay Palachy  (shay.palachy@gmail.com).

.. |PyPI-Status| image:: https://img.shields.io/pypi/v/decore.svg
  :target: https://pypi.python.org/pypi/decore

.. |PyPI-Versions| image:: https://img.shields.io/pypi/pyversions/decore.svg
   :target: https://pypi.python.org/pypi/decore

.. |Build-Status| image:: https://travis-ci.org/shaypal5/decore.svg?branch=master
  :target: https://travis-ci.org/shaypal5/decore

.. |LICENCE| image:: https://img.shields.io/pypi/l/decore.svg
  :target: https://pypi.python.org/pypi/decore

.. |Codecov| image:: https://codecov.io/github/shaypal5/decore/coverage.svg?branch=master
   :target: https://codecov.io/github/shaypal5/decore?branch=master
