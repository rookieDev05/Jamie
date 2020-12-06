##importing CSV library to use its functions
import csv
from prettytable import PrettyTable
##declared a function to contain the whole process.
def searchContact():
    """opens file contact.csv. store it to csvfile variable"""
    
    with open('contact.csv') as csvfile:#OBJECT FILE
        readCSV = csv.reader(csvfile, delimiter=',')##MULTI-THREAD
        ##declared 3 empty list variables
        names = []
        address = []
        emails=[]
        Contacts = PrettyTable()
        Contacts.field_names=['Name','Location','Email']
        ##looped to get data from csv and store it to lists
        for row in readCSV:
            names.append(row[0])
            address.append(row[1])
            emails.append(row[2])
        print(names)
        whatName = input('\nYou are looking for: ')
        #whatName = 'dar'
        nameIndex = names.index(whatName)
        #nameIndex = names.index('dar')
        # nameIndex = 1
####        print(nameIndex)
        theirAdd= address[nameIndex] #address[1]
        theirEmail = emails[nameIndex]#emails[1]
        print( whatName,'is in',theirAdd,'\nemail is: ',theirEmail )
        
searchContact()
