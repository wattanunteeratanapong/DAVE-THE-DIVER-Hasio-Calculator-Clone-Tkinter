import tkinter
from tkinter import *
from tkinter import ttk
import tkinter.font as font
from PIL import Image, ImageTk
from tkinter import Button, Label, Entry, CENTER, FLAT

root = Tk()
root.title("DAVE THE DIVER CALCULATOR")
root.geometry("580x980+665+135")
root.minsize(580, 980)
root.maxsize(580, 980)
root.configure(bg="#e7e7e7")

custom_font = font.Font(family='Snowstorm', size=12)
custom_font = font.Font(family='Snowstorm Light', size=12)

# Set image
# C
imagenormalc = Image.open("Button/Normal/c.png")
imageenterc = Image.open("Button/Enter/c.png")
imagepressedc = Image.open("Button/Pressed/c.png")
normalc = ImageTk.PhotoImage(imagenormalc)
enterc = ImageTk.PhotoImage(imageenterc)
pressedc = ImageTk.PhotoImage(imagepressedc)
# +/-
imagenormalplusminus = Image.open("Button/Normal/plusminus.png")
imageenterplusminus = Image.open("Button/Enter/plusminus.png")
imagepressedplusminus = Image.open("Button/Pressed/plusminus.png")
normalplusminus = ImageTk.PhotoImage(imagenormalplusminus)
enterplusminus = ImageTk.PhotoImage(imageenterplusminus)
pressedplusminus = ImageTk.PhotoImage(imagepressedplusminus)
# %
imagenormalpercent = Image.open("Button/Normal/percent.png")
imageenterpercent = Image.open("Button/Enter/percent.png")
imagepressedpercent = Image.open("Button/Pressed/percent.png")
normalpercent = ImageTk.PhotoImage(imagenormalpercent)
enterpercent = ImageTk.PhotoImage(imageenterpercent)
pressedpercent = ImageTk.PhotoImage(imagepressedpercent)
# ÷
imagenormaldivide = Image.open("Button/Normal/divide.png")
imageenterdivide = Image.open("Button/Enter/divide.png")
imagepresseddivide = Image.open("Button/Pressed/divide.png")
normaldivide = ImageTk.PhotoImage(imagenormaldivide)
enterdivide = ImageTk.PhotoImage(imageenterdivide)
presseddivide = ImageTk.PhotoImage(imagepresseddivide)
# 7
imagenormal7 = Image.open("Button/Normal/7.png")
imageenter7 = Image.open("Button/Enter/7.png")
imagepressed7 = Image.open("Button/Pressed/7.png")
normal7 = ImageTk.PhotoImage(imagenormal7)
enter7 = ImageTk.PhotoImage(imageenter7)
pressed7 = ImageTk.PhotoImage(imagepressed7)
# 8
imagenormal8 = Image.open("Button/Normal/8.png")
imageenter8 = Image.open("Button/Enter/8.png")
imagepressed8 = Image.open("Button/Pressed/8.png")
normal8 = ImageTk.PhotoImage(imagenormal8)
enter8 = ImageTk.PhotoImage(imageenter8)
pressed8 = ImageTk.PhotoImage(imagepressed8)
# 9
imagenormal9 = Image.open("Button/Normal/9.png")
imageenter9 = Image.open("Button/Enter/9.png")
imagepressed9 = Image.open("Button/Pressed/9.png")
normal9 = ImageTk.PhotoImage(imagenormal9)
enter9 = ImageTk.PhotoImage(imageenter9)
pressed9 = ImageTk.PhotoImage(imagepressed9)
# x
imagenormalmultiply = Image.open("Button/Normal/multiply.png")
imageentermultiply = Image.open("Button/Enter/multiply.png")
imagepressedmultiply = Image.open("Button/Pressed/multiply.png")
normalmultiply = ImageTk.PhotoImage(imagenormalmultiply)
entermultiply = ImageTk.PhotoImage(imageentermultiply)
pressedmultiply = ImageTk.PhotoImage(imagepressedmultiply)
# 4
imagenormal4 = Image.open("Button/Normal/4.png")
imageenter4 = Image.open("Button/Enter/4.png")
imagepressed4 = Image.open("Button/Pressed/4.png")
normal4 = ImageTk.PhotoImage(imagenormal4)
enter4 = ImageTk.PhotoImage(imageenter4)
pressed4 = ImageTk.PhotoImage(imagepressed4)
# 5
imagenormal5 = Image.open("Button/Normal/5.png")
imageenter5 = Image.open("Button/Enter/5.png")
imagepressed5 = Image.open("Button/Pressed/5.png")
normal5 = ImageTk.PhotoImage(imagenormal5)
enter5 = ImageTk.PhotoImage(imageenter5)
pressed5 = ImageTk.PhotoImage(imagepressed5)
# 6
imagenormal6 = Image.open("Button/Normal/6.png")
imageenter6 = Image.open("Button/Enter/6.png")
imagepressed6 = Image.open("Button/Pressed/6.png")
normal6 = ImageTk.PhotoImage(imagenormal6)
enter6 = ImageTk.PhotoImage(imageenter6)
pressed6 = ImageTk.PhotoImage(imagepressed6)
# -
imagenormalminus = Image.open("Button/Normal/minus.png")
imageenterminus = Image.open("Button/Enter/minus.png")
imagepressedminus = Image.open("Button/Pressed/minus.png")
normalminus = ImageTk.PhotoImage(imagenormalminus)
enterminus = ImageTk.PhotoImage(imageenterminus)
pressedminus = ImageTk.PhotoImage(imagepressedminus)
# 1
imagenormal1 = Image.open("Button/Normal/1.png")
imageenter1 = Image.open("Button/Enter/1.png")
imagepressed1 = Image.open("Button/Pressed/1.png")
normal1 = ImageTk.PhotoImage(imagenormal1)
enter1 = ImageTk.PhotoImage(imageenter1)
pressed1 = ImageTk.PhotoImage(imagepressed1)
# 2
imagenormal2 = Image.open("Button/Normal/2.png")
imageenter2 = Image.open("Button/Enter/2.png")
imagepressed2 = Image.open("Button/Pressed/2.png")
normal2 = ImageTk.PhotoImage(imagenormal2)
enter2 = ImageTk.PhotoImage(imageenter2)
pressed2 = ImageTk.PhotoImage(imagepressed2)
# 3
imagenormal3 = Image.open("Button/Normal/3.png")
imageenter3 = Image.open("Button/Enter/3.png")
imagepressed3 = Image.open("Button/Pressed/3.png")
normal3 = ImageTk.PhotoImage(imagenormal3)
enter3 = ImageTk.PhotoImage(imageenter3)
pressed3 = ImageTk.PhotoImage(imagepressed3)
# +
imagenormalplus = Image.open("Button/Normal/plus.png")
imageenterplus = Image.open("Button/Enter/plus.png")
imagepressedplus = Image.open("Button/Pressed/plus.png")
normalplus = ImageTk.PhotoImage(imagenormalplus)
enterplus = ImageTk.PhotoImage(imageenterplus)
pressedplus = ImageTk.PhotoImage(imagepressedplus)
# Del
imagenormaldelete = Image.open("Button/Normal/delete.png")
imageenterdelete = Image.open("Button/Enter/delete.png")
imagepresseddelete = Image.open("Button/Pressed/delete.png")
normaldelete = ImageTk.PhotoImage(imagenormaldelete)
enterdelete = ImageTk.PhotoImage(imageenterdelete)
presseddelete = ImageTk.PhotoImage(imagepresseddelete)
# 0
imagenormal0 = Image.open("Button/Normal/0.png")
imageenter0 = Image.open("Button/Enter/0.png")
imagepressed0 = Image.open("Button/Pressed/0.png")
normal0 = ImageTk.PhotoImage(imagenormal0)
enter0 = ImageTk.PhotoImage(imageenter0)
pressed0 = ImageTk.PhotoImage(imagepressed0)
# .
imagenormaldot = Image.open("Button/Normal/dot.png")
imageenterdot = Image.open("Button/Enter/dot.png")
imagepresseddot = Image.open("Button/Pressed/dot.png")
normaldot = ImageTk.PhotoImage(imagenormaldot)
enterdot = ImageTk.PhotoImage(imageenterdot)
presseddot = ImageTk.PhotoImage(imagepresseddot)
# =
imagenormalequal = Image.open("Button/Normal/equal.png")
imageenterequal = Image.open("Button/Enter/equal.png")
imagepressedequal = Image.open("Button/Pressed/equal.png")
normalequal = ImageTk.PhotoImage(imagenormalequal)
enterequal = ImageTk.PhotoImage(imageenterequal)
pressedequal = ImageTk.PhotoImage(imagepressedequal)
# Special
imageselect = Image.open("Button/Special/select.png")
photoselect = ImageTk.PhotoImage(imageselect)
imageclose = Image.open("Button/Special/close.png")
photoclose = ImageTk.PhotoImage(imageclose)



