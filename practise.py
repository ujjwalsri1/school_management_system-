import pickle
class Student:
    def _init_(self,rno=0,name=''):
        self.rollno=rno
        self.name=name
        self.marks1,self.marks2,self.marks3=0.0,0.0,0.0

    def readmarks(self):
        self.marks1=float(input('subject1'))
        self.marks2=float(input('subject2'))
        self.marks3=float(input('subject3'))
        self.name=input('enter a name')
        
    def display(self):
        print('roll no',self.rollno)
        print('name',self.name)
        print('marks',self.marks1,self.marks2,self.marks3)

stud1=Student()
stud2=Student()
stud1.readmarks()
stud2.readmarks()
file=open('student_data.log','wb')
pickle.dump(stud1,file)
pickle.dump(stud2,file)



        
def binaryfile_update():
    file=open('student_data.log','rb')
    pc=int(input("enter a number"))
    file.seek(0)
    try:
        while True:
            data=pickle.load(file)
            data.display()
            for record in data:
                if record[0]==pc:
                    record1=int(input("enter a number1"))
                    record2=int(input("enter a number2"))

                file.seek(std)
                pickle.dumb(data,file)
                break
    except EOFError:
        file.close()
binaryfile_update()
