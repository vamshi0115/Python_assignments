# print("helloworld")
# a=24
# b=37
# a=a+b
# print(a)

# age=int(input("enter the age"))
# if  age>=80:
#     print("not eligible")
# elif age>=18:
#     print("eligible")
# else:
#     print("too soon")

# file=open("data.txt","w")
# file.write("hello world\n")
# file.write("")

# write a programme to read a text file containing studentt marks and calcuate the average marks
# file=open("marks.txt","w")
# file.write("90\n")
# file.write("80\n")
# file.write("70\n")
# file.close()
# file=open("marks.txt","r")
# total=0
# count=0
# for line in file:
#     marks=int(line.strip())
#     total+=marks
#     count+=1
# average=total/count
# print("average marks:",average)

#write a programe to write user input into text file and append new data without deleting old data
user_input=input("enter some text:")
file=open("user_data.txt","a")