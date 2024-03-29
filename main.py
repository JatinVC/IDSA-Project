# IDSA-Project
import tkinter
from tkinter import *
from PIL import ImageTk,Image
from ComputerMode import *
import random

main = tkinter.Tk()
main.title("Sign-Reversal Puzzle")
main.geometry("700x700")
mframe = tkinter.Frame(main)
mframe.configure(bg="white")
mframe.pack()
submitButton = tkinter.Button(mframe, text='Enter', font='Arial', command=playerMove)

def cls():
    for buff in mframe.winfo_children():
        buff.destroy()

def play():
    cls()
    player = tkinter.Button(mframe, command=playerMode, text='Player Mode', font= "Arial")
    player.pack()
    computer = tkinter.Button(mframe, command=computerMode, text='Computer Mode', font= "Arial")
    computer.pack()
    back = tkinter.Button(mframe, command=window, text='Back', font= "Arial")
    back.pack()

def des():
    cls()
    lab = tkinter.Label(mframe, wraplength=300, justify=LEFT, text='This is an sign-reversal puzzle game. You need to change the signs of the numbers in different rows and columns.'
                                     'The main goal of this game is to form a sum of rows and columns which is non-negative', font="Bold")
    lab.pack()
    back = tkinter.Button(mframe, command=window, text='Back', font= "Arial")
    back.pack()

def how():
    cls()
    label1 = tkinter.Label(mframe, wraplength=300, justify=LEFT, text='There are 2 modes in this game 1) Player mode 2) Computer mode. In player mode you can manually change the '
                                        'signs of the numbers in different rows and columns. In Computer mode the computer will provide the user with the method to complete the game.', font="Bold")
    label1.pack()
    back = tkinter.Button(mframe, command=window, text='Back', font= "Arial")
    back.pack()

def playerMode():
    cls()
    labels = []

    for i in range(row+1):
        for j in range(col+1):
            labels.append(Label(mframe, text=matrix[i, j]).grid(column=j+5, row=i+5))

    commandEntry = tkinter.Entry(mframe, text="Type in your command here")
    commandEntry.grid(row=1, column=1, padx=5, pady=5)
    submitButton.grid()
    back = tkinter.Button(mframe, command=window, text='Back', font= "Arial")
    back.grid(row=2, column=1)

def computerMode():
        cls()

        for i in range(row+1):
            for j in range(col+1):
                labels.append(Label(mframe, text=matrix[i, j]).grid(column=j+5, row=i+5))

        commandEntry = tkinter.Entry(mframe, text="Type in your command here")
        commandEntry.grid(row=1, column=1, padx=5, pady=5)
        back = tkinter.Button(mframe, command=window, text='Back', font= "Arial")
        back.grid(row=2, column=1)
        hintField = tkinter.Text(mframe, width=30, height=2)
        hintField.grid()
        submitCommand = tkinter.Button(mframe, text='Enter', font="Arial")
        submitCommand.grid()
        hint=hints(matrix, row, col)
        showHint(hintField, hint)

def playerMove(entryField):
    command = entryField.get().split()
    if(command[0].lower() == "row"):
        choose(matrix, (command[1]-1), 0)
        updateSums(matrix, row, col)
        for label in labels:
            for i in range(row+1):
                for j in range(col+1):
                    label.config(text=matrix[i, j])

def showHint(hintField, hint):
    hintField.insert(tkinter.END, hint)

def window():
    cls()
    b1 = tkinter.Button(mframe, command=play, text='Play', font= "Arial")
    b1.pack()
    b2 = tkinter.Button(mframe, command=des, text='Description of the game', font= "Arial")
    b2.pack()
    b3 = tkinter.Button(mframe, command=how, text='How to play', font= "Arial")
    b3.pack()
    b4 = tkinter.Button(mframe, command=mframe.quit, text='Quit', font= "Arial")
    b4.pack()






canvas = Canvas(main, width=600, height=600)
image=ImageTk.PhotoImage(Image.open("pp.jpg"))
canvas.create_image(-20,-20,anchor=NW,image=image)
canvas.pack()
main.configure(bg="white")
row=random.randint(1, 10)
col = row
matrix = initArr(row, col)
labels = []
window()

main.mainloop()
