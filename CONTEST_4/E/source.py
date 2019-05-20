import time
import inspect


def profiler(function):
    def add_function(*args, **kwargs):
        if function.__name__ == inspect.stack()[1][3]:
            add_function.calls += 1
        else:
            add_function.calls = 1
        first_time = time.clock()
        func_value = function(*args, **kwargs)
        add_function.last_time_taken = time.clock() - first_time
        return func_value
    add_function.__name__ = function.__name__
    add_function.__doc__ = function.__doc__
    add_function.__module__ = function.__module__
    add_function.calls = 1
    return add_function
