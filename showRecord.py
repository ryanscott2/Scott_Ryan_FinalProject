# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 11/12/22
# Date of Submission: 12/8/22
# Description: This file ready "file_records.txt" into a list, splits it twice so only the last name input is checked
# for matches, and informs the user if there are or are not matches. Any matching records will be displayed.
# Input: This file takes the last name of the student as input
# Output: This file outputs record(s) with a string that matches the variable "lastName", or 'Records(s) not found'
# Additional comments: Like to deleteRecord file, please only enter the last name with proper capitalization. The input
# filters and splitting should prevent the vast majority of errors cause by user input but is not a catch-all.
def showRecord():
# Getting the desired search term from the user.
    lastName = input('Enter the students last name: ')
# Creating lineCount to keep track of matches.
    lineCount=0
# Opening "file_records.txt" in read mode and reading the lines into a list called "lines"
    with open('file_records.txt', 'r') as txt_file:
        lines = txt_file.readlines()
# Iterates through the list of lines and assigns each element to line. line.find then checks if the line contains a
# match for the string "lastName"
        for line in lines:
# Splitting each line into a list separated at the '(' and then again at the ',' this prevents the program from
# searching for anything that is not the last name
            linelist = line.split('(')
            linelist = linelist[0].split(',')
            if linelist[0].find(lastName) != -1:
# Prints records that match the string contained by lastName
                print(f'Record(s) with the last name {lastName}: {line}', end='')
                lineCount += 1
# If there are no matches this will execute the print line and inform the user that
# no records with that last name exist
    if lineCount == 0:
        print('Record(s) not found')










