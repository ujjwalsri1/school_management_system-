import pickle
def write():
    f=open('file.dat','wb')
    list=['a','s','p','e','d']
    pickle.dump(list,f)
    f.close()
write()
def read():
     f=open('file.dat','rb')
     lst=pickle.load(f)
     print(lst)
     f.close()

read()
