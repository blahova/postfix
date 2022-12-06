#!/usr/bin/env python3
def eval_expr(s):
    s=s.split()
    z=[]    #zasobnik
    while(len(s) != 0):
        while(s[0].isdigit()):
            z.append(s.pop(0))
        if (s[0]=="/"):
            z.append(str(eval(z.pop(0)+s.pop(0)*2+z.pop(0))))
        else:
            z.append(str(eval(z.pop(0)+s.pop(0)+z.pop(0))))
    return int(z[0])

