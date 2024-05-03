import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import Voice
import EqConverter
import Matplot

root = tk.Tk()
root.title('PY VOICE GRAPH')
root.geometry('1000x650')
root.resizable(False, False)

c = tk.Canvas(root, height=650, width=1000)
c.pack()

# Welcome Screen

img1 = ImageTk.PhotoImage(file=r'E:\Projects\FOCP\PyGraph\Project pics\Welcome.png')
c.create_image(0, 0, image=img1, anchor='nw', tag='del')

# 2nd screen
light_true = 0


def theme(num):
    global light_true
    light_true = num
    setting_page()
    if num == 0:
        light['state'] = ACTIVE
        dark['state'] = DISABLED

    else:
        dark['state'] = ACTIVE
        light['state'] = DISABLED

img2 = [None, None]
back_img = [None, None]
setting_pag = [None, None]
rec_screen = [None, None]
c3img = [None,None]

img2[0] = ImageTk.PhotoImage(file=r'E:\Projects\FOCP\PyGraph\Project pics\Sec screen.png')
img2[1] = ImageTk.PhotoImage(file=r'E:\Projects\FOCP\PyGraph\Project pics\SSC light.png')
setting_i = Image.open(r'E:\Projects\FOCP\PyGraph\Project pics\Settings.png')
setting_i = setting_i.resize((110, 110), Image.ANTIALIAS)
setting_img = ImageTk.PhotoImage(setting_i)

back_img[1] = ImageTk.PhotoImage(file=r'E:\Projects\FOCP\PyGraph\Project pics\Back.png')
back_img[0] = ImageTk.PhotoImage(file=r'E:\Projects\FOCP\PyGraph\Project pics\Backdark.png')
rec_i = Image.open(r'E:\Projects\FOCP\PyGraph\Project pics\mic.png').resize((140, 120), Image.ANTIALIAS)
rec_img = ImageTk.PhotoImage(rec_i)

setting_pag[0] = ImageTk.PhotoImage(file=r'E:\Projects\FOCP\PyGraph\Project pics\Settings page.png')
setting_pag[1] = ImageTk.PhotoImage(file=r'E:\Projects\FOCP\PyGraph\Project pics\Settings light.png')

rec_screen[0] = ImageTk.PhotoImage(file=r'E:\Projects\FOCP\PyGraph\Project pics\Record Screen.png')
rec_screen[1] = ImageTk.PhotoImage(file=r'E:\Projects\FOCP\PyGraph\Project pics\Record Light Screen.png')

last_img = ImageTk.PhotoImage(file=r'E:\Projects\FOCP\PyGraph\Project pics\SSC light.png')
c3img[0] = ImageTk.PhotoImage(file = r'E:\Projects\FOCP\PyGraph\Project pics\Last Image.png')
c3img[1] = ImageTk.PhotoImage(file = r'E:\Projects\FOCP\PyGraph\Project pics\Last Image Light.png')


# GRID
def grid(choice2, choice):
    for i in range(63):
        c.create_line(i * 5, 0, i * 5, 310, width=1, fill='black', tag='grid')
        c.create_line(0, i * 5, 310, i * 5, width=1, fill='black', tag='grid')
        c.create_line(155, 155, 310, 0, width=4, fill=choice2, tag='grid')
        c.create_line(2, 2, 155, 155, width=4, fill=choice2, tag='grid')

        if i * 5 == 155:
            c.create_line(i * 5, 0, i * 5, 310, width=3, fill=choice, tag='grid')
            c.create_line(0, i * 5, 310, i * 5, width=3, fill=choice, tag='grid')
    c.move('grid', 605, 215)


# Dropdown Menu
def drop(comm):
    color_list = ['aquamarine', 'red', 'green', 'blue', 'maroon']
    global variable
    global dropdown
    variable = StringVar()
    variable.set(color_list[4])
    dropdown = tk.OptionMenu(root, variable, *color_list, command=comm)
    choice = variable.get()
    dropdown.config(
        height=1, width=10,
        fg='black', font='TimesNewRoman 14',
        activeforeground='white',
        activebackground='dark grey')
    return dropdown


def second_sc():
    c.create_image(0, 0, image=img2[light_true], anchor='nw')
    record = tk.Button(image=rec_img, height=65, width=65, bd=1,
                       highlightcolor='blue', relief='flat', command=record_page)
    c.create_image(500, 300, anchor='center', image=rec_img)
    c.create_window(500, 300, anchor='center', window=record, tag='wind')
    c.create_image(500, 550, anchor='center', image=setting_img)
    settings = tk.Button(image=setting_img, height=70, width=70, bd=1, relief='flat', command=setting_page)
    c.create_window(500, 550, anchor='center', window=settings, tag='wind')
    c.delete('back')
    c2.destroy()
    frame.destroy()


def change_graph_color(choice2):
    print(choice2)
    global new2
    new2 = choice2
    grid(choice=new, choice2=new2)
    return new2


