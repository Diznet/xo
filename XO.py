from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title("Tic Tac Toe")

pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)
player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

bclick = True
flag = 0

def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)
    button10.configure(state=DISABLED)
    button11.configure(state=DISABLED)
    button12.configure(state=DISABLED)
    button13.configure(state=DISABLED)
    button14.configure(state=DISABLED)
    button15.configure(state=DISABLED)
    button16.configure(state=DISABLED)
    button17.configure(state=DISABLED)
    button18.configure(state=DISABLED)
    button19.configure(state=DISABLED)
    button20.configure(state=DISABLED)
    button21.configure(state=DISABLED)
    button22.configure(state=DISABLED)
    button23.configure(state=DISABLED)
    button24.configure(state=DISABLED)
    button25.configure(state=DISABLED)



def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, playerb, pa
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        playerb = "Congratulations " + p2.get() + "!"
        pa = "Congratulations " + p1.get() + "!"
        checkForWin()
        flag += 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe","Button already Clicked!")

def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button2['text'] == 'X' and button3['text'] == 'X' and button4['text'] == 'X' or
        button3['text'] =='X' and button4['text'] == 'X' and button5['text'] == 'X' or
        button6['text'] == 'X' and button7['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button8['text'] == 'X' and button9['text'] == 'X' and button10['text'] == 'X' or
        button11['text'] == 'X' and button12['text'] == 'X' and button13['text'] == 'X' or
        button12['text'] == 'X' and button13['text'] == 'X' and button14['text'] == 'X' or
        button13['text'] == 'X' and button14['text'] == 'X' and button15['text'] == 'X' or
        button16['text'] == 'X' and button17['text'] == 'X' and button18['text'] == 'X' or
        button17['text'] == 'X' and button18['text'] == 'X' and button19['text'] == 'X' or
        button18['text'] == 'X' and button19['text'] == 'X' and button20['text'] == 'X' or
        button21['text'] == 'X' and button22['text'] == 'X' and button23['text'] == 'X' or
        button22['text'] == 'X' and button23['text'] == 'X' and button24['text'] == 'X' or
        button23['text'] == 'X' and button24['text'] == 'X' and button25['text'] == 'X' or
        button1['text'] == 'X' and button7['text'] == 'X' and button13['text'] == 'X' or
        button2['text'] == 'X' and button8['text'] == 'X' and button14['text'] == 'X' or
        button3['text'] == 'X' and button9['text'] == 'X' and button15['text'] == 'X' or
        button6['text'] == 'X' and button12['text'] == 'X' and button18['text'] == 'X' or
        button7['text'] == 'X' and button13['text'] == 'X' and button19['text'] == 'X' or
        button8['text'] == 'X' and button14['text'] == 'X' and button20['text'] == 'X' or
        button11['text'] == 'X' and button17['text'] == 'X' and button23['text'] == 'X' or
        button12['text'] == 'X' and button18['text'] == 'X' and button24['text'] == 'X' or
        button13['text'] == 'X' and button19['text'] == 'X' and button25['text'] == 'X' or
        button5['text'] == 'X' and button9['text'] == 'X' and button13['text'] == 'X' or
        button4['text'] == 'X' and button8['text'] == 'X' and button12['text'] == 'X' or
        button3['text'] == 'X' and button7['text'] == 'X' and button11['text'] == 'X' or
        button10['text'] == 'X' and button14['text'] == 'X' and button18['text'] == 'X' or
        button9['text'] == 'X' and button13['text'] == 'X' and button17['text'] == 'X' or
        button8['text'] == 'X' and button12['text'] == 'X' and button16['text'] == 'X' or
        button15['text'] == 'X' and button19['text'] == 'X' and button23['text'] == 'X' or
        button14['text'] == 'X' and button18['text'] == 'X' and button22['text'] == 'X' or
        button13['text'] == 'X' and button17['text'] == 'X' and button21['text'] == 'X' or
        button1['text'] == 'X' and button6['text'] == 'X' and button11['text'] == 'X' or
        button6['text'] == 'X' and button11['text'] == 'X' and button16['text'] == 'X' or
        button11['text'] == 'X' and button16['text'] == 'X' and button21['text'] == 'X' or
        button2['text'] == 'X' and button7['text'] == 'X' and button12['text'] == 'X' or
        button7['text'] == 'X' and button12['text'] == 'X' and button17['text'] == 'X' or
        button12['text'] == 'X' and button17['text'] == 'X' and button22['text'] == 'X' or
        button3['text'] == 'X' and button8['text'] == 'X' and button13['text'] == 'X' or
        button8['text'] == 'X' and button13['text'] == 'X' and button18['text'] == 'X' or
        button13['text'] == 'X' and button18['text'] == 'X' and button23['text'] == 'X' or
        button4['text'] == 'X' and button9['text'] == 'X' and button14['text'] == 'X' or
        button9['text'] == 'X' and button14['text'] == 'X' and button19['text'] == 'X' or
        button14['text'] == 'X' and button19['text'] == 'X' and button24['text'] == 'X' or
        button5['text'] == 'X' and button10['text'] == 'X' and button15['text'] == 'X' or
        button10['text'] == 'X' and button15['text'] == 'X' and button20['text'] == 'X' or
        button15['text'] == 'X' and button20['text'] == 'X' and button25['text'] == 'X' ):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

    elif(flag == 24):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "DRAW")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
           button2['text'] == 'O' and button3['text'] == 'O' and button4['text'] == 'O' or
           button3['text'] =='O' and button4['text'] == 'O' and button5['text'] == 'O' or
           button6['text'] == 'O' and button7['text'] == 'O' and button8['text'] == 'O' or
           button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
           button8['text'] == 'O' and button9['text'] == 'O' and button10['text'] == 'O' or
           button11['text'] == 'O' and button12['text'] == 'O' and button13['text'] == 'O' or
           button12['text'] == 'O' and button13['text'] == 'O' and button14['text'] == 'O' or
           button13['text'] == 'O' and button14['text'] == 'O' and button15['text'] == 'O' or
           button16['text'] == 'O' and button17['text'] == 'O' and button18['text'] == 'O' or
           button17['text'] == 'O' and button18['text'] == 'O' and button19['text'] == 'O' or
           button18['text'] == 'O' and button19['text'] == 'O' and button20['text'] == 'O' or
           button21['text'] == 'O' and button22['text'] == 'O' and button23['text'] == 'O' or
           button22['text'] == 'O' and button23['text'] == 'O' and button24['text'] == 'O' or
           button23['text'] == 'O' and button24['text'] == 'O' and button25['text'] == 'O' or
           button1['text'] == 'O' and button7['text'] == 'O' and button13['text'] == 'O' or
           button2['text'] == 'O' and button8['text'] == 'O' and button14['text'] == 'O' or
           button3['text'] == 'O' and button9['text'] == 'O' and button15['text'] == 'O' or
           button6['text'] == 'O' and button12['text'] == 'O' and button18['text'] == 'O' or
           button7['text'] == 'O' and button13['text'] == 'O' and button19['text'] == 'O' or
           button8['text'] == 'O' and button14['text'] == 'O' and button20['text'] == 'O' or
           button11['text'] == 'O' and button17['text'] == 'O' and button23['text'] == 'O' or
           button12['text'] == 'O' and button18['text'] == 'O' and button24['text'] == 'O' or
           button13['text'] == 'O' and button19['text'] == 'O' and button25['text'] == 'O' or
           button5['text'] == 'O' and button9['text'] == 'O' and button13['text'] == 'O' or
           button4['text'] == 'O' and button8['text'] == 'O' and button12['text'] == 'O' or
           button3['text'] == 'O' and button7['text'] == 'O' and button11['text'] == 'O' or
           button10['text'] == 'O' and button14['text'] == 'O' and button18['text'] == 'O' or
           button9['text'] == 'O' and button13['text'] == 'O' and button17['text'] == 'O' or
           button8['text'] == 'O' and button12['text'] == 'O' and button16['text'] == 'O' or
           button15['text'] == 'O' and button19['text'] == 'O' and button23['text'] == 'O' or
           button14['text'] == 'O' and button18['text'] == 'O' and button22['text'] == 'O' or
           button13['text'] == 'O' and button17['text'] == 'O' and button21['text'] == 'O' or
           button1['text'] == 'O' and button6['text'] == 'O' and button11['text'] == 'O' or
           button6['text'] == 'O' and button11['text'] == 'O' and button16['text'] == 'O' or
           button11['text'] == 'O' and button16['text'] == 'O' and button21['text'] == 'O' or
           button2['text'] == 'O' and button7['text'] == 'O' and button12['text'] == 'O' or
           button7['text'] == 'O' and button12['text'] == 'O' and button17['text'] == 'O' or
           button12['text'] == 'O' and button17['text'] == 'O' and button22['text'] == 'O' or
           button3['text'] == 'O' and button8['text'] == 'O' and button13['text'] == 'O' or
           button8['text'] == 'O' and button13['text'] == 'O' and button18['text'] == 'O' or
           button13['text'] == 'O' and button18['text'] == 'O' and button23['text'] == 'O' or
           button4['text'] == 'O' and button9['text'] == 'O' and button14['text'] == 'O' or
           button9['text'] == 'O' and button14['text'] == 'O' and button19['text'] == 'O' or
           button14['text'] == 'O' and button19['text'] == 'O' and button24['text'] == 'O' or
           button5['text'] == 'O' and button10['text'] == 'O' and button15['text'] == 'O' or
           button10['text'] == 'O' and button15['text'] == 'O' and button20['text'] == 'O' or
           button15['text'] == 'O' and button20['text'] == 'O' and button25['text'] == 'O'):
                disableButton()
                tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)


