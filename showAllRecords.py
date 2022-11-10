# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 10/31/22
# Date of Submission: 11/10/22
# Description: This file takes all data in the text file, turns each line into a list item, and then prints the list.
# Input: The only input required is "A" for ascending order, or "D" for descending order. Lower and uppercase work.
# Output:
# Additional comments:
def showAll():
    order = input('Enter A for ascending order or D for descending order: ')
    allRecords = []  # Declare an empty list
    with open('file_records.txt', 'rt') as txt_file:
        for record in txt_file:
            allRecords.append(record)
        if order == 'A' or order == 'a':
            for element in allRecords:
                print(element)
        elif order == 'D' or order == 'd':
            allRecords.sort(reverse=True)
            for element in allRecords:
                print(element)
        txt_file.close()


