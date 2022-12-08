# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 11/12/22
# Date of Submission: 11/22/22
# Description: This file searches through "file_records.txt" line by line and looks for any lines that have a string
# matching "lastName." If the line contains a match it will add 1 to "lineCount" and print the record. The iterable
# object "lineCount" allows the program to keep track of how many records match. If none match it will
# print "Record not found." Step by step explanation is provided in the comments
# Input: This file takes the last name of the student as input
# Output: This file outputs record(s) with a string that matches the variable "lastName"
# Additional comments: Please only enter the students last name for best results as the entire records is a string.
# Entering other information will not break the program but may not return accurate results.
def showRecord():
# Getting the desired search term from the user.
    lastName = input('Enter the students last name: ')
    print()
# Creating lineCount to keep track of matches.
    lineCount=0
# Opening "file_records.txt" in read mode and reading the lines into a list called "lines"
    with open('file_records.txt', 'r') as txt_file:
        lines = txt_file.readlines()
#   Iterates through the list of lines and assigns each element to line. line.find then checks if the line contains a
#   match for the string "lastName"
        for line in lines:
            if line.find(lastName) != -1:
# Prints records that match the string contained by lastName
                print('Record(s) with the last name', lastName, ':', line)
                lineCount += 1
# If there are no matches this will execute the print line and inform the user that
# no records with that last name exist
    if lineCount == 0:
        print('Record not found')










