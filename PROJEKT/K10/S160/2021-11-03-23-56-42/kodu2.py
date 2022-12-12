tripstrapstrull = {"O" : 0, "X" : 0}
def võitja(maatriks):
    for i in maatriks:
        if i.count('O') == 3 :
            tripstrapstrull['O'] += 1
        if i.count('O') == 4:
            tripstrapstrull['O'] += 2
        if i.count('X') == 3 :
            tripstrapstrull['X'] += 1
        if i.count('X') == 4:
            tripstrapstrull['X'] += 2
    return tripstrapstrull
võitja([['X','X','X',' '],[' ','O',' ',' '],[' ',' ','O',' '],[' ',' ',' ','O']])