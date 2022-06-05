from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk
from Text_Summarizer import text_summerize
from textrank import generate_summary
from PIL import ImageTk, Image
import tkinter.font as font
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize, sent_tokenize
from nltk.collections import Counter
import tkinter.scrolledtext as scrolledtext

import os

win = Tk()
width= win.winfo_screenwidth()
w=width//2
height= win.winfo_screenheight()
#setting tkinter window size
win.geometry("%dx%d" % (width, height))
win.iconbitmap(r"C:\Users\ADMIN\OneDrive\Desktop\Text Summarizer/download.ico")
style = ttk.Style()
win.title("Text Summarization using Extraction Method")



string_summ = ''
show_text_val = 0
scroll = None
text_entry = None
frame2 = None
path_string = StringVar()
no_words = IntVar()
no_words.set('1')
summary = None
poswords = []
stop_words = []
token_sent = []

def open_file():
    global string_summ
    try:
        path = filedialog.askopenfile(title="Open File", filetypes=(("text files", '.txt'), ('all files', '*.*')),
                                      defaultextension=("text files", '.txt'), initialdir="C:/")
        path = path.name
        file2 = open(path)
        string_summ = file2.read()
        no_com.config(state='active')
        summ_btn.config(state='active')
        path_string.set(path)
        path_En.config(state='disabled')
        file = path_string.get()
        file = open(file, 'r')
        textgiven = file.read()
        inputtxt.delete("1.0","end")
        inputtxt.insert(1.0,textgiven)
        nof=0
        with open(path_string.get(),'r') as f:
            for line in f:
                w = line.split()
                nof+=len(w)
        inpwords_label.config(text = "No. of words given as input: {}".format(nof))
    except Exception as e:
        print(e)


def show_stop_words():
    global Output,frame2, scroll, text_entry, stop_words,value
    Output.config(state="normal")
    l2.config(text = "Stop Words")
    stop_words = list(stop_words)
    Output.delete("1.0","end")
    Output.insert("1.0","\n".join(stop_words))
    Output.config(state="disabled")
    #Output.destroy()
    #scroll.config(command=text_entry.yview)

def show_pos_words():
    global Output,frame2, scroll, text_entry, poswords,value
    Output.config(state="normal")
    l2.config(text = "Pos Tagged Words")
    
    Output.delete("1.0","end")
    Output.insert("1.0","\n".join(poswords))
    Output.config(state="disabled")
    #Output.destroy()
    #scroll.config(command=text_entry.yview)

def show_token_words():
    global frame2, scroll, text_entry, token_sent,value
    if frame2 and scroll and text_entry:
        frame2.destroy()
        scroll.destroy()
        text_entry.destroy()
    frame2 = Frame(bg="floral white")
    frame2.pack(pady=(10, 0))
    scroll = Scrollbar(frame2)
    scroll.pack(side="right", fill=Y)
    text_entry = Text(frame2, width="60", height="20", yscrollcommand=scroll.set, wrap='word')
    text_entry.pack()
    # file = open(os.path.dirname(path_string.get()) + '/output.txt', 'r')
    # token_sent = list(token_sent)
    # text = ''
    # for i in list(token_sent):
    #     text = i + '\n\n'
    inputtxt.insert(1.0,token_sent)
    text_entry.insert(1.0, token_sent)
    text_entry.config(state="disabled")
    scroll.config(command=text_entry.yview)


def summ_file():
    global Output,summary, stop_words, token_sent,value
    # file = open(path_string.get())
    Output.config(state="normal")
    l2.config(text = "Summarized Text")
    string_summ = inputtxt.get("1.0", "end-1c")
    #inputtxt.insert(1.0,string_summ)
    if(string_summ !=''):
        no_com.config(state='active')
        summ_btn.config(state='active')
       # path_En.config(state='disabled')
    summary, stop_words, token_sent = text_summerize(path_string.get(), no_words.get())
    Output.delete("1.0","end")
    Output.insert("1.0",summary)
    nof=len(summary.split())
    oupwords_label.config(text = "No. of words given as output: {}".format(nof))
    Output.config(state="disabled")
    hide_btn.config(state='active')
    
    #hide_btn1.config(state='active')
