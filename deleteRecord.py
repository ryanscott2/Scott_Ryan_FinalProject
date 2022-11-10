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
    with open("file_records.txt", 'r') as txt_file:
        # read an store all lines into list
        lines = txt_file.readlines()
    with open("file_records.txt", 'w') as fp:
        for number, line in enumerate(lines):
            if lastName not in line:
                txt_file.write(line)








