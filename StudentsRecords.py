# ITP-100 Software Design
# Student: Scott, Ryan
# Instructor: Katherine Tupac
# Date given to class: 10/25/22
# Date of Submission: 10/28/22
# Description: This program takes a users input to select a function from a menu. This is done using two functions
# "mainMenu" which determines what to output given the users choice, and "menu" which stores the 8 lines of print
# functions we need to properly format the menu.
# Input: The input must be integers, 1-5 are assigned to the choices on the menu.
# Output: This program outputs the menu, and then the users choice. It does so for each input until the user enters 5.
# Additional Comments: This program only accepts integers as input. Any other input will crash it.

import createRecord
import showRecord
import deleteRecord
import showAllRecords
# why is this auto running the function in createRecord?

newRecord = 1
dispRecord = 2
delRecord = 3
dispAllRecords = 4
exit = 5

def mainMenu():
# The choice variable controls when the program will run, and stop running.
   choice1 = 0
   while choice1 != exit:
# Calling the menu function.
      menu()
# Takes user input, only integers will work with this program.
      choice1 = int(input('Enter your choice: '))
# Runs a print command if the user enters a valid input.
      if choice1 == newRecord:
         print('1. Create a record')
         createRecord.createRecord()
      elif choice1 == dispRecord:
         print('2. Show a record.')
      elif choice1 == delRecord:
         print('3. Delete a record.')
      elif choice1 == dispAllRecords:
         print('4. Display all records.')
         showAllRecords.showAll()
      elif choice1 == exit:
         print('5. Exiting the program.')
# This runs if the user inputs an invalid selection and informs them of the valid selections.
      else:
         print('Invalid selection. Please enter 1-5')
# The menu function stores the menu to be called when needed.
def menu():
    print('**********************************************')
    print('RECORDS MANAGER')
    print('**********************************************')
    print('\t1. Create a new record.')
    print('\t2. Show a record.')
    print('\t3. Delete a record.')
    print('\t4. Display All Records.')
    print('\t5. Exit')

# Calling the mainMenu function.
mainMenu()