d = {
    "ä": "a",
    "õ": "o",
    "ö": "o",
    "ü": "u",
}
first = input('Sisesta eesnimi: ').lower()
last = input('Sisesta perekonnanimi: ').lower()
name = f'{first}.{last}'
print(name.translate({ord(k): v for k, v in d.items()}))
