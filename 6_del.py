def corotune(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


class BlaBlaException(Exception):
    pass



def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            print('hi')
        else:
            print('-----', message)

    return 'hi ho'


@corotune
def delegator(g):
    result = yield from g

    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
