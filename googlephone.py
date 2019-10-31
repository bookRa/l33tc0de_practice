def google_phone(n, h):
    """
        n steps in a list of length h. How many possiblities when starting at i=0
    """
    poss = [[0 for x in range(h)] for y in range(n)]
    for row in range(0, n):
        for col in range(row+2):
            if row == 0:
                poss[row][col] = 1
            else:
                # looking at steps greater than 1
                left_lookup = 0 if col ==0 else poss[row-1][col-1] 
                right_lookup = 0 if col == h-1 else poss[row-1][col+1]
                same_lookup = poss[row-1][col]
                poss[row][col] = same_lookup + left_lookup + right_lookup
            if row == n-1:
                return poss[row][0]

ns = [3]
hs = [3]
for n,h in zip(ns, hs):
    print(f"{n=}, {h=}, {google_phone(n, h)}")