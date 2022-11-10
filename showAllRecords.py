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
    order = input('Enter A for ascending order or D for descending order: ')
    allRecords = []  # Declare an empty list
    with open('file_records.txt', 'rt') as txt_file:
        for record in txt_file:
            allRecords.append(record)
        if order == 'A':
            for element in allRecords:
                print(element)
        elif order == 'D':
            allRecords.sort(reverse=True)
            for element in allRecords:
                print(element)
        txt_file.close()


