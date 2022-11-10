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
     address = (input('Enter the Address: '))
     phonenum = (input('Enter the Phone Number: '))
     recordList = [lastname, ', ', firstname, ' (', 'ID: ', studentid, ', ', 'Age: ',  age, ', ', 'Address: ',
                   address, ', ', 'Phone number: ', phonenum, ')']
     with open('file_records.txt', 'a') as txt_file:
          for line in recordList:
               txt_file.write("".join(line))
     file_records.write('\n')
     file_records.close()
















