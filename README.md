# text-to-melody-converter
Simple Python module to convert text into melodies.

The module contains one class and two functions.

The Connect-class connects characters to certain frequencies. It has to be imported, to let the convert-function work (from text_to_melody_converter import Connect). It also contains reference frequencies (c-h) that can be used.

The convert-function reads text files (.txt), converts them into lists of frequencies and returns this list. It's only argument takes the name of the chosen text file as a string (e.g. freqs = convert("text_file.txt")). This text file has to be in the same directory as the module.

The play-function plays the created melody with help of the pyo package (http://ajaxsoundstudio.com/pyodoc/). It takes three arguments: The list of frequencies, the synth and the duration of each tone in seconds. The list of frequencies should be a list you created with the convert-function. The synth should be a sound created with pyo, for example a sine-wave. The duration of each tone in seconds can be an integer or a float.

The module itself is called text_to_melody_conver.py. The file to illustrate the module interacting with the pyo package is called illustration_with_pyo.py. There is also a text example called text_example.txt, containing the four first lines of Goethes peom "Erlkönig". This example is used in the illustration file.
