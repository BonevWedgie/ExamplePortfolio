def BinCart(U,V):
    return [(u,v) for u in U for v in V]

def BinConcat(L,M):
    return [(l + m) for l in L for m in M]

# BinCart more common operation for sets?

def cartProd(sets):
    result = {()}
    for s in sets:
        result = {acc + t for acc in result for t in s}
    return result
    