def divide(p, a):
    if len(a) < 1:
        return ([], [])
    x, y = divide(p, a[1:])
    b = a[0]
    if b < p:
        return ([b], x, y)
    else:
        return (x, [b] + y)

def quick_sort(a):
    if len(a) < 2:
        return a
    p = a[0]
    x, y = divide(p, a[1:])
    return quick_sort(x) + [p] + quick_sort(y)