buttons = StringVar()

label = Label(tk, text="Player 1:", font='Times 20 bold', bg='white', fg='black', height=1, width=6)
label.grid(row=1, column=0)
label = Label(tk, text="Player 2:", font='Times 20 bold', bg='white', fg='black', height=1, width=6)
label.grid(row=2, column=0)

button1 = Button(tk, text=" ", font='Times 20 bold', bg='gray', fg='white',height=3, width=6, command=lambda: btnClick(button1))
button1.grid(row=3, column=0)
button2 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=3, width=6, command=lambda: btnClick(button2))
button2.grid(row=3, column=1)
button3 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=3, width=6,command=lambda: btnClick(button3))
button3.grid(row=3, column=2)
button4 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=3, width=6, command=lambda: btnClick(button4))
button4.grid(row=3, column=3)
button5 = Button(tk, text=' ',font='Times 20 bold', bg='gray', fg='white', height=3, width=6, command=lambda: btnClick(button5))
button5.grid(row=3, column=4)


button6 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=3, width=6,command=lambda: btnClick(button6))
button6.grid(row=4, column=0)
button7 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=3, width=6, command=lambda: btnClick(button7))
button7.grid(row=4, column=1)
button8 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white',height=3, width=6, command=lambda: btnClick(button8))
button8.grid(row=4, column=2)
button9 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=3, width=6, command=lambda: btnClick(button9))
button9.grid(row=4, column=3)
button10 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=3, width=6, command=lambda: btnClick(button10))
button10.grid(row=4, column=4)


