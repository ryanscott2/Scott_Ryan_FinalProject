# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class:
# Date of Submission:
# Description:
# Input:
# Output:
# Additional comments:
def showRecord():
    lastName = input('Enter the students last name: ')
    with open('file_records.txt', 'r') as txt_file:
        lines = txt_file.readlines()
        for line in lines:
            if line.find(lastName) != -1:
                print('Record(s) with the last name', lastName, ':', line)








