failinimi = 'sõiduplaan.txt'
with open(failinimi) as fail:
    for rida in fail:
        rida = rida.split('\n')
        print(rida[0])