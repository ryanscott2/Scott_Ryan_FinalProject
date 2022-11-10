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
        lines = txt_file.readlines()
        for line in lines:
            if lastName not in line:
                txt_file.write(line)
    print(f'Record(s) with the last name {lastName} deleted.')

delRecord()




