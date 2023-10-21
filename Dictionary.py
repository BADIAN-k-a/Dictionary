import json
from tkinter import *
from tkinter import ttk
import tkinter as tk

def translate_word():
    word = t.get("1.0", "end-1c")
    translation = "Can't translate"
    
    with open('top1000.json', encoding='utf-8') as file:
        data = json.load(file)
        
        for item in data:
            if item['english'] == word:
                translation = item['russian']
                break
    
    t1.delete("1.0", "end")
    t1.insert("1.0", translation)

def display_words():
    words = []
    with open('top1000.json', encoding='utf-8') as file:
        data = json.load(file)
        words = [item['english'] for item in data]
    
    combobox['values'] = words

root=Tk()   
root.geometry("700x500")   
root.title('Dictionary')   
root.resizable(width=False,height=False)   
root['bg']='#BF6470'   
##########################
# Создание фрейма для изображений и названия  
title_frame = Frame(root, bg='#890835')
title_frame.pack(anchor=N,fill=X)  

# Изображения  
image_left = PhotoImage(file="eng.png")  
image_right = PhotoImage(file="rus.png")  
  
# Уменьшение размеров изображений  
image_left = image_left.subsample(30, 30)  
image_right = image_right.subsample(30, 30)  
  
# Размещение изображений на фрейме  
label_left = Label(title_frame, image=image_left, bg='#890835')  
label_left.pack(side=LEFT)  
  
label_right = Label(title_frame, image=image_right, bg='#890835')  
label_right.pack(side=RIGHT)  
  
# Размещение фрейма с изображениями и названием  
label_title = Label(title_frame, text="Dictionary", font='Arial 16 bold', bg='#890835', fg='white')  
label_title.pack(side=TOP, fill=X)

# Размещение фрейма с изображениями и названием


# Название

        
###########################
label=Label(root,fg='white',bg='#BF6470',font='Arial 11 bold',text='Enter word')   
label.place(relx=0.5,rely=0.2,anchor=CENTER)   
t=Text(root,width=35,height=2,font='Arial 12 bold')   
t.place(relx=0.5,rely=0.3,anchor=CENTER)

btn=Button(root,width=40,text='Translate', command=translate_word)   
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

t1=Text(root,width=35,height=2,font='Arial 12 bold')   
t1.place(relx=0.5,rely=0.5,anchor=CENTER)

combobox = ttk.Combobox(root, width=10)
combobox.place(relx=0.8, y=140, anchor=CENTER)
combobox.bind("<<ComboboxSelected>>", lambda event: t.delete(1.0, "end") or t.insert("end", combobox.get()))
load_button = Button(root, text="Load Words", command=display_words)
load_button.place(relx=0.8, y=170, anchor=CENTER)

root.mainloop()