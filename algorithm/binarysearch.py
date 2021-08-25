def show(tree):
    if len(tree) == 0:
        return ''
    left, data, right = tree
    return '(' + show(left) + str(data) + show(right) + ')'

def insert(tree, n):
    if len(tree) == 0:
        return ((), n, ())
    left, data, right = tree
    if n == data:
        return tree
    if n < data:
        return (insert(left, n), data, right)
    return (left, data, insert(right, n))

def search(tree, n):
    if len(tree) == 0:
        return False
    left, data, right = tree
    if n == data:
        return True
    if n < data:
        return search(left, n)
    return search(right, n)

def remove(tree, n):
    if len(tree) == 0:
        return ()
    left, data, right = tree
    if n == data:
        if len(left) == 0:
            return right
        if len(right) == 0:
            return left
        minimum, removed_right = remove_min(right)
        return (left, minimum, removed_right)

    if n < data:
        return (remove(left, n), data, right)
    return (left, data, remove(right, n))

def remove_min(tree):
    left, data, right = tree
    if len(left) == 0:
        return (data, right)
    minimum, removed_right = remove_min(left)
    return (minimum, (removed_right, data, right))