# Set display value
content = ""
txt_input = StringVar(value="0")

# Function
def btn(numbers):
    global content
    content = content + str(numbers)
    txt_input.set(content)

def equal():
    global content
    try:
        result = eval(content)
        if not isinstance(result, int):
            result = float(result)
        if len(str(result)) > 10:
            content = f"{result:.2e}"
        else:
            content = str(result)
    except Exception as e:
        content = "Error"
    txt_input.set(content)

def clear():
    global content
    content = ""
    txt_input.set("")
    display.insert(0,"0")

def plus():
    global content
    if "+" not in content:
        content = content + "+"
        txt_input.set(content)
    if "-" in content:
        content = content.replace("-", "")
        txt_input.set(content)
    if "*" in content:
        content = content.replace("*", "")
        txt_input.set(content)
    if "/" in content:
        content = content.replace("/", "")
        txt_input.set(content)

def minus():
    global content
    if "-" not in content:
        content = content + "-"
        txt_input.set(content)
    if "+" in content:
        content = content.replace("+", "")
        txt_input.set(content)
    if "*" in content:
        content = content.replace("*", "")
        txt_input.set(content)
    if "/" in content:
        content = content.replace("/", "")
        txt_input.set(content)

def multiply():
    global content
    if "*" not in content:
        content = content + "*"
        txt_input.set(content)
    if "+" in content:
        content = content.replace("+", "")
        txt_input.set(content)
    if "-" in content:
        content = content.replace("-", "")
        txt_input.set(content)
    if "/" in content:
        content = content.replace("/", "")
        txt_input.set(content)

