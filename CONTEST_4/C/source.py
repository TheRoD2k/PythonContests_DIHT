import sys


def takes(*types):
    def decorator(func):
        def new_func(*args):
            for i in range(min(len(types), len(args))):
                if not isinstance(args[i], types[i]):
                    raise TypeError
            return func(*args)

        new_func.__name__ = func.__name__
        new_func.__doc__ = func.__doc__
        return new_func

    return decorator


exec(sys.stdin.read())
