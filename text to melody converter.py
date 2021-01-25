##!/usr/bin/env/ python3

#simple python script to convert text into melodies
#by Aaron Sabellek


import codecs
from time import sleep


#cclass to connect characters to frequencies
class Connect():
    #create reference frequencies (equal temperament)
    h = 246.942
    ais = b = 233.082
    a = 220
    gis = as_ = 207.652
    g = 195.998
    fis = ges = 184.997
    f = 174.614
    e = 164.814
    dis = es = 155.563
    d = 146.832
    cis = des = 138.591
    c = 130.813

    #connect characters to frequencies in dictionary
    #C = c/2, c1 = c*2, c2 = c*4..
    #connections for illustration in c minor
    connections = {
    "e": c/2,   #17.40% (relative frequency in german language)
    "n": c,     #9.78%
    "i": c*2,   #7.55%
    "s": c*4,   #7.27%
    "r": g/2,   #7.00%
    "a": g,     #6.51%
    "t": g*2,   #6.15%
    "d": g*4,   #5.08%
    "h": es/2,  #4.76%
    "u": es,    #4.35%
    "l": es*2,  #3.44%
    "c": es*4,  #3.06%
    "g": f/2,   #3.01%
    "m": f,     #2.53%
    "o": f*2,   #2.51%
    "b": f*4,   #1.89%
    "w": as_/2, #1.89%
    "f": as_,   #1.66%
    "k": as_*2, #1.21%
    "z": as_*4, #1.13%
    "p": d/2,   #0.79%
    "v": d,     #0.67%
    "ß": d*2,   #0.31%
    "j": d*4,   #0.27%
    "y": b/2,   #0.04%
    "x": b,     #0.03%
    "q": b*2    #0.02%
    }


#function to convert a text file into a list of frequencies
def convert(text_name):
    #create an object of Connect-class to connect characters to frequencies
    connect = Connect()
    
    #read text file and safe as string
    #for illustration converted to lowercase and without umlauts or breaks
    with codecs.open(text_name, "r", "utf-8") as text_file:
        text = text_file.read().lower().replace("\n", " ").replace("ö", "oe").replace("ä", "ae").replace("ü", "ue")

    #function to translate characters to frequencies
    def freq(char):
        if char in connect.connections:
            return connect.connections[char]
        else:
            return 0
    
    #convert characters to frequencies and safe in list
    freq_list = []
    for char in text:
        freq_list.append(freq(char))
        del char

    #return list of frequencies
    return freq_list


#function to play the converted melody
#adjust duration of single note in seconds
def play(freq_list, synth, duration):
    for frequency in freq_list:
        synth.freq = frequency
        sleep(duration)
    synth.freq = 0
