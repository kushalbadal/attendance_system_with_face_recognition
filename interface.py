from tkinter import *
import tkinter.ttk as ttk
import csv
import os  # accessing the os functions
import check_camera
import Capture_Image
import Train_Image
import Recognize

root = Tk()
root.title("Attendance System ")
root.resizable(0, 0)
# Window size
appWidth = 852
appHeight = 480
font = "Times New Roman"


screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

x = int((screenWidth / 2) - (appWidth / 2))
y = int((screenHeight / 2) - (appHeight / 2))

# window pops up on center of the screen
root.geometry(f'{appWidth}x{appHeight}+{int(x)}+{int(y)}')

myLabel1 = Label(root, text="Attendance detail",
                 font=("Calibri", 15), fg="Blue", anchor=N)  # Title
myLabel1.place(relx=0.2,rely=0.0)
TableMargin = Frame(root, width=500)
TableMargin.place(relx=0.0,rely=0.05)

scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("ID", "Name", "Date",'Time'), height=400, selectmode="extended",
                    yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('ID', text="ID", anchor=W)
tree.heading('Name', text="Name", anchor=W)
tree.heading('Date', text="Date", anchor=W)
tree.heading('Time', text="Time", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=120)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.pack()
with open('Attendance/test.csv') as f:
  reader = csv.DictReader(f, delimiter=',')
  for row in reader:
    emp_id = row['Id']
    name = row['Name']
    dt = row['Date']
    ti = row['Time']
    tree.insert("", 0, values=(emp_id, name, dt,ti))



def checkCamera():
    check_camera.camer()


# --------------------------------------------------------------
# calling the take image function form capture image.py file

def CaptureFaces():
    Capture_Image.takeImages()



# -----------------------------------------------------------------
# calling the train images from train_images.py file

def Trainimages():
    Train_Image.TrainImages()



# --------------------------------------------------------------------
# calling the recognize_attendance from recognize.py file

def RecognizeFaces():
    Recognize.recognize_attendence()




button_generate = Button(root, text="Check Camera", padx=20, command=lambda :checkCamera())
button_generate.place(relx=0.76,rely=0.1)
button_generate = Button(root, text="Capture Faces", padx=20,command=lambda :CaptureFaces())
button_generate.place(relx=0.76,rely=0.2)
button_generate = Button(root, text="Train Images", padx=26,command=lambda :Trainimages())
button_generate.place(relx=0.76,rely=0.3)
button_generate = Button(root, text="Recognize\nAttendance", padx=33,command=lambda :RecognizeFaces())
button_generate.place(relx=0.76,rely=0.4)
button_generate = Button(root, text="Refresh", padx=43)
button_generate.place(relx=0.76,rely=0.53)
Output = Label(root,text="Status:",font=("Calibri", 15))
Output.place(relx=0.7,rely=0.64)
Output = Label(root,text="",height = 7,
                  width = 30,
                  bg = "white")
Output.place(relx=0.7,rely=0.7)
root.mainloop()
