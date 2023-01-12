def trouve(p, t):
    for x in t:
        if(p(x)): 
            return x