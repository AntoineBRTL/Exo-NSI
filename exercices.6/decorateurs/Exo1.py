def deux_fois(func):
    def warper(*args, **kwargs):
        v1 = func(*args, **kwargs)
        v2 = func(*args, **kwargs)
        return v1, v2
    return warper

@deux_fois
def dit_bonjour():
    print("bonjour")