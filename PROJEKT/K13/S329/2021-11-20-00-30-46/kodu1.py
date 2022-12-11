def auto_hind(m, n):
    if n == 0:
        return m
    else:
        return round(auto_hind(m, n - 1) * 80 / 100, 2)
