file_1_name = input('Sisesta sisend faili nimi: ')
file_2_name = input('Sisesta väljund faili nimi: ')
with open(file_1_name) as eng, open(file_2_name, 'w') as est:
    count = 0
    for line in eng.readlines():
        count += line.count('Hello')
        est.write(line.replace('Hello', 'Tere'))
print(count)