#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

w = 320                                   # width
h = 240                                   # height
c = 0                                     # counter
size=(w,h)                                # size
filename_write = "./new-image-03-processed.pbm"     # filename
filename_read = "./new-image-03.pbm"
bit = ""
bits = []

def transform(x0, y0):
     a = 319.0
     b = 239.0  # y01
     d = 199.0
     e = 80.0   # y11
     c = a - d
     
     # y1 = e + (y0 * ((b - e) / b))
     c0 = (b - e) / (b * b)
     c1 = e
     y1 = (c0 * y0 * y0) + c1
     
     x2 = (((y1 * c) - (b * c)) / (e - b))
     x3 = a - x2
     x1 = x2 + (((x3 - x2) / a) *  x0)

     return (x1, y1)

if __name__ == "__main__":
    # prepare frame
    for y in xrange(0, 240):
        for x in range(0, 320):
            bits.append("0")

    # read and transform frame 
    with open(filename_read, "r") as fr:
        # discards three first header lines 
        fr.readline()
        fr.readline()
        fr.readline()
    
        for y in xrange(0, 240):
            yt_old = 0
            for x in xrange(0, 320):
                bit = fr.read(1)
                if bit == '\n':
                    bit = fr.read(1)

                # fill gaps
                for inc_y in xrange(0, 10):
                    (xt, yt) = transform(x, y + inc_y * 0.1)
                    #if int(yt) != yt_old:
                    #    yt_old = int(yt)
                    #    print ("y0=%d; xt=%d; yt=%d;") % (int(y), int(xt), int(yt))
                    if (int(yt) < 240) and (int(xt) < 320):
                        bits[int(xt) + int(yt) * 320] = bit

    # write frame
    with open(filename_write, "w") as fw:
        fw.write("P1\n")
        fw.write("# CREATOR: Albert Baranguer Codina\n")
        fw.write("%d %d\n" % size)
        for bit in bits:
            fw.write(bit)
            c = c + 1
            if (c == 70):
                c = 0
                fw.write('\n')
        
            
print "done!"
