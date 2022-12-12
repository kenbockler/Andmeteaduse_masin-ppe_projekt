liinikaugus = int(input(print("Mis on elektriliini liinipikkus meetrites?")))
max_postide_kaugus = int(input(print("Mis on postidevaheline kaugus meetrites?")))
min_postide_arv_baasarv = int(round((int(liinikaugus)/int(max_postide_kaugus))))
min_postide_arv = int((int(min_postide_arv_baasarv) + 1))
min_postide_arv2 = int((int(min_postide_arv_baasarv) + 2))
min_postide_arv3 = 2
if int(liinikaugus) < int(max_postide_kaugus):
    print("Minimaalne postide arv valitud vahemikele on: " + str(min_postide_arv3))
elif int(liinikaugus) > (int(min_postide_arv_baasarv)*int(max_postide_kaugus)):
    print("Minimaalne postide arv valitud vahemikele on: " + str(min_postide_arv2))
else: print("Minimaalne postide arv valitud vahemikele on: " + str(min_postide_arv))