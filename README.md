# text-to-melody-converter
Simple Python module to convert text into melodies.

The module contains one class and two functions:

The class Connect() connects characters to certain frequencies in a dictionary. It has to be imported to let the function convert() work. It also contains reference frequencies (c-h) that can be used.

The function convert() reads text files (.txt), converts them into lists of frequencies and returns this lists. It's only argument takes the name of the chosen text file as a string (e.g. freqs = convert("text_file.txt")). This text file has to be in the same directory as the module.

The function play() plays the created melody with help of the pyo package (http://ajaxsoundstudio.com/pyodoc/). It takes three arguments: The list of frequencies, the sound and the duration of each tone in seconds. The list of frequencies should be a list you created with convert(). The sound should be created with pyo, for example a sine-wave, because play() is adjustet to pyo's syntax. The duration of each tone in seconds can be an integer or a float.

The module itself is called text_to_melody_converter.py. The file to illustrate the module interacting with the pyo package is called illustration_with_pyo.py. There is also a text example called text_example.txt, containing the four first lines of Goethe's peom "Erlkönig". This example is used in the illustration file.
