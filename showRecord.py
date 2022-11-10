# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 10/31/22
# Date of Submission: 11/10/22
# Description:
# Input:
# Output:
# Additional comments:
def showRecord():
    lastName = input('Enter the students last name: ')
    lineCount=0
    with open('file_records.txt', 'r') as txt_file:
        lines = txt_file.readlines()
        for line in lines:
            if line.find(lastName) != -1:
                print('Record(s) with the last name', lastName, ':', line)
                lineCount+=1
    if lineCount == 0:
        print('Record not found')
    txt_file.close()










