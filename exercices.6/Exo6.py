import time

def mesurePerf(func):
    def warper(*args, **kwargs):
        start = time.perf_counter()
        value = func(*args, **kwargs)
        end = time.perf_counter()
        print(end - start)
        return value
    return warper

@mesurePerf
def test(text):
    print("bonjour", text)

test("fonction de test")