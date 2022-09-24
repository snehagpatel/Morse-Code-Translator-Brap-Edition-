#Import the required Libraries
from tkinter import *
from tkinter import ttk


# Python program to implement Morse Code Translator
# inp = 'Brap brap brap. Brap brap brapbrap. Brap brapbrap brap. Brap. Brap brapbrap brapbrap. Brap brap. Brap brap brap. Brap brap brap brap. Brap brap. Brap brap brap brap. Brap brapbrap. Brapbrap brap brap. Brap brapbrap. Brapbrap brap brapbrap brap. Brapbrap brap brapbrap brap. Brap. Brap brap brap. Brap brap brap. Brapbrap. Brapbrap brapbrap brapbrap. Brapbrap. Brap brap brap brap. Brap brap. Brap brap brap. brapbrap brap brapbrap brap. Brapbrap brapbrap brapbrap. Brapbrap brapbrap brapbrap. Brap brapbrap brap brap. Brap brapbrap brapbrap brap. Brap brapbrap brap. Brapbrap brapbrap brapbrap. Brapbrap brapbrap brap. Brap brapbrap brap. Brap brapbrap. Brapbrap brapbrap.'
# to_brap = False

# Dictionaries for translating
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ': ''}
MORSE_TO_ENG = {v: k for k, v in MORSE_CODE_DICT.items()}
MORSE_TO_BRAP= { '.':'brap', '-':'brapbrap', '/': '/'}
BRAP_TO_MORSE = {v: k for k, v in MORSE_TO_BRAP.items()}

def translate_to_brap(x):
    x = x.upper()
    x = x.replace(' ', '')
    output = ''
    for i in x:
        o = MORSE_CODE_DICT[i]
        b =''
        for dotdash in o:
            b = b + MORSE_TO_BRAP[dotdash] + ' '
        output = output + b + '. '

    output = output.replace(' . ', '. ')
    return output

def translate_from_brap(x):
    if (x[-1] is '.'):
        x = x[0:-1]
    x = x.lower()
    input_arr = x.split('.')
    out = ''
    for word in input_arr:
        word = word.lstrip()
        word_arr = word.split(' ')
        morse = ''
        for brap in word_arr:
            morse = morse + BRAP_TO_MORSE[brap]
        out = out + MORSE_TO_ENG[morse]
    return out

def translate(item, to):
    item = item.lstrip().rstrip()
    if (to):
        return translate_to_brap(item)
    else:
        return translate_from_brap(item)

#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x250")





#Initialize a Label to display the User Input
label=Label(win, text="", font=("Courier 12 bold"))
label.pack()

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()


 
toBrap = BooleanVar()
 
RBttn = Radiobutton(win, text = "English --> Brap", variable = toBrap,
                    value = True)
RBttn.pack(padx = 5, pady = 5)
 
RBttn2 = Radiobutton(win, text = "Brap --> English", variable = toBrap,
                     value = False)
RBttn2.pack(padx = 5, pady = 5)


def display_text():
   global entry
   string= translate(entry.get(), toBrap.get())
   print(string)
   label.configure(text=string)

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Translate",width= 20, command= display_text).pack(pady=20)


win.mainloop()
# print(translate(inp, to_brap))