import sqlite3 as lite #importing sqlite (database)
import sys             #importing module that gives access to computer system
import os, shutil      #importing os module that allows us to use operating system dependent functionality
                       #importing shutil that allows file copying and/or removing. 
from datetime import datetime #importing module enabling us to see the date and time.
import os.path                #importing pathname manipulations
import time                   #importing time module so we can make the programme sleep for a certain amount of secs.

# Create a version of the database in database file (.db)
DB_NAME = "mydatabase.db"
con = lite.connect(DB_NAME)
#creating a datetime variable, with timezone = none.
datetime.now(tz=None)

#defining a function with variables that allow us create variables 
def dbFileInsert(tableName, fileName, filePath):
    # Creates the SQLite cursor that is used to query the database
    cur = con.cursor()  
    #Executing the desired database script
    cur.executescript("""
        DROP TABLE IF EXISTS """ + tableName + """; 
        CREATE TABLE """ + tableName + """ (fileName TEXT, filePath TEXT);   
        INSERT INTO """ + tableName + """ VALUES('""" + fileName + """','""" + filePath + """'); 
        """)


    # Force the database to make changes with the commit command
    con.commit()

    # Execute simple SQL query
    cur.execute('SELECT * FROM '+ tableName) 
    for i in cur:
        print("\n")
        for j in i:
            print(j)
            

    # Close the database
    con.close()


def fileCopy(fileName, fileFrom, fileTo):
    os.chdir('C:\\')
    print("Changing directionary to the C-drive...")
    os.path.isfile(fileTo)    
    os.path.isfile(fileTo+"\\"+fileName)

    # attempting to create a new folder.. if the folder already exists, the programme proceeds to execute the next step
    if os.path.exists(fileTo) == False: 
        os.system('mkdir NyFiskeFolder')
        print("Creating new folder...")
    elif os.path.exists(fileTo) == True:
        print("The folder already exists. Trying to copy image...")
        time.sleep(2)

    #copying image from old folder to newly created folder and prints the time, unless  already exists. 
    if os.path.exists(fileTo+"\\"+fileName) == False:
        shutil.copy(fileFrom+"\\"+fileName,fileTo+"\\"+fileName)
        shutil.copy(fileFrom+"\\"+fileName,fileTo+"\\"+fileName)
        dateTimeObj = datetime.now()
        print("Image has been copied to new folder at this time: ", dateTimeObj)
    elif os.path.exists(fileTo+"\\"+fileName) == True:
        print("The image has already been copied!")


#calling the functions with the desired variables
dbFileInsert("Images", r"fisk1.jpg", r"\content\images")

fileCopy("fisk1.jpg",r"C:\\FiskeFolder",r"C:\\NyFiskeFolder")