def kaprekar_step(L):
    asc = ''.join(str(d) for d in sorted(L))
    desc = ''.join(str(d) for d in sorted(L, reverse=True))
    
    small = int(asc)
    big = int(desc)
    
    return big - small
