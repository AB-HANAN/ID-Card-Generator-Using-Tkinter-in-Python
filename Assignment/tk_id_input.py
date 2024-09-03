#ABDUL HANAN ASIF
#Roll No. 261943888


#Import

import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

#Library and Title

my_w =tk.Tk()
my_w.geometry("500x400")
my_w.title("ID Card Generator")

#Main Heading 

tk.Label(my_w, text="Enter Data", font="ar 15 bold").grid(row=0, column=2)

#Assigning Variables

firstName = tk.StringVar(value='')
lastName = tk.StringVar(value='')
rollNo = tk.StringVar(value='')
Majors = tk.StringVar(value='')
gender=tk.StringVar(value='')
s_filename=''

l1=tk.Label(my_w,text='First Name',fg='blue')
l1.grid(row=1,column=1)
e1=tk.Entry(my_w,textvariable=firstName)
e1.grid(row=1,column=2)

l2=tk.Label(my_w,text='Last Name',fg='blue')
l2.grid(row=1,column=3)
e2=tk.Entry(my_w,textvariable=lastName)
e2.grid(row=1,column=4)

l3=tk.Label(my_w,text='Roll No.',fg='blue')
l3.grid(row=2,column=1)
e3=tk.Entry(my_w,textvariable=rollNo)
e3.grid(row=2,column=2)

l4=tk.Label(my_w,text='Major',fg='blue')
l4.grid(row=2,column=3)
e4=tk.Entry(my_w,textvariable=Majors)
e4.grid(row=2,column=4)

l5=tk.Label(my_w,text='Gender',fg='blue')
l5.grid(row=3,column=1)
e5=tk.Entry(my_w,textvariable=gender)
e5.grid(row=3,column=2)

l6=tk.Label(my_w,text='Select Image',fg='blue')
l6.grid(row=4,column=1)



checkvalue =  tk.IntVar

b1 = tk.Button(my_w, text='Upload',width=17,
    command = lambda:upload_file())
b1.grid(row=4,column=2,columnspan=1)

def upload_file():

    global img,s_filename
    f_types = [('Jpg Files', '*.jpg')]
    s_filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(file=s_filename)
    b4 =tk.Button(my_w,image=img) # using Button 
    b4.grid(row=4,column=2,columnspan=1)
    #print(s_filename)
    

b2=tk.Button(my_w,text='Submit',font=10,command=lambda:my_w.destroy())
b2.grid(row=10,column=1,padx=10,pady=10)

#Check Button
def getvar():
    print("ID Card Form submitted!")

checkbtn =tk.Checkbutton(text="Remember Me", variable = checkvalue)
checkbtn.grid(row=5, column=4)
tk.Button(my_w,text="Enter", command = getvar).grid(row=6, column=4)


my_w.mainloop()


