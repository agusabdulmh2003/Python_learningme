import tkinter as tk
from tkinter import  *
root = tk()
root.wm_title("jendela utama")
root.wm_iconbiitmap('man.ico')

root.geometry('300x200')
root.configure(bg="white")
root.state("normal")

root.mainloop()


#button


bpp = tk.Tk()
bpp.title("lanjutkan")
button = tk.button(bpp, text = 'stop', width = 25, command = bpp.destroy)
button.pack()
bpp.mainloop()


#style

master = Tk ()
w = Canvas(master, width=40, height=60)
w.pack()
canvas_height=20
canvas_width =200
y= int(canvas_height / 2)
w.create_line(0, y, canvas_width, y)
mainloop()

#checkbox

master = Tk()
master.title("hobby")
var1 = intVar()
Checkbutton(master, text = 'berenang', variable = var1).grid(row=0, sticky = w)
var2 = intVar()
Checkbutton(master, text = 'berkuda', variable = var1).grid(row=0, sticky = w)
mainloop()

# frame 

root = Tk()
frame = frame(root)
frame.pack()
bottomframe = frame(root)
bottomframe.pack (side = BOTTOM)
redbutton = Button(frame, text= "RED", fg = 'red')
redbotton.pack (side =LEFT)
greenbutton = Button(frame, text= "GREEN", fg = 'green')
greenbotton.pack (side =LEFT)
bluebutton = Button(frame, text= "BLUE", fg = 'blue')
bluebotton.pack (side =LEFT)
blackbutton = Button(frame, text= "BLACK", fg = 'black')
blackbotton.pack (side =LEFT)
yellowbutton = Button(frame, text= "YELLOW", fg = 'yellow')
yellowbotton.pack (side =BOTTOM)
root.mainloop()


#listbox

top = Tk()
top.title("BPP")
lb = Listbox(top)
lb.insert(1, 'python')
lb.insert(2, 'java')
lb.insert(3, 'C++')
lb.insert(4, 'PHP')
lb.insert(5, 'HTML')
lb.pack()
top.mainloop()



#navbar
ap=Tk()
ap.title(" APLIKASI SEJAHTERA")
menu = Menu (ap)
ap.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label = 'profil', menu = filemenu)
filemenu.add_command(label = 'sejarah')
filemenu.add_command(label = 'struktur organisasi')
filemenu.add_separator()
helpmenu = Menu(menu)
menu.add_cascade(label = 'help', menu = helpmenu)
helpmenu.add_command(label = 'tentang')
filemenu.add_separator()
logout = Menu(menu)
menu.add_cascade(label = 'logout', menu = logout)
hlogout.add_command(label = 'logout', command = ap.quit)

mainloop()





