def divide():
    global content
    if "/" not in content:
        content = content + "/"
        txt_input.set(content)
    if "+" in content:
        content = content.replace("+", "")
        txt_input.set(content)
    if "-" in content:
        content = content.replace("-", "")
        txt_input.set(content)
    if "*" in content:
        content = content.replace("*", "")
        txt_input.set(content)

def plusminus():
    global content
    if content[0] == "-":
        content = content[1:]
    else:
        content = "-" + content
    txt_input.set(content)

def percent():
    global content
    calculate = float(content) / 100
    content = str(calculate)
    txt_input.set(calculate)

def delete():
    global content
    content = content[:-1]
    txt_input.set(content)

def dot():
    global content
    if "." not in content:
        content = content + "."
        txt_input.set(content)

def select():
    global last_pressed
    if last_pressed is not None:
        last_pressed.invoke()

def close():
    root.destroy()



# Hasio
Label(root,text="HASIO",font=("Snowstorm",25),fg="#ada9a3",bg="#e7e7e7").place(x=28, y=20)

# Display
outer_frame = Frame(root, bg="#d5d5c6", bd=16, width=517, height=133)
outer_frame.place(x=32, y=82)

inner_frame = Frame(outer_frame, bg='#b1b4a2', bd=3)
inner_frame.place(x=0, y=0, width=485, height=102)

display = Entry(inner_frame, font=("Snowstorm",64), justify="right", bd=0, fg="#474f3d", bg="#b1b4a2", textvariable=txt_input, insertwidth=0)
display.place(x=0, y=0, width=470, height=100)

# Button
last_pressed = None

class CustomButton(Button):
    def __init__(self, master, photonormal, photoonenter, photocpressed, cnf={}, **kw):
        Button.__init__(self, master, image=photonormal, **cnf, **kw)
        self.photonormal = photonormal
        self.photoonenter = photoonenter
        self.photocpressed = photocpressed
        self.config(
            relief=FLAT,
            borderwidth=0,
            highlightthickness=0,
            activebackground=self.cget("background"),
            overrelief=FLAT
        )
        self.bind("<ButtonPress-1>", self.on_press)
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_press(self, event):
        global last_pressed
        if last_pressed is not None:
            last_pressed.config(image=last_pressed.photonormal)
        self.config(image=self.photocpressed)
        last_pressed = self

    def on_enter(self, event):
        if self is not last_pressed:
            self.config(image=self.photoonenter)

    def on_leave(self, event):
        if self is not last_pressed:
            self.config(image=self.photonormal)