def change_grid_color(choice):
    print(choice)
    global new
    new = choice
    grid(choice=new, choice2=new2)
    return new


def male_voice():
    global ind
    ind = 0
    Voice.male_female(ind)
    female['state'] = ACTIVE
    male['state'] = DISABLED
    female.config(relief='raised', bg='white', fg='black')
    male.config(relief='flat', bg='dark gray', fg='white')


def female_voice():
    ind = 2
    Voice.male_female(ind)
    female['state'] = DISABLED
    male['state'] = ACTIVE
    male.config(relief='raised', bg='white', fg='black')
    female.config(relief='flat', bg='dark gray', fg='white')


def setting_page():
    c.create_image(0, 0, image=setting_pag[light_true], anchor='nw')

    back = tk.Button(image=back_img[light_true], height=40, width=90, bd=4, relief='raised', command=second_sc)
    c.create_window(80, 80, anchor='nw', window=back, tag='back')

    global male
    male = tk.Button(text='MALE', bg='white', font='TimesNewRoman 12', bd=3, height=1, width=8, command=male_voice)
    c.create_window(355, 245, window=male, anchor='nw', tag='back')

    global female
    female = tk.Button(text='FEMALE', bg='white', font='TimesNewRoman 12', bd=3, height=1, width=8,
                       command=female_voice)
    c.create_window(430, 245, window=female, anchor='nw', tag='back')

    global dark
    dark = tk.Button(text='DARK', font='TimesNewRoman 12',
                     height=1, width=8, bg='black', fg='white',
                     bd=3, command=lambda: theme(0))
    c.create_window(355, 320, window=dark, anchor='nw', tag='back')

    global light
    light = tk.Button(text='LIGHT', fg='black', font='TimesNewRoman 12',
                      bg='white', height=1, bd=3,
                      width=8, command=lambda: theme(1))
    c.create_window(430, 320, window=light, anchor='nw', tag='back')

    a = drop(change_grid_color)
    c.create_window(355, 390, window=a, anchor='nw', tag='back')

    b = drop(change_graph_color)
    c.create_window(355, 470, window=b, anchor='nw', tag='back')

    c.delete('wind')
    c2.destroy()
    frame.destroy()


def record_page():
    c.delete('wind')
    c.create_image(0, 0, image=rec_screen[light_true], anchor='nw')

    listen = ['#3FEED6', '#695F1A']
    back = tk.Button(image=back_img[light_true], height=40, width=90, bd=4, relief='raised', command=second_sc)
    c.create_window(80, 80, anchor='nw', window=back, tag='back')

    c.create_text(500, 200,text='Listening...', fill = listen[light_true], font='Brokenbrush 30',tag='listen')
    def take():
        yes = tk.Button(text='PROCEED', font='TimesNewRoman 18', height=1, width=8, command=last_page)
        c.create_window(390, 500, window=yes, anchor='nw', tag='back')

        no = tk.Button(text='AGAIN', font='TimesNewRoman 18', height=1, width=8, command=record_page)
        c.create_window(510, 500, window=no, anchor='nw', tag='back')

        global eq
        eq = EqConverter.converter(Voice.takecommand(c))

        c.delete('listen')
        c.create_text(500, 400, text='y = '+eq, fil=listen[light_true], font='Brokenbrush 30')
        c.after(300,Voice.proceed)

    c.after(100,take)
    c2.destroy()
    frame.destroy()


def last_page():
    c.delete('back')

    global frame
    frame = tk.Frame(c, height=650, width=300)
    frame.pack(side=tk.LEFT)

    global c3
    c3 = tk.Canvas(frame, bg='white', height=650, width=300)
    c3.pack()

    c3.create_image(0, 0, image=c3img[light_true], anchor='nw')
    back = tk.Button(image=back_img[light_true], height=40, width=90, bd=4, relief='raised', command=second_sc)
    c3.create_window(45, 40, anchor='nw', window=back, tag='back')

    c3.create_image(150, 400, anchor='center', image=rec_img)
    record = tk.Button(image=rec_img, height=65, width=65, bd=1,
                       highlightcolor='blue', relief='flat', command=record_page)
    c3.create_window(150, 400, anchor='center', window=record, tag='wind')


    c3.create_image(150, 550, anchor='center', image=setting_img)
    settings = tk.Button(image=setting_img, height=70, width=70, bd=1, relief='flat', command=setting_page)
    c3.create_window(150, 550, anchor='center', window=settings, tag='wind')

    global fc
    fc=['white','black']
    c3.create_text(110, 235, text='y = '+eq, font = 'Brokenbrush 19',anchor ='center' ,fill=fc[light_true])

    global c2
    c2 = tk.Canvas(c, height=650, width=700)
    c2.pack()
    Matplot.matplotter(c2, eq, cgrid=new, cgraph=new2)


c.after(500,Voice.wishme)
c.after(1000, second_sc)

# __________________________________________________________________________________
root.mainloop()