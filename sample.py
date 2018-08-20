import inspect

def some_shite(a=None, b=None, c=None, d=None):
    pass

# def some_shite(a, b, *args, **kwargs):
#     pass

# def some_shite(**kwargs):
#     pass

# def some_shite(*args):
#     pass

if __name__ == '__main__':
    params = inspect.signature(some_shite).parameters
    for k,v in params.items():
        print(k)
        print(v.kind)
        print('')
