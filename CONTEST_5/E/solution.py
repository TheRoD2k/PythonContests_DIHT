import import_me

def get_all_functions():
    membs = dir(import_me)
    answer = []
    for i in membs:
        if callable(getattr(import_me, i)):
            answer.append(i)
    return answer
