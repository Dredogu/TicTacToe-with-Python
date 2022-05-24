from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('300x400+660+140')
root.resizable(False, False)

def clear():
    global buttonVar, control, timer

    for j in range(9):
        buttons[j].config(text='', state=NORMAL, bg='white')
        chooseButtons[j] = j

    buttonVar, control, timer = 'X', True, 0
    showLabel.config(text='{} turn'.format(buttonVar))

def question():
    answer = messagebox.askyesno(title='?', message='Restart or Exit')

    if answer:
        clear()
    else:
        root.destroy()

def winner(a, b, c):
    showLabel.config(text='Winner {}'.format(buttonVar))
    buttons[a].config(bg='green')
    buttons[b].config(bg='green')
    buttons[c].config(bg='green')
    
    question()


def change():
    global buttonVar, control
    
    if control:
        buttonVar = 'O'
        control = False
    else:
        buttonVar = 'X'
        control = True

    showLabel.config(text='{} turn'.format(buttonVar))


def check():
    global timer
    
    timer += 1
    
    if chooseButtons[0] == buttonVar and chooseButtons[1] == buttonVar and chooseButtons[2] == buttonVar:
        winner(0, 1, 2)
    elif chooseButtons[3] == buttonVar and chooseButtons[4] == buttonVar and chooseButtons[5] == buttonVar:
        winner(3, 4, 5)
    elif chooseButtons[6] == buttonVar and chooseButtons[7] == buttonVar and chooseButtons[8] == buttonVar:
        winner(6, 7, 8)
    elif chooseButtons[0] == buttonVar and chooseButtons[3] == buttonVar and chooseButtons[6] == buttonVar:
        winner(0, 3, 6)
    elif chooseButtons[1] == buttonVar and chooseButtons[4] == buttonVar and chooseButtons[7] == buttonVar:
        winner(1, 4, 7)
    elif chooseButtons[2] == buttonVar and chooseButtons[5] == buttonVar and chooseButtons[8] == buttonVar:
        winner(2, 5, 8)
    elif chooseButtons[0] == buttonVar and chooseButtons[4] == buttonVar and chooseButtons[8] == buttonVar:
        winner(0, 4, 8)
    elif chooseButtons[2] == buttonVar and chooseButtons[4] == buttonVar and chooseButtons[6] == buttonVar:
        winner(2, 4, 6)
    elif timer == 9:
        showLabel.config(text='Draw')
        question()
    else:
        change()


def show(index):
    buttons[index].config(text=buttonVar, state=DISABLED)
    chooseButtons[index] = buttonVar
    check()

def addButton(index):
    button = Button(root, command=lambda: show(index), bg='white', font='JetBrains 30')
    button.place(x=xEx, y=yEx, width=100, height=100)
    buttons.append(button)
    chooseButtons.append(index)

control = True
buttonVar = 'X'
buttons, chooseButtons = [], []
xEx, yEx = 0, 100
timer = 0

showLabel = Label(root, text='{} turn'.format(buttonVar), font='JetBrains 50', fg='green', bg='black')
showLabel.place(x=0, y=0, width=300, height=100)

for i in range(1, 10):
    addButton(i-1)
    xEx += 100
    if not i % 3:
        yEx += 100
        xEx = 0

root.mainloop()
