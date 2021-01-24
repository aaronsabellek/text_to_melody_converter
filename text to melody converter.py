##!/usr/bin/env/ python3

#simple python script to convert text into melodies
#by Aaron Sabellek


import codecs
from pyo import *
from time import sleep


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


#connect characters to frequencies
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


#function for translating characters to frequencies
def freq(char):
    if char in connections:
        return connections[char]
    else:
        return 0


#read text file and save as string
#text for illustration converted to lowercase only and without umlauts and breaks
with codecs.open("text_example.txt", "r", "utf-8") as text_file:
    text = text_file.read().lower().replace("\n", " ").replace("ö", "oe").replace("ä", "ae").replace("ü", "ue")


#convert string into list of frequencies
freq_list = []
for char in text:
    freq_list.append(freq(char))
    del char


#start pyo server
s = Server().boot()
s.start()
    

#create or upload sounds using pyo (http://ajaxsoundstudio.com/pyodoc/)
#saw- and sine-waves for illustration
bg_synth_1 = SuperSaw(freq=c/2, mul=0.1).out() #saw-wave for background (left)
bg_synth_2 = SuperSaw(freq=c, mul=0.1).out(1) #saw-wave for background (right)

main_synth = Sine(freq=0, mul=0.1) #sine-wave

del_synth_1 = Delay(main_synth, delay=[0.1, 0.04], feedback=0.6).out() #delayed sine-wave for main sound (left)
del_synth_2 = Delay(main_synth, delay=[0.1, 0.06], feedback=0.6).out(1) #delayed sine-wave for main sound (right)

sleep(2) #play background synth for two seconds before melody starts


#play melody
#adjust sleep(x) to manipulate duration of single note in seconds
for frequency in freq_list:
    main_synth.freq = frequency
    sleep(0.8)

main_synth.freq = 0
sleep(2) #play background synth for two seconds after melody already ended

    
#stop pyo server
s.stop()