def text_rank():
    global Output,summary, stop_words, token_sent,value
    # file = open(path_string.get())
    Output.config(state="normal")
    l2.config(text = "Summarized Text")
    string_summ = inputtxt.get("1.0", "end-1c")
    #inputtxt.insert(1.0,string_summ)
    
    if(string_summ !=''):
        no_com.config(state='active')
        summ_btn.config(state='active')
       # path_En.config(state='disabled')
    summary, token_sent = generate_summary(path_string.get(), no_words.get())
    Output.delete("1.0","end")
    Output.insert("1.0",summary)
    nof=len(summary.split())
    oupwords_label.config(text = "No. of sentences given as output: {}".format(token_sent))
    Output.config(state="disabled")
    hide_btn.config(state='active')
def win_exit():
    boo = messagebox.askyesno("Exit", "Are you sure to exit")
    if boo:
        win.destroy()
#win.geometry("2000x720")
#win.resizable(True, True)
win.config(bg="floral white")
image1 = Image.open(r"C:\Users\ADMIN\OneDrive\Desktop\Text Summarizer/ball.jpg")
image1 = image1.resize((100, 100), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)
label1 = Label(image=test)
label1.image = test
label1.place(x=20, y=5)
lb = Label(win, text="  Text Summarization Using TF-IDF Approach                                        \n ", font=('Copperplate Gothic Bold', 24, 'bold'), bg='floral white', fg='navy blue')
lb2 = Label(win,text="\n  Text Summarizer will summarize the given text based on the retention rate provided by the user",font=('Helvetica',10),bg='floral white',fg='black')
lb.place(x=120,y=10)
lb2.place(x=150,y=50)
Font_tuple = ("Century Schoolbook",11)
l = Label(text = "Upload the document here.", font=('Helvetica', 14, 'bold'), bg='floral white', fg='navy blue')
inputtxt = scrolledtext.ScrolledText(win, height = 25,
                width = 85,wrap="word",
                bg = "light yellow",undo=True,highlightthickness = 2,highlightbackground='light yellow',highlightcolor='light green')
inputtxt.focus()
inputtxt.configure(font = Font_tuple)
inpwords_label = Label( text ="", font=('Helvetica', 10, 'bold'), bg='floral white', fg='navy blue')
inpwords_label.place(x=20,y=700)
l2 = Label(text = "", font=('Helvetica', 14, 'bold'), bg='floral white', fg='navy blue')
Output = scrolledtext.ScrolledText(win, height = 25, 
              width = 85,wrap="word", 
              bg = "light cyan",undo=True,highlightthickness = 2,highlightbackground='light cyan',highlightcolor='navy blue')
Output.config(state="disabled")
Output.focus()
oupwords_label = Label( text ="", font=('Helvetica', 14, 'bold'), bg='floral white', fg='navy blue')

l.place(x=20,y=160)
inputtxt.place(x=20,y=220)
l2.place(x=802,y=160)
Output.place(x=800,y=220)
Output.configure(font = Font_tuple)
oupwords_label = Label( text ="", font=('Helvetica', 10, 'bold'), bg='floral white', fg='navy blue')
oupwords_label.place(x=800,y=700)
##@@@
path_En = ttk.Entry(width="62", textvariable=path_string)
path_En.place(x=20,y=200)
path_btn = ttk.Button(text="Open File", command=open_file)
path_btn.place(x=400,y=197)



no_label = Label(win, text="Percentage of information to retain(in percent)",font=('Helvetica',10, 'bold'), bg='floral white')
no_label.place(x=25,y=120)
no_com = ttk.Entry(win, textvariable=no_words)
no_com.place(x=335,y=120)
myFont = font.Font(family='Helvetica',size=10)
summ_btn = Button(win, text="TF-IDF", command=summ_file,bg="skyblue1",activebackground='pale green1',font=myFont)
summ_btn.place(x=480,y=120)

summ_btn2 = Button(win, text="PageRank", command=text_rank,bg="skyblue1",activebackground='pale green1',font=myFont)
summ_btn2.place(x=580,y=120)

hide_btn = Button(win, text="Show Stop words", command=show_stop_words,state='disabled',bg="skyblue1",activebackground='pale green1',font=myFont)
hide_btn.place(x=680,y=120)

#hide_btn1 = Button(win, text="Show Pos Tagged words", command=show_pos_words,state='disabled',bg="skyblue1",activebackground='pale green1',font=myFont)
#hide_btn1.place(x=780,y=120)


win.protocol("WM_DELETE_WINDOW", win_exit)
win.mainloop()
