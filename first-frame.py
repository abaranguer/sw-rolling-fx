#!/usr/bin/env python
# -*- coding: utf-8 -*-

# read first frame

w = 320                                   # width
h = 240                                   # height
c = 0                                     # counter
size=(w,h)                                # size
filename_write = "./new-image-03.pbm"     # filename
filename_read = "text2.pbm"
bit = ""

with open(filename_read, "r") as fr:    
    with open(filename_write, "w") as fw:
        # discards three first header lines
        fr.readline()
        fr.readline()
        fr.readline()

        fw.write("P1\n")
        fw.write("# CREATOR: Albert Baranguer Codina\n")
        fw.write("%d %d\n" % size)
        for x in range(0, 240 * 320):
            bit = fr.read(1)
            if bit == '\n':
                fw.write(bit)
                bit = fr.read(1)
            fw.write(bit)
            
print "done!"
