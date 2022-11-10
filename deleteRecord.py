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
    with open('file_records.txt', 'r+') as txt_file:
        # read all lines in a list
        lines = txt_file.readlines()
        txt_file.seek(0)
        txt_file.truncate()
        for line in lines:
            if line.find(lastName) != -1:
                for number, line in enumerate(lines):
                    # delete line number 5 and 8
                    # note: list index start from 0
                    if number not in []:
                        txt_file.write(line)





