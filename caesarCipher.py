# Caesar Cipher in GUI
# Write : 28/06/2021
#--------------------------------------------#
from tkinter import *
from tkinter import ttk
import pyperclip
# Setting Basic GUI
GUI = Tk()
GUI.geometry('500x500')
GUI.title('Caesar Cipher')
message = StringVar()
result = StringVar()
# Function encrypt caesar cipher
def EncryptDecrypt_Caesar():
    msg = str(message.get())
    key = 13   # Setting key
    mode = 'encrypt'   # Set to either 'encrypt' or 'decrypt'
    character = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?.'
    translation = ''
    for symbol in msg:
        if symbol in character:
            symbol_index = character.find(symbol)
            # Perform encrypt/decrypt
            if mode == 'encrypt':   # Select encrypt mode
                translationIndex = symbol_index + key
            elif mode == 'decrypt':   # Select decrypt mode
                translationIndex = symbol_index - key
            # Handle wraparound
            if translationIndex >= len(character):
                translationIndex -= len(character)
            elif translationIndex < 0:
                translationIndex += len(character)

            translation += character[translationIndex]
        else:
            translation += symbol
    # Output in show text
    resultText = ("Translate : %s" % (translation))
    result.set(resultText)
    pyperclip.copy(translation)

# Setting title in GUI
title = Label(GUI, text='Caesar Cipher Encryption', font=(None, 18, 'bold'))
title.pack(padx=10, pady=10)
# Textbox
textbox = ttk.Entry(GUI, textvariable=message)
textbox.pack(padx=10, pady=10)
#call function enter/Push button
button = ttk.Button(GUI, text='Enter', command=EncryptDecrypt_Caesar) # command = Function name
button.pack(padx=10, pady=10, ipadx=10, ipady=10)
# Show results
result_GUI = Label(GUI, textvariable=result, font=('bold', 18))
result_GUI.pack(padx=10, pady=10)

GUI.mainloop()
