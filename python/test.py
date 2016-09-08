#!/usr/bin/env python2

# Add your images in the ./images/directory

import pyneven
import os

def process(filename):
	faces = pyneven.detect_faces_from_filename(filename);
	print filename + " " + str(len(faces))

def main():
    for f in os.listdir("images"):
        process('images/' + f);

if __name__ == "__main__":
    main()
