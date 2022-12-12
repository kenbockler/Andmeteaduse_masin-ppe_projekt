def create_username(first_name : str, second_name : str):
    return '{}.{}'.format(first_name.lower(), second_name.lower()).replace('ä','a').replace('ö','o').replace('õ','o').replace('ü','u')
f_name = input('Sisesta eesnimi: ')
l_name = input('Sisesta perenimi: ')
print(create_username(f_name, l_name))
