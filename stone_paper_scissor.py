from tkinter import *
import random

root = Tk()
root.title("Stone Paper Scissor")
root.geometry("630x400")

num = 1

def random_computer_choice():
    # global e_opp
    e_opp.delete(0, END)
    opp = random.choice(["Stone", "Paper", "Scissor"])
    e_opp.insert(0, opp)
    return opp

def stone():    
    e_you.delete(0, END)
    e_you.insert(0, 'Stone')
    random_computer_choice()
    chs = e_opp.get()
    if chs == "Scissor":
        e_stat.delete(0, END)
        e_stat.insert(0, "You Won !!!")
        # for i in range(0, num): 
        a = your_score.get()
        your_score.delete(0, END)
        your_score.insert(0, int(a) + int(num))
        
    elif chs == "Paper":
        e_stat.delete(0, END)
        e_stat.insert(0, "You Lose !!!")
        # opp_score.insert(0, num + 1)
        b = opp_score.get()
        opp_score.delete(0, END)
        opp_score.insert(0, int(b) + int(num))
    
    else:
        e_stat.delete(0, END)
        e_stat.insert(0, "It's a Tie !!!")
    
def paper():
    e_you.delete(0, END)
    e_you.insert(0, "Paper")
    random_computer_choice()
    chs1 = e_opp.get()
    if chs1 == "Stone":
        e_stat.delete(0, END)
        e_stat.insert(0, "You Won !!!")
        # your_score.insert(0, num + 1)
        a = your_score.get()
        your_score.delete(0, END)
        your_score.insert(0, int(a) + int(num))

    elif chs1 == "Scissor":
        e_stat.delete(0, END)
        e_stat.insert(0, "You Lose !!!")
        # opp_score.insert(0, num + 1)
        b = opp_score.get()
        opp_score.delete(0, END)
        opp_score.insert(0, int(b) + int(num))

    else:
        e_stat.delete(0, END)
        e_stat.insert(0, "It's a Tie !!!")

def scissor():
    e_you.delete(0, END)
    e_you.insert(0, "Scissor")
    random_computer_choice()
    chs1 = e_opp.get()
    if chs1 == "Paper":
        e_stat.delete(0, END)
        e_stat.insert(0, "You Won !!!")
        # your_score.insert(0, num + 1)
        a = your_score.get()
        your_score.delete(0, END)
        your_score.insert(0, int(a) + int(num))

    elif chs1 == "Stone":
        e_stat.delete(0, END)
        e_stat.insert(0, "You Lose !!!")
        # opp_score.insert(0, num + 1)
        b = opp_score.get()
        opp_score.delete(0, END)
        opp_score.insert(0, int(b) + int(num))

    else:
        e_stat.delete(0, END)
        e_stat.insert(0, "It's a Tie !!!")

btnstone = Button(root, text = "Stone", height=5, width=20, bg = "black", fg = "red", command=stone)
btnstone.grid(row = 1, column = 1, padx = 20, pady = 40, columnspan = 1)

btnpaper = Button(root, text = "Paper", height=5, width=20, bg = "#999966", fg = "#00ffff", command=paper)
btnpaper.grid(row = 1, column = 2, padx = 20, pady = 40, columnspan = 1)

btnscissor = Button(root, text = "Scissor", height=5, width=20, bg = "red", fg = "black", command=scissor)
btnscissor.grid(row = 1, column = 3, padx = 20, pady = 40, columnspan = 1)

e_stat = Label(root, text = "Status  :")
e_stat.grid(row = 2, column = 1, pady = 10)

e_stat = Entry(root, width = 40)
e_stat.grid(row = 2, column = 2)

e_you = Label(root, text="Your Choice  :")
e_you.grid(row = 3, column = 1, pady = 10)

e_you = Entry(root, width = 40)
e_you.grid(row = 3, column = 2)

e_opp = Label(root, text="Opponent's Choice  :")
e_opp.grid(row = 4, column = 1, pady = 10)

e_opp = Entry(root, width = 40)
e_opp.grid(row = 4, column = 2)

your_score = Label(root, text=" Your Score  :")
your_score.grid(row = 5, column = 1, pady = 10)

your_score = Entry(root, width = 40)
your_score.insert(0,0)
your_score.grid(row = 5, column = 2)

opp_score = Label(root, text=" Opponent's Score  :")
opp_score.grid(row = 6, column = 1, pady = 10)

opp_score = Entry(root, width = 40)
opp_score.insert(0,0)
opp_score.grid(row = 6, column = 2)


root.mainloop()