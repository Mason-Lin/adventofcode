"""
.. module:: filter
   :synopsis:
      iterable object filter
.. moduleauthor:: Mason Lin

This module help to filter some iterable objects by predefind criteria.
"""

from collections.abc import Callable


class Filter(Callable):
    """Filter defines the interface of filter.
    All kinds of filter should follow Filter
    filter init with a callable function
    filter should implement the __call__ method
    it can be called with a input object and it will return boolean
    it can work with operator such as &, | , ^, ~

    `True` means input matches the criteria it looks for
    `False` means input doesn't match the criteria."""

    def __init__(self, function):
        if callable(function):
            self._filters = function
        else:
            raise TypeError("Input should be a function")

    def __call__(self, x) -> bool:
        return bool(self._filters(x))

    def __add__(self, other):
        return Filter(lambda x: self(x) and other(x))

    def __and__(self, other):
        return Filter(lambda x: self(x) and other(x))

    def __or__(self, other):
        return Filter(lambda x: self(x) or other(x))

    def __xor__(self, other):
        return Filter(lambda x: self(x) != other(x))

    def __sub__(self, other):
        return Filter(lambda x: self(x) and not other(x))

    def __truediv__(self, other):
        return Filter(lambda x: self(x) and not other(x))

    def __invert__(self):
        return Filter(lambda x: not self(x))

    def filtered(self, objects):
        return list(filter(self._filters, objects))


always_false_filter = Filter(lambda x: False)
always_true_filter = Filter(lambda x: True)
