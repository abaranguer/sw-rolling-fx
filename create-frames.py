#!/usr/bin/env python
# -*- coding: utf-8 -*-

def transform(x0, y0):
     a = 319.0
     b = 239.0
     d = 199.0
     e = 40.0
     c = a - d

     # lineal
     # y1 = e + (y0 * ((b - e) / b))
     
     # parabolic
     c0 = (b - e) / (b * b)
     c1 = e
     y1 = (c0 * y0 * y0) + c1


     x2 = (((y1 * c) - (b * c)) / (e - b))
     x3 = a - x2
     x1 = x2 + (((x3 - x2) / a) *  x0)

     return (x1, y1)

if __name__ == "__main__":
    w = 320                                   # width of a frame and base image
    h_frame = 240                             # height of a frame
    h_img_base = 800                          # height of base image
    c = 0                                     # counter
    frame_size=(w,h_frame)                    # size of frame
    filename_read = "intro.pbm"
    frames_folder = "./frames/"
    filename_master = "master"
    bit = ""
    
    # create movie master
    with open(filename_read, "r") as fr:    
        with open(frames_folder + filename_master, "w") as fm:
            # discards three first header lines
            fr.readline()
            fr.readline()
            fr.readline()

            for i in xrange(0, w * h_img_base):
                c = c + 1
                bit = fr.read(1)
                if bit == '\n':
                    bit = fr.read(1)
                fm.write(bit)
            
                if c == w:
                    fm.write('\n')
                    c = 0

    # create frames
    filename_frame = ""
    filename_pattern = "frame_%0#5d.pbm"
    filename_processed_pattern = "frame_%0#5d.processed.pbm"
    frame_count = 0

    with open(frames_folder + filename_master, "r") as fr:
        for frame_count in xrange(0, h_img_base - h_frame): 
            filename_frame = filename_pattern % frame_count
            print "[Frame %d]" % frame_count
        
            with open(frames_folder + filename_frame, "w") as fw:
                fw.write("P1\n")
                fw.write("# CREATOR: Albert Baranguer Codina\n")
                fw.write("%d %d\n" % frame_size)

                fr.seek(frame_count * (w + 1))

                for i in xrange(h_frame ):
                    fw.write(fr.readline())

    # create frame transform master
    num_steps = 2.0
    frame_transform = [["1" for j in xrange(0,int(num_steps))] for i in range(0, w * h_frame)]
    for y in xrange(0, h_frame):
        for x in xrange(0, w):
            for inc_y in xrange(0, int(num_steps)):
                frame_transform[x + y * w][inc_y] = transform(x, y + inc_y * (1 / num_steps) ) 
                    
    # create Processed frames    
    processed_frames_folder = "./processed-frames/"  
    filename_frame = ""
    filename_processed_frame = ""
    filename_pattern = "frame_%0#5d.pbm"
    filename_processed_pattern = "frame_%0#5d.processed.ppm"
    frame_count = 0

    for frame_count in xrange(0, h_img_base - h_frame): 
        filename_frame = filename_pattern % frame_count
        filename_processed_frame = filename_processed_pattern % frame_count
 
        # read and transform frame 
        with open(frames_folder + filename_frame, "r") as fr:
            # discards three first header lines 
            fr.readline()
            fr.readline()
            fr.readline()

            # initialize black frame
            frame_bits = ["1" for i in xrange(0, w * h_frame)]

            for y in xrange(0, h_frame):
                for x in xrange(0, w):
                    bit = fr.read(1)
                    if bit == '\n':
                        bit = fr.read(1)

                    # lineal
                    # (xt, yt) = transform(x, y)
                    # frame_bits[int(xt) + int(yt) * 320] = bit

                    # parabolic. trick for filling gaps
                    for inc_y in xrange(0, int(num_steps)):
                        (xt, yt) = frame_transform[x + y * w][inc_y]
                        if int(xt) < w and int(yt)< h_frame:
                            frame_bits[int(xt) + int(yt) * w] = bit
                    
        # write transformed frame
        # c = 0
        rgb = ""
        black = " 0 0 0"
        yellow = " 255 255 0"  
        print "[Processed Frame %0#5d]" % frame_count
        with open(processed_frames_folder + filename_processed_frame, "w") as fw:
            fw.write("P3\n")
            fw.write("# CREATOR: Albert Baranguer Codina\n")
            fw.write("%d %d 255\n" % frame_size)
            for bit in frame_bits:
                if bit == "1":
                    rgb = black
                else:
                    rgb = yellow 
                fw.write(rgb)
                c = c + 1
                if (c == w):
                    c = 0
                    fw.write('\n')
                
print "done!"
