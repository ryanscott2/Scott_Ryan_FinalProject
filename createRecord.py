# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class:
# Date of Submission:
# Description:
# Input:
# Output:
# Additional comments: indexing for data storage  line 10, 20-22 WIP

def createRecord():
     file_records = open('file_records.txt', 'a')
     studentid = (input('Enter the student ID: '))
     firstname = (input('Enter the First Name: '))
     lastname = (input('Enter the Last Name: '))
     age = (input('Enter the Age: '))
     adress = (input('Enter the Address: '))
     phonenum = (input('Enter the Phone Number: '))
     recordList = [firstname, lastname, [studentid,  age, adress, phonenum]]
     with open("file_records.txt", "w") as txt_file:
          for line in recordList:
               txt_file.write(" ".join(line) + "\n")
     #for i in recordList:
          #file_records.write(i)
     file_records.write('\n')
     file_records.close()
     print(recordList)





createRecord()









