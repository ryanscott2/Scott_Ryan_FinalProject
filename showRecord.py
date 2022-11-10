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
    file_records = open("file_records.txt", "r")
    records = file_records.read()
    recordsList = records.split("\n")
    recordList=[]
    #if lastName in recordsList:


    print(recordsList)
    file_records.close()

showRecord()






