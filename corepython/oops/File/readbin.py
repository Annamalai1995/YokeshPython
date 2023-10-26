from pickle import *
name=open("mydetails.txt","rb")
while True:
    try:
        studentdata=load(name)
        print(studentdata)
    except EOFError as e:
        break


# content=load(name)
# print(content)
# content1=load(name)
# print(content1)
# name.close()
