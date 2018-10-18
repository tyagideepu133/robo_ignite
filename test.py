#! /usr/bin/env python

with open('unit1_basicROS.tex', 'rb') as f,open('out.tex', 'w') as f2:
    for x in f:
	x = x.replace('\r','\\')
        if ('End of' not in x) and ('END' not in x):
            f2.write(x)

	
