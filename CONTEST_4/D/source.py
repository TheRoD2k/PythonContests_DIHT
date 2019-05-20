from collections import OrderedDict


def cache(n):
    def cache_or_recall(function):
        cached = OrderedDict()
        count = 0

        def decorate(*args, **kwargs):
            nonlocal count
            value = args + tuple(kwargs.values())
            if value not in cached:
                cached[value] = function(*args, **kwargs)
                count += 1
                if count > n:
                    cached.popitem(False)
            return cached[value]
        decorate.__name__ = function.__name__
        decorate.__doc__ = function.__doc__
        decorate.__module__ = function.__module__
        return decorate
    return cache_or_recall
