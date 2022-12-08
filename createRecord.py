# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 11/12/22
# Date of Submission: 12/8/22
# Description: This file takes the inputs listed below, stores them as strings, checks to ensure no strings used in
# formatting are stored and then enters them into a list to be formatted in a manner that makes it easier to search
# for/sort specific records.
# Step by step explanation is included in the comments.
# Input: This file takes the student id, first and last name, age, address, and phone number as inputs
# Output: "recordList" to "file_records.txt", input prompts, and will inform the user if an input is invalid
# Additional comments: All inputs are stored as strings, it will work with any input that can be stored as a string
# that is not in "invalidInputs." While this is not perfect it is better than the alternative of the possibility of
# records that can not be deleted, or deleting the entire record file with a predictable invalid input.

def createRecord():
# Creating the set of sub strings used in formatting the stored records. This will later prevent issues deleting and
# showing records. This does mean no inputs with the listed substrings can be stored.
    invalidInputs = {', ', ' (', 'ID: ', 'Address: ', 'Phone number: ', ')', ',', '(', 'ID:', 'Address:',
                     'Phone number:', 'ID', 'Address', 'Phone number', 'Years Old'}
# Here we are prompting the user to enter the information
    studentid = (input('Enter the student ID: '))
    firstname = (input('Enter the First Name: '))
    lastname = (input('Enter the Last Name: '))
    age = (input('Enter the Age: '))
    address = (input('Enter the Address: '))
    phonenum = (input('Enter the Phone Number: '))
    invalidcount = 0
    templist = [studentid, firstname, lastname, age, address, phonenum]
    for item in templist:
        if item in invalidInputs:
            invalidcount += 1
    if invalidcount != 0:
# Most invalid inputs would be user error but in the case of rare names or nicknames an adjustment of capitalization
# will allow the record to be stored
        print('Please only enter the requested information, or adjust capitalization.')
        if invalidcount == 0:
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















