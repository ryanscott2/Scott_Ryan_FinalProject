# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 11/12/22
# Date of Submission: 12/8/22
# Description: This program will store the text file as a list, split the list twice so only the last name is searched
# for the string 'lastName' If there are no matches the user will be informed no records match that input.
# Step by step explanation is included in the comments.
# Input: This program takes the last name as a string input
# Output: This program will output 'Enter the student's last name' to prompt an input, and then
# 'Record(s) with the last name {lastName} deleted' if there are records with that last name found, or
# 'Record(s) not found' if no record is found.
# Additional comments: For best results please only enter the last name with proper capitalization. The input filters
# and splitting should prevent the vast majority of errors cause by user input but is not a catch-all.
def delRecord():
    lastName = input("Enter the student's last name: ")
# Creating the iterable object to keep track of matches
    lineCount = 0
# Opens "file_records.txt" in read mode to store in a list.
    with open("file_records.txt", 'r') as txt_file:
# read and store all lines into list
        lines = txt_file.readlines()
# Reopens file in write mode as "txt_file"
    with open("file_records.txt", 'w') as txt_file:
        for number, line in enumerate(lines):
# Splitting each line into a list separated at the '(' and then again at the ',' this prevents the program from
# searching for anything that is not the last name.
            linelist = line.split('(')
            linelist = linelist[0].split(',')
# Adds 1 to line count for each line that does not contain last time and then puts the line back in the text file
            if lastName not in linelist[0]:
                lineCount += 1
                txt_file.write(line)
    if len(lines) != lineCount:
        print(f'Record(s) with the last name {lastName} deleted')
# If the length of lines is equal to the amount of lines without last name that were reprinted, there was no record
# matching that lastName
    if len(lines) == lineCount:
        print('Record(s) not found')







