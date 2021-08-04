import tkinter as tk
from tkinter import *
from textblob import TextBlob
'''
If you want to modify this Project then message me on my Instagram !
1. @CoderMohit
2. @Itz_Mohit.Goyal
'''


CODERMOHIT = tk.Tk()
CODERMOHIT.title("Spell Checker By Coder Mohit")
CODERMOHIT.geometry('500x400')

def website():
    import webbrowser
    url = 'https://codermohit.com'
    webbrowser.open(url)


def youtube():
    import webbrowser
    url = 'https://www.youtube.com/channel/UCaqKx5W0cSS0l2i2GgKQw9g?sub_confirmation=1'
    webbrowser.open(url)


def Output():
    inp = inputtxt.get(1.0, "end-1c")
    b = TextBlob(inp)

    lbl.config(text="Output: " + str(b.correct()))


lbl_name = Label(CODERMOHIT, text='Enter Text Here: ', width=20, fg='white', font=('Helvetica', 15, 'bold'))
lbl_name.config(bg="#f56d40")
lbl_name.pack()

# TextBox Creation
inputtxt = tk.Text(CODERMOHIT, height=6, width=40)

inputtxt.pack()

# Button Creation
printButton = tk.Button(CODERMOHIT, text="Check Now!", width=10, fg='white', bg='green', font=('Helvetica', 12, 'bold'),
                        command=Output)
printButton.pack()

# Label Creation
lbl = tk.Label(CODERMOHIT, text='Output__________' + '', width=100, fg='white', font=('Helvetica', 15, 'bold'))
lbl.config(bg="#eb4034")
lbl.pack()


Website_Button = Button(CODERMOHIT, text="Website", font=('Courier', 15, 'bold'), command=website, fg='white', bg='#fb2056',
                        width=13).pack(side=LEFT)
youtube_Button = Button(CODERMOHIT, text="YouTube", font=('Courier', 15, 'bold'), command=youtube, fg='white', bg='#c4302b',
                        width=13).pack(side=LEFT)
Exit_Button = Button(CODERMOHIT, text="Exit", font=('Courier', 15, 'bold',), command=exit, fg='white', bg='#8B0000',
                     width=13).pack(side=LEFT)

CODERMOHIT.mainloop()
