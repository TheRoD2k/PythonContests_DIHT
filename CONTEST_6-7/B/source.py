import numbers
import collections.abc
from app import VeryImportantClass, decorator


class HackedClass(VeryImportantClass):
    def __getattribute__(self, obj):
        attribute = super().__getattribute__(obj)
        if obj.startswith('_'):
            return attribute
        if callable(attribute):
            return decorator(attribute)
        if isinstance(attribute, numbers.Number):
            return attribute * 2
        if isinstance(attribute, collections.abc.Iterable):
            return type(attribute)()
        return attribute
