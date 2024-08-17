from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES, Translator       
from gtts import gTTS      # to use TTS Engine
from playsound import playsound    # to play .mp3 file 
import os     # to delete .mp3

window = Tk()
window.geometry('800x500')
window.config(bg='#85929E')
window.title("Niks Translater")

def Translate():
    t1 = Translator()
    translated = t1.translate(text=input_text.get(1.0, END), src=s.get(), dest=s1.get())
    output_text.delete(1.0, END)
    output_text.insert(END, translated.text)

def Speak():
    translated_text = output_text.get(1.0, END).strip()
    if translated_text:
        try:
            lang_code = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(s1.get())]
            tts = gTTS(text=translated_text, lang=lang_code)
            audio_file = "translated_text.mp3"
            tts.save(audio_file)
            playsound(audio_file)
            os.remove(audio_file)  
        except Exception as e:
            #print(f"Error: {e}")
            print('Done!')
            
Label(window, text='Language Translater', font='arial 20 bold').place(x=260, y=20)
Label(window, text='Source Language : ').place(x=50, y=100)
Label(window, text='Result : ').place(x=430, y=100)

lang_list = list(LANGUAGES.values())

s = ttk.Combobox(window, values=lang_list)
s.set('Select Language')
s.place(x=160, y=100)

s1 = ttk.Combobox(window, values=lang_list)
s1.set('Select Language')
s1.place(x=490, y=100)

input_text = Text(window, height=8, width=40)
input_text.place(x=50, y=130)

output_text = Text(window, height=8, width=40)
output_text.place(x=430, y=130)

Button(window, text='Translate', command=Translate).place(x=320, y=300)
Button(window, text='Speak', command=Speak).place(x=420, y=300)

window.mainloop()