button11 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=3, width=6, command=lambda: btnClick(button11))
button11.grid(row=5, column=0)
button12 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=3, width=6, command=lambda: btnClick(button12))
button12.grid(row=5, column=1)
button13 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=3, width=6, command=lambda: btnClick(button13))
button13.grid(row=5, column=2)
button14 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=3, width=6, command=lambda: btnClick(button14))
button14.grid(row=5, column=3)
button15 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=3, width=6, command=lambda: btnClick(button15))
button15.grid(row=5, column=4)


button16 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white',height=3, width=6, command=lambda: btnClick(button16))
button16.grid(row=6, column=0)
button17 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white',height=3, width=6, command=lambda: btnClick(button17))
button17.grid(row=6, column=1)
button18 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=3, width=6, command=lambda: btnClick(button18))
button18.grid(row=6, column=2)
button19 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white',height=3, width=6, command=lambda: btnClick(button19))
button19.grid(row=6, column=3)
button20 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white',height=3, width=6, command=lambda: btnClick(button20))
button20.grid(row=6, column=4)


button21 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=3, width=6, command=lambda: btnClick(button21))
button21.grid(row=7, column=0)
button22 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=3, width=6, command=lambda: btnClick(button22))
button22.grid(row=7, column=1)
button23 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white', height=3, width=6, command=lambda: btnClick(button23))
button23.grid(row=7, column=2)
button24 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white',height=3, width=6, command=lambda: btnClick(button24))
button24.grid(row=7, column=3)
button25 = Button(tk, text=' ', font='Times 20 bold', bg='gray', fg='white',height=3, width=6, command=lambda: btnClick(button25))
button25.grid(row=7, column=4)

tk.mainloop()
