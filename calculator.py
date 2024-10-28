from tkinter import *
root=Tk()
root.title('SIMPLE CALCULATOR')
e=Entry(root,borderwidth=5,width=30)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
def buttonclick(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def buttonclear():
    e.delete(0,END)
def button_add():
    first=e.get()
    global f_num
    global mat
    mat='addition'
    f_num=int(first)
    e.delete(0,END)

def button_equal():
    second=e.get()
    e.delete(0,END)
    if mat=='addition':
        e.insert(0,f_num+int(second))
    elif mat=='substraction':
        e.insert(0,f_num-int(second))
    elif mat=='multiplication':
        e.insert(0,f_num*int(second))
    elif mat=='division':
        e.insert(0,f_num/int(second))
def button_mul():
    first=e.get()
    global f_num
    global mat
    mat='multiplication'
    f_num=int(first)
    e.delete(0,END)
def button_sub():
    first=e.get()
    global f_num
    global mat
    mat='substraction'
    f_num=int(first)
    e.delete(0,END)
    
def button_div():
    first=e.get()
    global f_num
    global mat
    mat='division'
    f_num=int(first)
    e.delete(0,END)


# define buttons
button1=Button(root,text='1',padx=40,pady=20,command=lambda:buttonclick(1))
button2=Button(root,text='2',padx=40,pady=20,command=lambda:buttonclick(2))
button3=Button(root,text='3',padx=40,pady=20,command=lambda:buttonclick(3))
button4=Button(root,text='4',padx=40,pady=20,command=lambda:buttonclick(4))
button5=Button(root,text='5',padx=40,pady=20,command=lambda:buttonclick(5))
button6=Button(root,text='6',padx=40,pady=20,command=lambda:buttonclick(6))
button7=Button(root,text='7',padx=40,pady=20,command=lambda:buttonclick(7))
button8=Button(root,text='8',padx=40,pady=20,command=lambda:buttonclick(8))
button9=Button(root,text='9',padx=40,pady=20,command=lambda:buttonclick(9))
button0=Button(root,text='0',padx=40,pady=20,command=lambda:buttonclick(0))
buttonad=Button(root,text='+',padx=39,pady=20,command=button_add)
buttonequal=Button(root,text='=',padx=91,pady=20,command=button_equal)
buttonc=Button(root,text='clear',padx=70,pady=20,command=lambda:buttonclear())
buttonmul=Button(root,text='*',padx=39,pady=20,command=button_mul)
buttonsub=Button(root,text='-',padx=39,pady=20,command=button_sub)
buttondiv=Button(root,text='/',padx=39,pady=20,command=button_div)

# put on screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)
buttonc.grid(row=4,column=1,columnspan=2)
buttonad.grid(row=5,column=0)
buttonequal.grid(row=5,column=1,columnspan=2)
buttonsub.grid(row=6,column=0)
buttonmul.grid(row=6,column=1)
buttondiv.grid(row=6,column=2)
 


root.mainloop()