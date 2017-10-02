decore
#########

A small pure-python package for utility decorators.

.. code-block:: python

  from decore import lazy_property

  @lazy_property
  def some_big_calc(param_array):
    sub_res = [big_func(param) for param in param_array]
    return sum(sub_res)


Installation
============

Install ``decore`` with:

.. code-block:: bash

  pip install decore


Credits
=======
Created by Shay Palachy  (shay.palachy@gmail.com).
