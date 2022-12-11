'''-- Kodutöö nr. 14 - 1. Rekursiivne absoluutväärtus --'''
def rek_abs(järjend):
    abs_järjend = []
    if järjend:
        for el in järjend:
            if not isinstance(el, list):
                abs_järjend.append(abs(el))
            else:
                abs_järjend.append(rek_abs(el))
    return abs_järjend
print(rek_abs([2, -6, [8, -12, -12, [4, [-6], -3]], 7, [3.55, -3.55]]))
print([2, 6, [8, 12, 12, [4, [6], 3]], 7, [3.55, 3.55]])