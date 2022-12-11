with open(input('Vali sisend'), 'r') as f:
    tekst = f.readlines()
hello_count = 0
with open(input('Vali väljund'), 'w') as f:
    for i in tekst:
        hello_count += i.count('Hello')
        i = i.replace('Hello', 'Tere')
        f.write(i)
print(f'Tehti {hello_count} asendamist.')