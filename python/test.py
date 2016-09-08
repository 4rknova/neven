#!/usr/bin/env python2

import pyneven
import os
import Image, ImageDraw

srcdir = "images"
outdir = "out"
outfor = "png"
reccol = "red"
linwgt = 5

def export(src, dst, faces, weight=linwgt):
    if not os.path.exists(outdir):
        os.makedirs(outdir)
    im = Image.open(src)
    draw = ImageDraw.Draw(im)
    for face in faces:
        ax = face.midpointx - face.eyedist;
        ay = face.midpointy - face.eyedist;
        bx = face.midpointx + face.eyedist;
        by = face.midpointy + face.eyedist;
        for i in range (0, weight):
            draw.rectangle(((ax-i,ay-i),(bx+i,by+i)),outline = reccol)
    del draw
    im.save(dst, outfor.upper())

def process(filename):
    faces = pyneven.detect_faces_from_filename(filename)
    print filename + " " + str(len(faces))
    outfile = outdir + os.path.sep +  os.path.basename(filename)
    (prefix, sep, suffix) = outfile.rpartition('.')
    outfile = prefix + os.path.extsep + outfor
    export(filename, outfile, faces)

def main():
    for f in os.listdir(srcdir):
        process(srcdir + os.path.sep + f);

if __name__ == "__main__":
    main()
