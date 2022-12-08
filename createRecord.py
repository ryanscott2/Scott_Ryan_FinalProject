# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 11/12/22
# Date of Submission: 12/8/22
# Description: This file takes the inputs listed below, stores them as strings, and then enters them into a list to be
# formatted in a manner that makes it both easier to search for/sort specific records, and more readable. If lastname
# contains a ',' or '(' no record will be stored as this will cause issues with show and delete record.
# Step by step explanation is included in the comments.
# Input: This file takes the student id, first and last name, age, address, and phone number as inputs
# Output: "recordList" to "file_records.txt", input prompts. Also outputs a message informing user if their input
# is invalid
# Additional comments: All inputs are stored as strings, it will work with any input that can be stored as a string
# excluding a ',' or '(' in lastname.

def createRecord():
    invalid = [',', '(']
    numinvalid = 0
# Here we are prompting the user to enter the information
    studentid = (input('Enter the student ID: '))
    firstname = (input('Enter the First Name: '))
    lastname = (input('Enter the Last Name: '))
    age = (input('Enter the Age: '))
    address = (input('Enter the Address: '))
    phonenum = (input('Enter the Phone Number: '))
# Checking lastname for any input that would cause issues with splitting in delete and show record
    for i in invalid:
# Checking if any character in i (each element of last name is compared separately under the name i) matches a character
# in lastname (char)
        if any(char in lastname for char in i):
            print('"(" and "," are used to format the records. Please exclude those from the last name')
            numinvalid += 1
# Formatting and storing record if no invalid inputs are detected
    if numinvalid == 0:
# This stores the records as a list and adds punctuation to make the records more readable and easier to search.
# I chose to store each student's record as one list to simplify formatting of the text file and possibly reduce
# runtime in cases of high volume record storage.
        recordList = [lastname, ', ', firstname, ' (', 'ID: ', studentid, ', ',  age, ' Years Old, ', 'Address: ',
                      address, ', ', 'Phone number: ', phonenum, ')']
        with open('file_records.txt', 'a') as txt_file:
# This enters the list into "file_records.txt" and then creates a new line.
            for line in recordList:
                txt_file.write("".join(line))
            txt_file.write('\n')















