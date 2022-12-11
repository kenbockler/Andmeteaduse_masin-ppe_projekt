def transponeeriK(maatriks):
    return [list(rida) for rida in zip(*maatriks[::-1])][::-1]