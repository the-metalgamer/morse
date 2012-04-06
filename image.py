#!/usr/bin/python2
# -*- coding: utf-8 -*-

import morse
import Image

def draw(string, file):

    if "." not in string or "-" not in string or "/" not in string or "//" not in string:
        string = morse.encode(string)
    
    words = string.split("//")

    i = []
    for word in words:
        letters = word.split("/")

        for letter in letters:
            charletter = list(letter)
            for x in charletter:
                if x == ".":
                    i.append(1)   
                elif x == "-":
                    i.append(1)
                    i.append(1)
                    i.append(1)
                else:
                    continue
                i.append(0)
            i.append(0)
            i.append(0)
        #draw.line((i,0,i+7,0), fill=0)
        i.append(0)
        i.append(0)
        i.append(0)
        i.append(0)

    while i[-1] == 0:
        i.pop()
    
    im = Image.new("1", (len(i),1))
    im.putdata(i)
    im.save(file, "PNG")

