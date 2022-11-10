# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class:
# Date of Submission:
# Description:
# Input:
# Output:
# Additional comments:
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







