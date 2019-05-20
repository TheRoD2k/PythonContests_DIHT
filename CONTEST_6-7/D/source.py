from contextlib import contextmanager
import traceback
import sys
from io import StringIO


@contextmanager
def supresser(*types):
    try:
        yield
    except types:
        pass


@contextmanager
def retyper(input, output):
    try:
        yield
    except input:
        tup = sys.exc_info()
        exception = tup[1]
        trace = tup[2]
        new_exception = output().with_traceback(trace)
        new_exception.args = exception.args
        raise new_exception


@contextmanager
def dumper(output):
    try:
        yield
    except Exception as exception:
        error_string = traceback.format_exception_only(exception.__class__, exception)
        error_string[0] = error_string[0][:-1]
        error_string += traceback.format_exc().split('\n')
        output.write('\n'.join(error_string))
