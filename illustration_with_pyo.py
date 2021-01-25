##!/usr/bin/env/ python3

#illustration of interacting with pyo (http://ajaxsoundstudio.com/pyodoc/)
#by Aaron Sabellek


from text_to_melody_converter import Connect, convert, play
from pyo import *


#create object of Connect-class to connect characters to frequencies
connect = Connect()


#convert text file to melody and safe melody in variable
melody = convert("text_example.txt")


#start pyo server
s = Server().boot()
s.start()


#create or upload sounds using pyo (http://ajaxsoundstudio.com/pyodoc/)
#saw- and sine-waves for illustration
#take freqs from Connect-class
bg_synth_1 = SuperSaw(freq=connect.c/2, mul=0.1).out() #saw-wave for background (left)
bg_synth_2 = SuperSaw(freq=connect.c, mul=0.1).out(1) #saw-wave for background (right)

main_synth = Sine(freq=0, mul=0.1) #sine-wave

del_synth_1 = Delay(main_synth, delay=[0.1, 0.04], feedback=0.6).out() #delayed sine-wave for main sound (left)
del_synth_2 = Delay(main_synth, delay=[0.1, 0.06], feedback=0.6).out(1) #delayed sine-wave for main sound (right)

time.sleep(2) #play bg_synths for two seconds without main_synth


#play converted melody on main synth
play(melody, main_synth, 0.5)

time.sleep(2) #play bg_synths for two seconds without main_synth


#stop pyo server
s.stop()
