def auto_hind(n, m):
    if m < 1:
        return n
    else:
        return auto_hind(round(n - (n * 0.2), 2), m - 1)