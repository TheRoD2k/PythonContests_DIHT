import traceback


def force_load(file_name):
    file = open(file_name + '.py', 'rt')
    lines = file.readlines()
    ldict = {}
    while True:
        try:
            exec(''.join(lines), globals(), ldict)
        except SyntaxError as syntax_exception:
            str_index = syntax_exception.lineno
        except Exception as exception:
            str_index = exception.__traceback__.tb_next.tb_lineno
        else:
            break

        lines.pop(str_index - 1)
        ldict = {}
    return ldict
