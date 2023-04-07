from tkinter import *
import tkinter.messagebox
import backend as pb

root=Tk()
root.title("student database management system")
root.geometry("1328x585")
root.config(bg="red")
stdId=StringVar()
Firstname=StringVar()
Surname=StringVar()
DoB=StringVar()
Age=StringVar()
Gender=StringVar()
Adress=StringVar()
Mobile=StringVar()
pb.studentData()
MainFrame=Frame(root,bg="red")
MainFrame.grid()
TitFrame=Frame(MainFrame,bd=1,padx=54,pady=8,bg="green",relief=RIDGE)
TitFrame.pack(side=TOP)

def iExit():
              iExit=tkinter.messagebox.askyesno("UJJWAL STUDENT MANAGEMENT SYSTEM","EXIT")
              if iExit>0:
                     root.destroy()
                     return

def clearData():
    txtStdId.delete(0,END)
    txtFirstname.delete(0,END)
    txtSurname.delete(0,END)
    txtDob.delete(0,END)
    txtAge.delete(0,END)
    txtGender.delete(0,END)
    txtAdress.delete(0,END)
    txtMobile.delete(0,END) 

def addData():
    if(len(stdId.get())!=0):
            pb.addStdRec(stdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Adress.get(),Mobile.get())
            studentlist.delete(0,END)
            studentlist.insert(END,(stdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Adress.get(),Mobile.get()))

def DisplayData():
    studentlist.delete(0,END)
    for row in pb.viewData():
        studentlist.insert(END,row)

def StudentRec(event):
        global sd
        searchstd = studentlist.curselection()[0]
        sd=studentlist.get(searchstd)
        if len(sd)==9:
            txtStdId.delete(0,END)
            txtStdId.insert(END,sd[1])
            txtFirstname.delete(0,END)
            txtFirstname.insert(END,sd[2])
            txtSurname.delete(0,END)
            txtSurname.insert(END,sd[3])
            txtDob.delete(0,END)
            txtDob.insert(END,sd[4])
            txtAge.delete(0,END)
            txtAge.insert(END,sd[5])
            txtGender.delete(0,END)
            txtGender.insert(END,sd[6])
            txtAdress.delete(0,END)
            txtAdress.insert(END,sd[7])
            txtMobile.delete(0,END)  
            txtMobile.insert(END,sd[8])                         
        else:
            txtStdId.delete(0,END)
            txtStdId.insert(END,sd[0])
            txtFirstname.delete(0,END)
            txtFirstname.insert(END,sd[1])
            txtSurname.delete(0,END)
            txtSurname.insert(END,sd[2])
            txtDob.delete(0,END)
            txtDob.insert(END,sd[3])
            txtAge.delete(0,END)
            txtAge.insert(END,sd[4])
            txtGender.delete(0,END)
            txtGender.insert(END,sd[5])
            txtAdress.delete(0,END)
            txtAdress.insert(END,sd[6])
            txtMobile.delete(0,END)  
            txtMobile.insert(END,sd[7])                         

def DeleteData():
              if(len(stdId.get())!=0):
                     pb.deleteRec(sd[0])
                     clearData()
                     DisplayData()

def searchDatabase():
              studentlist.delete(0,END)
              for row in pb.searchData(stdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Adress.get(),Mobile.get()):
                     studentlist.insert(END,row,str(""))       

def update():
              if(len(stdId.get())!=0):
                     pb.deleteRec(sd[0])
              if(len(stdId.get())!=0):
                     pb.addStdRec(stdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Adress.get(),Mobile.get())
                     studentlist.delete(0,END)
                     studentlist.insert(END,(stdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Adress.get(),Mobile.get()))   
    
lblTit=Label(TitFrame,font=('Courier',45,'bold'),text="Students Database Management System",bg="yellow",fg="black")
lblTit.grid()

lblTit=Label(TitFrame,font=('Courier',25,'bold'),text="JT GOLDEN JUBILEE",bg="yellow",fg="black")
lblTit.grid()

lblTit=Label(TitFrame,font=('Courier',12),text="(MADE BY UJJWAL SRIVASTAVA)",bg="yellow",fg="black")
lblTit.grid()

ButtonFrame=Frame(MainFrame,bd=1,width=1350,height=70,padx=18,pady=10,bg="yellow",relief=RIDGE)
ButtonFrame.pack(side=BOTTOM)

DataFrame=Frame(MainFrame,bd=9,width=1300,height=400,padx=20,pady=20,bg="#555",relief=RIDGE)
DataFrame.pack(side=BOTTOM)
         
DataFrameLeft=LabelFrame(DataFrame,font=('Courier',12,'bold'),bd=1,width=450,height=300,bg="Ghost White",relief=RIDGE,text="STUDENT INFO\n")
DataFrameLeft.pack(side=LEFT)

DataFrameRight=LabelFrame(DataFrame,font=('Courier',12,'bold'),bd=1,width=450,height=300,bg="Ghost White",relief=RIDGE,text="STUDENT DETAILS\n")
DataFrameRight.pack(side=RIGHT)
lblStdId=Label(DataFrameLeft,font=('Courier',12,'bold'),padx=2,pady=3,text="student Id:",bg="ghost white")
lblStdId.grid(row=0,column=0,sticky=W)
       
