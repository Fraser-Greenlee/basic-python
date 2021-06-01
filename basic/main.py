
def fizzbuzz(n):
    s = 0
    for i in range(n):
        if i % 3 == 0 and i % 5 == 0:
            print("i")
            continue
        elif i % 3 == 0:
            print("fizz")
            s += 3
            continue
        elif i % 5 == 0:
            print("buzz")
            s -= 1
            continue
        print(i)
    return s


def ops(a, b):
    s = a + b
    s //= b
    s = '.' * s
    s = len(s)
    return a - b


def loops():
    s = 0
    for x in range(3):
        for y in range(3):
            s += 1
    return s


def calls():
    x = 1
    x += 1


def sub_call(t):
    for _ in range(100):
        if not t:
            ops(100, 10)
            calls()
            return make_calls(False)
        else:
            calls()
        return None


def make_calls(t=True):
    while True:
        s = loops()
        x = fizzbuzz(s)
        if t:
            calls()
            sub_call(False)
        else:
            calls()
            calls()
            sub_call(True)
        return None
