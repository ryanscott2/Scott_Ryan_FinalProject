# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 11/12/22
# Date of Submission: 11/22/22
# Description: This program will store the text file as a list, and then search that list for strings that match the
# entered string. If there is a match it will delete any lines containing that match.
# Step by step explanation is included in the comments.
# Input: This program takes the last name as a string input
# Output: This program will output 'Enter the student's last name' to prompt an input, and then either
# 'Record(s) deleted' if there are records with that last name found, or 'Record not found' if no record is found.
# Additional comments: Caution, entering strings other than the last name can result in the entire record file being
# deleted. For best results please enter only the student's last name with appropriate capitalization.
def delRecord():
    invalidInputs = {', ', ' (', 'ID: ', 'Address: ', 'Phone number: ', ')', ',', '(', 'ID:',
                     'Address:', 'Phone number:', 'ID', 'Address', 'Phone number', 'Years Old'}
    lastName = input("Enter the student's last name: ")
# Filtering substrings used to format the records file that could result in all records being deleted.
    if lastName in invalidInputs:
        print('Please only enter the students last name\n')
# Creating the iterable object to keep track of matches
    lineCount = 0
    if lastName not in invalidInputs:
# Opens "file_records.txt" in read mode to store in a list.
        with open("file_records.txt", 'r') as txt_file:
# read and store all lines into list
            lines = txt_file.readlines()
# Reopens file in write mode as "txt_file"
        with open("file_records.txt", 'w') as txt_file:
            for number, line in enumerate(lines):
# Adds 1 to line count for each line that does not contain last time and then puts the line back in the text file
                if lastName not in line:
                    lineCount += 1
                    txt_file.write(line)
        print(f'Record(s) with the last name {lastName} deleted')
# If the length of lines is equal to the amount of lines without last name that were reprinted, there was no record
# matching that lastName
        if len(lines) == lineCount:
            print('Record not found')