class PlainButton(tkinter.Button):
    def __init__(self, master=None, command=None, fg=None, bg=None, **kwargs):
        super().__init__(master, command=command, fg=fg, bg=bg, **kwargs)
        self.config(
            relief=tkinter.FLAT,
            borderwidth=0,
            highlightthickness=0,
            activebackground=self.cget("background"),
            overrelief=tkinter.FLAT
        )

# row1
btnc = CustomButton(root, normalc, enterc, pressedc, command=clear, fg="#3b3838", bg="#e7e7e7")
btnc.place(x=50, y=268)
btnplusminus = CustomButton(root, normalplusminus, enterplusminus, pressedplusminus, command=plusminus,fg="#3b3838", bg="#e7e7e7")
btnplusminus.place(x=172, y=268)
btnpercent = CustomButton(root, normalpercent, enterpercent, pressedpercent, command=percent,fg="#3b3838", bg="#e7e7e7")
btnpercent.place(x=295, y=268)
btndivide = CustomButton(root, normaldivide, enterdivide, presseddivide, command=divide,fg="#3b3838", bg="#e7e7e7")
btndivide.place(x=417, y=268)

# row2
btn7 = CustomButton(root, normal7, enter7, pressed7, command=lambda:btn(7),fg="#3b3838", bg="#e7e7e7")
btn7.place(x=50, y=373)
btn8 = CustomButton(root, normal8, enter8, pressed8, command=lambda:btn(8),fg="#3b3838", bg="#e7e7e7")
btn8.place(x=172, y=373)
btn9 = CustomButton(root, normal9, enter9, pressed9, command=lambda:btn(9),fg="#3b3838", bg="#e7e7e7")
btn9.place(x=295, y=373)
btnmultiply = CustomButton(root, normalmultiply, entermultiply, pressedmultiply, command=multiply,fg="#3b3838", bg="#e7e7e7")
btnmultiply.place(x=417, y=373)

# row3
btn4 = CustomButton(root, normal4, enter4, pressed4, command=lambda:btn(4),fg="#3b3838", bg="#e7e7e7")
btn4.place(x=50, y=478)
btn5 = CustomButton(root, normal5, enter5, pressed5, command=lambda:btn(5),fg="#3b3838", bg="#e7e7e7")
btn5.place(x=172, y=478)
btn6 = CustomButton(root, normal6, enter6, pressed6, command=lambda:btn(6),fg="#3b3838", bg="#e7e7e7")
btn6.place(x=295, y=478)
btnminus = CustomButton(root, normalminus, enterminus, pressedminus, command=minus,fg="#3b3838", bg="#e7e7e7")
btnminus.place(x=417, y=478)

# row4
btn1 = CustomButton(root, normal1, enter1, pressed1, command=lambda:btn(1),fg="#3b3838", bg="#e7e7e7")
btn1.place(x=50, y=583)
btn2 = CustomButton(root, normal2, enter2, pressed2, command=lambda:btn(2),fg="#3b3838", bg="#e7e7e7")
btn2.place(x=172, y=583)
btn3 = CustomButton(root, normal3, enter3, pressed3, command=lambda:btn(3),fg="#3b3838", bg="#e7e7e7")
btn3.place(x=295, y=583)
btnplus = CustomButton(root, normalplus, enterplus, pressedplus, command=plus,fg="#3b3838", bg="#e7e7e7")
btnplus.place(x=417, y=583)

# row5
btndelete = CustomButton(root, normaldelete, enterdelete, presseddelete, command=delete,fg="#3b3838", bg="#e7e7e7")
btndelete.place(x=50, y=688)
btn0 = CustomButton(root, normal0, enter0, pressed0, command=lambda:btn(0),fg="#3b3838", bg="#e7e7e7")
btn0.place(x=172, y=688)
btndot = CustomButton(root, normaldot, enterdot, presseddot, command=dot,fg="#3b3838", bg="#e7e7e7")
btndot.place(x=295, y=688)
btnequal = CustomButton(root, normalequal, enterequal, pressedequal, command=equal,fg="#3b3838", bg="#e7e7e7")
btnequal.place(x=417, y=688)

# row6
btnselect = PlainButton(root, image=photoselect, command=select, fg="#3b3838", bg="#e7e7e7")
btnselect.place(x=108, y=845)
btnspace = PlainButton(root, image=photoclose, command=close, fg="#3b3838", bg="#e7e7e7")
btnspace.place(x=301, y=845)

root.mainloop()