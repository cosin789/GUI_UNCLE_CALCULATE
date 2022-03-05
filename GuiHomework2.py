from tkinter import *
import csv
from datetime import datetime
from tkinter.ttk import Notebook
from tkinter import ttk

GUI = Tk() #ผนัง
GUI.geometry('300x300+50+50')
n = Notebook(GUI) #สร้างง tab
Days = {'Mon' : 'จันทร์',
 'Tue' : 'อังคาร',
 'Wed' : 'พุธ',
 'Thu' : 'พฤหัสบดี',
 'Fri' : 'ศุกร์',
 'Sat' : 'เสาร์',
 'Sun' : 'อาทิตย์'}
Date = datetime.now()
#fr1 = Frame(n, width = 200, height = 200) 
#fr2 = Frame(n, width = 200, height = 200)
fr1 = Frame(n) 
fr2 = Frame(n)

icon_fr1 = PhotoImage(file = 'Finance-Wallet-icon.png')
icon_fr2 = PhotoImage(file = 'Bulleted-List-icon.png')
main_icon_fr1 = PhotoImage(file = 'City-Market-Square-icon.png')

#------------TAB-------------------#
n.add(fr1,text = f'{"คำนวณราคา" : ^{30}}',image = icon_fr1,compound = 'top')
n.add(fr2,text = "คำนวณราคา",image = icon_fr2,compound = 'top')
#n.pack()
n.pack(fill = BOTH)

#------------DEF-------------------#

def SaveToCal():
    Show_expanse = v_expanse.get()
    Show_price = v_price.get()
    Show_piece = v_piece.get()
    Total = Show_piece*Show_price
    v_expanse.set('')
    v_price.set('')
    v_piece.set('')

    print(f'{Show_expanse}, {Show_price:,d}, {Show_piece}, {Total}')
    Todays = datetime.now().strftime('%a')
    Dt = datetime.now().strftime('%Y-%m-%d-{} %H:%M:%S'.format(Days[Todays]))
    with open('savedata2.csv', 'a', encoding = 'utf-8', newline = '') as f:
        fw = csv.writer(f)
        data = [Show_expanse,Show_price,Show_piece,Total]
        fw.writerow(data)
    E2.focus()
    print(Dt)
#------------MAIN ICON-------------------#
mainicon = Label(fr1,image = main_icon_fr1)
mainicon.pack()
#------------LABEL-------------------#

L1 = Label(fr1,text = 'รายการ')
L1.pack()
v_expanse = StringVar()
E2 = Entry(fr1,textvariable = v_expanse)
E2.pack()

#------------ENTRY------------------#
L2 = Label(fr1,text = 'ราคา')
L2.pack()
v_price = IntVar()
E1 = Entry(fr1,textvariable = v_price)
E1.pack()
#------------PIECE------------------#
L3 = Label(fr1,text = 'จำนวน')
L3.pack()
v_piece = IntVar()
E1 = Entry(fr1,textvariable = v_piece)
E1.pack()
#------------BUTTON------------------#
#F1 = Frame(GUI)
#F1.place(x = 130, y = 150)
icon_OK = PhotoImage(file = 'Save-icon.png')


B1 = Button(fr1,text = 'OK', command = SaveToCal,image = icon_OK ,compound = 'left')
B1.pack(pady = 5)
#------------------------------------#

GUI.mainloop()
