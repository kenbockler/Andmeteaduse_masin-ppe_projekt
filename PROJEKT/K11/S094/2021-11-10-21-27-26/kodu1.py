def seosta_lapsed_ja_vanemad(lapsed_fail, nimed_fail):
     isikukoodid = {}
     with open(lapsed_fail) as isikukoodifail, open(nimed_fail) as nimedefail:
         for rida_andmed in nimedefail:
             rida_andmed_eraldatud = rida_andmed.split(' ', 1)
             rida_andmed_puhas = []
             for el in rida_andmed_eraldatud:
                 print(el)
seosta_lapsed_ja_vanemad("lapsed.txt", "nimed.txt")