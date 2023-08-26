# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 12:17:59 2021

@author: vikas
"""

from tkinter import *
import random
from tkinter import messagebox
from random import shuffle


answer=["turn", "tomato", "castist", "race", "ginger", "nayan", "potato", "salt"
        , "critics", "salt", "kohli", "rohit", "rabbit"]

word1=[]


for i in answer:
    word2=list(i)
    shuffle(word2)
    word1.append(word2)

num=random.randint(0,len(word1)-1) #select words from answer randomly
    
def initialize():
    global word1,num
    label1.configure(text=word1[num]) #providing words to label1 widget

counting=0

def checkans():
    global word1, answer, num, counting, msg2
    file1 = open('HighScore.txt', 'r')
    highScore = int(file1.read().strip())
    print(f'High Score : {highScore}')
    user_input=entry1.get()
    if(user_input==answer[num]):
        messagebox.showinfo("Success","Absolutely CORRECT")
        counting=counting+1
        msg2.config(text=str(counting))
        file1.close()
        print(counting)
        nextQuestion()
    else:
        messagebox.showinfo("Failure","INCORRECT")
        if (highScore < counting):
            file1.close()
            file1 = open('HighScore.txt', 'w')
            file1.write(str(counting))
            file1.close()
        else:
            file1.close()
        counting=0
        msg2.config(text=str(counting))
        entry1.delete(0,END)

        
def Reset():
    global word1,num,answer, counting, msg2
    file1 = open('HighScore.txt', 'r')
    highScore = int(file1.read().strip())
    if counting > highScore: 
        file1.close()
        file1 = open('HighScore.txt', 'w')
        file1.write(str(counting))
        msg2.config(text=0)
        counting = 0
        print('written in reset')
        file1.close()
    else:
        file1.close()
    msg2.config(text=str(counting))
    num=random.randint(0,len(word1)-1)
    label1.configure(text=word1[num])
    entry1.delete(0,END)

def nextQuestion():
    global word1,num,answer, counting, msg2
    num=random.randint(0,len(word1)-1)
    label1.configure(text=word1[num])
    entry1.delete(0,END)
   

top=Tk()

top.geometry("600x600")
listbox=Listbox(top)    

top.configure(background='sky blue')
top.title("Guess the Word !!!")
msg=Label(top,text="Welcome to Guess the Word Game!",bg='beige')
msg1=Label(top,text="So, Let's Begin...",bg="beige")

#
msg2=Label(top,text=counting,bg="red")
msg2.config(font=('Algerian',14,'bold'),foreground='green')
#

msg.config(font=('Algerian',20,'bold'),foreground='dark red')
msg1.config(font=('Algerian',14,'bold'),foreground='green')
msg.pack()
msg1.pack()

#
msg2.pack()
#

#top.geometry("600x600+350+50")
label1=Label(top,font=('Verdana',18,'bold'),foreground='dark blue',
             bg='light grey')
label1.pack(pady=30,ipady=10,ipadx=10)


#

#label2=Label(top,font=('Verdana',18,'bold'),foreground='dark blue',
#            bg='light grey')
#label2.pack(pady=30,ipady=40,ipadx=10)

#
answer1=StringVar()
entry1=Entry(top,textvariable=answer,font=(10))
entry1.pack(ipady=5,ipadx=5)

button1=Button(top,text="Check",width=20,command=checkans,
               foreground='dark green',font=('times 20',10,'bold'))
button1.pack(pady=30)


button2=Button(top,text="Reset",width=20,command=Reset,
               font=('times 20',10,'bold'))
button2.pack()

b_exit=Button(top,text='Exit',width=10,command=top.destroy,foreground='red') 
b_exit.pack(pady=30)

initialize()

listbox.pack()

top.mainloop()



