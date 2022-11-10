# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 10/31/22
# Date of Submission: 11/10/22
# Description: This program will store the text file as a list, and then search that list for strings that match the
# entered string. If there is a match it will delete any lines containing that match.
# Input: This program takes the last name as a string input
# Output:
# Additional comments: Caution, entering strings other than the last name can result in the entire record file being
# deleted. For example, entering "ID: " will match all the record files and delete them all.
def delRecord():
    lastName = input('Enter the students last name: ')
    lines = []
    lineCount = 0
    with open("file_records.txt", 'r') as txt_file:
        # read an store all lines into list
        lines = txt_file.readlines()
    with open("file_records.txt", 'w') as txt_file:
        for number, line in enumerate(lines):
            if lastName not in line:
                lineCount+=1
                txt_file.write(line)
    if len(lines) == lineCount:
        print('Record not found')
    txt_file.close()







