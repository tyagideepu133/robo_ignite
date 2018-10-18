#! /usr/bin/env python

import sys

with open(sys.argv[1]) as f,open('out.tex', 'w') as f2:
    for x in f:
        if ('End of' not in x) and ('END OF' not in x) and ('END' not in x):
            f2.write(x)
