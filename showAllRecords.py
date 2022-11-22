# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 11/12/22
# Date of Submission: 11/22/22
# Description: This file takes all data in the text file, turns each line into a list item, and then prints the list.
# Step by step explanation is included in comments.
# Input: The only input required is "A" for ascending order, or "D" for descending order. Lower and uppercase work.
# Output: This file will output all records contained in "file_records.txt" in ascending or descending order.
# Additional comments:
def showAll():
# Requesting input to determine order of sorting
    order = input('Enter A for ascending order or D for descending order: ')
# Creating the list that the records will be added to
    allRecords = []
# Opening the file in read mode under the name "txt_file"
    with open('file_records.txt', 'rt') as txt_file:
# Iterates through each line of the file and adds each line as an element to the list created on like 17
        for record in txt_file:
            allRecords.append(record)
# If the user inputs 'A' or 'a' it will print in ascending order
        if order == 'A' or order == 'a':
# For readability, I use a for loop to print each element on its own line
            for element in allRecords:
                allRecords.sort()
                print(element)
# Prints the list in descending order if the input is 'D' or 'd' by sorting in reverse
        elif order == 'D' or order == 'd':
            allRecords.sort(reverse=True)
            for element in allRecords:
                print(element)
# Closing the text file
        txt_file.close()


