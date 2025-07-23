
#A global lock ensures only one call occurs at a time.
#https://docs.python.org/3/library/tkinter.html   tkinter — Python interface to Tcl/Tk

import tkinter as tk    #
from tkinter import ttk  #
import glob  as glob 
import tcl as tcl
import os
from PIL import Image, ImageTk
from pathlib import Path
from tkinter import *
import glob, re
from tkinter import Tcl
from  tkinter import Image

#regex = glob.translate('**/*.png', recursive=True, include_hidden=True)   #txt

file=('skywalk.txt')


#root = tk.Tk() #

#style = ttk.Style(root)
#root.tk.call, file1=("source",  "forest-light.tcl")    #forest-light.tcl....VSCODE-OVERVIEW...._tkinter.TclError: no files matched glob pattern "*.png"
#root.tk.call, file2=("source",  "forest-dark.tcl")     #forest-dark.tcl....VSCODE-OVERVIEW....
#style.theme_use, file2=("source",  "forest-dark.tcl")
#file = img = tk.PhotoImage(file2 = "glob assets/logo.png")
#sorted(Path('.').glob('*.png'))



#frame = ttk.Frame(root)
#frame.pack()

#print(file= "skywalk.txt")

#root.mainloop()   #



#def skywalktxt():
    #file = open("skywalk.txt", "r")                     #file = open("Bank Data.txt", "r")
    #print("Current file")
    #print(file.read())
    #current = open("skywalk.txt", "r").read()
    #floatCurrent = float(current)
    #file.close()



#print('file.read'())


#print('skywalk.txt')

#f = open('skywalk.txt', 'r')

#file_contents = f.read()

#print (file_contents)

#f.close()

#with open("path/to/file") as f:
    #print f.read()


#with open("filename.txt", "w+") as file:
  #for line in file:
    #print line

#with open("skywalk.txt", "r", encoding="utf-8") as file:
    #for line in file:
        #print(line.strip())


#print(open('skywalk.txt', 'r').read()) 


#with open('skywalk.txt') as f_obj:
    #f_obj.readlines()


#Opening file
#f= open('skywalk.txt')
#reading everything in file
#r=f.read()
#reading at particular index
#r=f.read(1)
#print
#print(r)

#file= open("skywalker1.txt",  'r')
#content_of_file= file.read()
#print(content_of_file)

file= open('WVVBCheckLedger.txt', "r")
content_of_file= file.read()
print(content_of_file)

nums = list(range (1, 100))

def is_prime(n):
    if n <2:
        return False
    
    if n ==2:
        return True
    
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5)+1,2):
        if n % i == 0:
            return False
    return True

primes = filter(is_prime, nums)   #add list before filter
print(primes,"","[green] memory registration/Title[/green]")  

