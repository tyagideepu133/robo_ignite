#!/usr/bin/env python

import fileinput
import sys

f = open(sys.argv[1],'rb')
filedata = f.read()
f.close()

# Replacement 
newdata = filedata.replace(".\n\n",".\\\\\n\\\\\n")
newdata = newdata.replace("?\n\n","?\\\\\n\\\\\n")
newdata = newdata.replace("!\n\n","!\\\\\n\\\\\n")
newdata = newdata.replace(":\n\n",":\\\\\n\\\\\n")

f = open(sys.argv[1],'w')
# f = open('pepe.tex','w')
f.write(newdata)
f.close()
