
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
