from cspConsistency import Con_solver, Search_with_AC_from_CSP
from cspProblem import CSP, Constraint        
from operator import lt,ne,eq,gt
from searchProblem import Arc, Search_problem
from searchGeneric import Searcher

# def ne_(val):
#     """not equal value"""
#     # nev = lambda x: x != val   # alternative definition
#     # nev = partial(neq,val)     # another alternative definition
#     def nev(x):
#         return val != x
#     nev.__name__ = str(val)+"!="      # name of the function 
#     return nev

# def is_(val):
#     """is a value"""
#     # isv = lambda x: x == val   # alternative definition
#     # isv = partial(eq,val)      # another alternative definition
#     def isv(x):
#         return val == x
#     isv.__name__ = str(val)+"=="
#     return isv

# C0 = Constraint(('A','B'),lt)
# C1 = Constraint(('B',),ne_(2))
# C2 = Constraint(('B','C'),lt)
# csp1 = CSP({'A':{1,2,3,4},'B':{1,2,3,4}, 'C':{1,2,3,4}},
#            [C0, C1, C2])

# q1
Con_solver.max_display_level = 4
LAKE_COORDS = (x_lake, y_lake) = (2,1)
CEM_COORDS = (x_cem, y_cem) = (0,0)
allow = {(x, y) for x in [0,1,2] for y in [0,1,2] if not ((x == x_cem and y == y_cem) or (x == x_lake and y == y_lake))}

def close(A, B):
    """close if share edge or corner"""
    (xA, yA) = A
    (xB, yB) = B
    return abs(xA - xB) <= 1 and abs(yA - yB) <= 1

def not_close(A, B):
    return not close(A, B)

A = 'house'
B = 'hotel'
C = 'rec'
D = 'garbage'
CEM = 'cem'
LAKE = 'lake'

# stuff not at each other
Ca = Constraint((A, B), ne)
Cb = Constraint((A, C), ne)
Cc = Constraint((A, D), ne)
Cd = Constraint((B, C), ne)
Ce = Constraint((B, D), ne)
Cf = Constraint((C, D), ne)

# house hotel not close cemetery
C0a = Constraint((A, CEM), not_close)
C0b = Constraint((B, CEM), not_close)

# rec close to lake
C1 = Constraint((C, LAKE), close)

# house hotel close rec
C2a = Constraint((A, C), close)
C2b = Constraint((B, C), close)

# house hotel not close garbage
C3a = Constraint((A, D), not_close)
C3b = Constraint((B, D), not_close)

# garbage not close lake
C4 = Constraint((D, LAKE), not_close)

lake_problem = CSP({A: allow, B: allow, C: allow, D: allow, CEM: {CEM_COORDS}, LAKE: {LAKE_COORDS}},
                [Ca, Cb, Cc, Cd, Ce, Cf, C0a, C0b, C1, C2a, C2b, C3a, C3b, C4])
# Con_solver(lake_problem).solve_one()
#searcher1d = Searcher(Search_with_AC_from_CSP(lake_problem))

# q2
dom = [1, 2, 3, 4]

fails = 0
expanded = 1 # for root node

print("\nSolutions:\nA B C D E F G H")
for A in dom:
    expanded += 1
    for B in dom:
        expanded += 1
        if True:
            for C in dom:
                expanded += 1
                if True:
                    for D in dom:
                        expanded += 1
                        if (D != C):
                            for E in dom:
                                expanded += 1
                                if (E != C) and (E < D - 1):
                                    for F in dom:
                                        expanded += 1
                                        if (abs(F - B) == 1) and (C != F) and (D != F) and (abs(E - F) % 2 == 1):
                                            for G in dom:
                                                expanded += 1
                                                if (A > G) and (abs(G - C) == 1) and (D > G) and (G != F):
                                                    for H in dom:
                                                        expanded += 1
                                                        if (A <= H) and (G < H) and ((H - C) % 2 == 0) and (H != D) and (E != H - 2) and (H != F):
                                                            print(A, B, C, D, E, F, G, H)
                                                        else:
                                                            fails += 1
                                                else:
                                                    fails += 1
                                        else:
                                            fails += 1
                                else:
                                    fails += 1
                        else:
                            fails += 1
                else:
                    fails +=1
        else:
            fails += 1
                
print("Search: number of failures:",fails)
print("Number of nodes expanded:",expanded)