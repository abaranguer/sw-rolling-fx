#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

a = 319.0
b = 239.0  # y01
d = 199.0
e = 80.0   # y11
c = a - d

# y1 = e + (y0 * ((b - e) / b))
c0 = (b - e) / (b * b)
c1 = e

print ("c0=%f; c1=%f;") % (c0, c1)


for y0 in xrange(0, 240):
  # y1 = c0 * math.sqrt(y0)  + c1
  y1 = c0 * y0 * y0 + c1
  #x2 = (((y1 * c) - (b * c)) / (e - b))
  #x3 = a - x2
  #x1 = x2 + (((x3 - x2) / a) *  x0)
  print ("y0=%d; y1=%d") % (y0, int(y1))
