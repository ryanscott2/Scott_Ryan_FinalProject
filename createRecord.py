# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 10/31/22
# Date of Submission: 11/10/22
# Description: This file takes the inputs listed below, stores them as strings, and then enters them into a list to be
# formatted in a manner that makes it easier to search for/sort specific records.
# Step by step explanation is included in the comments.
# Input: This file takes the student id, first and last name, age, address, and phone number as inputs
# Output: This file outputs "recordList" to "file_records.txt"
# Additional comments: All inputs are stores as strings, it will work with any input that can be stored as a string.

def createRecord():
# This opens the file an append mode so the records are added in chronological order.
     file_records = open('file_records.txt', 'a')
# Here we are prompting the user to enter the information
     studentid = (input('Enter the student ID: '))
     firstname = (input('Enter the First Name: '))
     lastname = (input('Enter the Last Name: '))
     age = (input('Enter the Age: '))
     address = (input('Enter the Address: '))
     phonenum = (input('Enter the Phone Number: '))
# This stores the records as a list and adds punctuation to make the records more readable and easier to search.
# I chose to store each student's record as one list to simplify formatting of the text file and possibly reduce
# runtime in cases of high volume record storage.
     recordList = [lastname, ', ', firstname, ' (', 'ID: ', studentid, ', ', 'Age: ',  age, ', ', 'Address: ',
                   address, ', ', 'Phone number: ', phonenum, ')']
     with open('file_records.txt', 'a') as txt_file:
# This enters the list into "file_records.txt" and then creates a new line.
          for line in recordList:
               txt_file.write("".join(line))
     file_records.write('\n')
# Closing text file
     file_records.close()
     txt_file.close()














