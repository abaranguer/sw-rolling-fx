#!/usr/bin/env python
# -*- coding: utf-8 -*-

w = 320                             # width
h = 240                             # height
c = 0                               # counter
size=(w,h)                          # size
filename = "./new-image-02.pbm"     # filename
bit = "0"

with open(filename, "w") as fd:
    fd.write("P1\n")
    fd.write("# CREATOR: Albert Baranguer Codina\n")
    fd.write("%d %d\n" % size)
    for y in range(0, 240):
        for x in range(0, 320):
            c = c + 1
            fd.write(bit)
            if bit == "1":
                bit = "0"
            else:
                bit = "1"
            if c == 70:
                fd.write("\n")
                c = 0
print "done!"
