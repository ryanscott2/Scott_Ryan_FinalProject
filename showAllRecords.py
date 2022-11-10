# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class:
# Date of Submission:
# Description:
# Input:
# Output:
# Additional comments:
def showAll():
    allRecords = []  # Declare an empty list
    with open('file_records.txt', 'rt') as txt_file:
        for record in txt_file:
            allRecords.append(record)
        for element in allRecords:
            print(element)
        txt_file.close()
