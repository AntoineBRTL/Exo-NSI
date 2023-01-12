admin = False

def admin_requis(func):
    def warper(*args, **kwargs):
        if admin:
            return func(*args, **kwargs)
        raise RuntimeError()
    return warper
        
@admin_requis
def test():
    print("test")