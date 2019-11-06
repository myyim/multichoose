import numpy as np

def multichoose(n,k):
    """multichoose(n,k) computes n multichoose k and returns the list of all possible combinations."""
    import itertools
    z = itertools.combinations_with_replacement(range(n),k)
    y = list(z)
    output = []
    print str(n)+' multichoose '+str(k)+' = '+str(len(y))
    for j in range(len(y)):
        count = []
        for k in range(n):
            count.append(np.sum(np.array(y[j])==k))
        output.append(count)
    return output