txtStdId=Entry(DataFrameLeft,font=('Courier',12,'bold'),textvariable=stdId,bg="ghost white",width=39)
txtStdId.grid(row=0,column=1)#student id

lblFirstname=Label(DataFrameLeft,font=('Courier',12,'bold'),padx=2,pady=3,text="First Name:",bg="ghost white")
lblFirstname.grid(row=1,column=0,sticky=W)
       
txtFirstname=Entry(DataFrameLeft,font=('Courier',12,'bold'),textvariable=Firstname,bg="ghost white",width=39)
txtFirstname.grid(row=1,column=1)#firstname


lblSurname=Label(DataFrameLeft,font=('Courier',12,'bold'),padx=2,pady=3,text="Surname:",bg="ghost white")
lblSurname.grid(row=2,column=0,sticky=W)
       
txtSurname=Entry(DataFrameLeft,font=('Courier',12,'bold'),textvariable=Surname,bg="ghost white",width=39)
txtSurname.grid(row=2,column=1)#surname

lblDob=Label(DataFrameLeft,font=('Courier',12,'bold'),padx=2,pady=3,text="Date of Birth",bg="ghost white")
lblDob.grid(row=3,column=0,sticky=W)
       
txtDob=Entry(DataFrameLeft,font=('Courier',12,'bold'),textvariable=DoB,bg="ghost white",width=39)
txtDob.grid(row=3,column=1)#dateof birth

lblAge=Label(DataFrameLeft,font=('Courier',12,'bold'),padx=2,pady=3,text="Age:",bg="ghost white")
lblAge.grid(row=4,column=0,sticky=W)
       
txtAge=Entry(DataFrameLeft,font=('Courier',12,'bold'),textvariable=Age,bg="ghost white",width=39)
txtAge.grid(row=4,column=1)#age

lblGender=Label(DataFrameLeft,font=('Courier',12,'bold'),padx=2,pady=3,text="Gender:",bg="ghost white")
lblGender.grid(row=5,column=0,sticky=W)
       
txtGender=Entry(DataFrameLeft,font=('Courier',12,'bold'),textvariable=Gender,bg="ghost white",width=39)
txtGender.grid(row=5,column=1)#gender

lblAdress=Label(DataFrameLeft,font=('Courier',12,'bold'),padx=2,pady=3,text="Address:",bg="ghost white")
lblAdress.grid(row=6,column=0,sticky=W)
       
txtAdress=Entry(DataFrameLeft,font=('Courier',12,'bold'),textvariable=Adress,bg="ghost white",width=39)
txtAdress.grid(row=6,column=1)#adress

lblMobile=Label(DataFrameLeft,font=('Courier',12,'bold'),padx=2,pady=3,text="Mobile:",bg="ghost white")
lblMobile.grid(row=7,column=0,sticky=W)
       
txtMobile=Entry(DataFrameLeft,font=('Courier',12,'bold'),textvariable=Mobile,bg="ghost white",width=39)
txtMobile.grid(row=7,column=1)#mobile

scrollbar=Scrollbar(DataFrameRight)
scrollbar.grid(row=0 ,column=1,sticky='ns')#scroll bar

studentlist=Listbox(DataFrameRight,width=68,height=12,font=('Courier',12,'bold'), yscrollcommand=scrollbar.set)
studentlist.bind('<<ListboxSelect>>',StudentRec)
studentlist.grid(row=0,column=0,padx=10)
scrollbar.config(command= studentlist.yview)

btnAddData=Button(ButtonFrame,text="Add New",font=('Courier',20,'bold'),height=1,width=10,bd=4,fg="#555",command=addData)
btnAddData.grid(row=2,column=0)#ADD NEW

btnDisplay=Button(ButtonFrame,text="Display",font=('Courier',20,'bold'),height=1,width=10,bd=4,fg="#555",command=DisplayData)
btnDisplay.grid(row=2,column=1)#DISPLAY

btnClear=Button(ButtonFrame,text="Clear",font=('Courier',20,'bold'),height=1,width=10,bd=4,fg="#555",command=clearData)
btnClear.grid(row=2,column=2)#CLEAR


btnDelete=Button(ButtonFrame,text="Delete",font=('Courier',20,'bold'),height=1,width=10,bd=4,fg="#555",command=DeleteData)
btnDelete.grid(row=2,column=3)#DELETE

btnSearch=Button(ButtonFrame,text="Search",font=('Courier',20,'bold'),height=1,width=10,bd=4,fg="#555",command=searchDatabase)
btnSearch.grid(row=2,column=4)#SEARCH


btnUpdate=Button(ButtonFrame,text="Update",font=('Courier',20,'bold'),height=1,width=10,bd=4,fg="#555",command=update)
btnUpdate.grid(row=2,column=5)#UPDATE

btnExit=Button(ButtonFrame,text="Exit",font=('Courier',20,'bold'),height=1,width=10,bd=4,fg="#555",command=iExit)
btnExit.grid(row=2,column=6)#EXIT

root.mainloop()
