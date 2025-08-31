def front_x(words):
    x_list = [w for w in words if w.startswith('x')]
    other_list = [w for w in words if not w.startswith('x')]
    return sorted(x_list) + sorted(other_list)
