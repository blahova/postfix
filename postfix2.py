#!/usr/bin/env python3
def eval_expr(s):
        s=s.split()
        z=[]    #zasobnik
        while(len(s) != 0):
                while(s[0].isdigit()):
                        z.append(int(s.pop(0)))
                if (s[0]=="+"):
                        z.append(z.pop(-2)+z.pop())
                elif (s[0]=="-"):
                        z.append(z.pop(-2)-z.pop())
                elif (s[0]=="*"):
                        z.append(z.pop(-2)*z.pop())
                elif (s[0]=="/"):
                        z.append(z.pop(-2)//z.pop())
                s.pop(0)
        return z[0]
