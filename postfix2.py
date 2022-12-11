#!/usr/bin/env python3
def eval_expr(s):
        s=s.split()
	z=[]	#zasobnik
	while(len(s) != 0):
		if (s[0]=="+"):
			z.append(z.pop(-2)+z.pop())
		elif (s[0]=="-"):
			z.append(z.pop(-2)-z.pop())
		elif (s[0]=="*"):
			z.append(z.pop(-2)*z.pop())
		elif (s[0]=="/"):
			z.append(z.pop(-2)//z.pop())
		else:
			z.append(int(s[0]))
                s.pop(0)
	return z[0]
