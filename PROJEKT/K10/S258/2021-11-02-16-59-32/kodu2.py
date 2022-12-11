def võitja(mat):
    BBW={}
    eh={'O': 0, 'X': 0}
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            BBW[(i,j)]=mat[i][j]
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            el=mat[i][j]
            try:
                if el == BBW[(i-1,j)] and el == BBW[(i+1,j)]:
                    eh[el]+=1
            except: pass
            try:
                if el == BBW[(i,j-1)] and el == BBW[(i,j+1)]:
                    eh[el]+=1
            except: pass
            try:
                if el == BBW[(i+1,j+1)] and el == BBW[(i-1,j-1)]:
                    eh[el]+=1
            except: pass
            try:
                if el == BBW[(i-1,j+1)] and el == BBW[(i+1,j-1)]:
                    eh[el]+=1
            except: pass
    return eh