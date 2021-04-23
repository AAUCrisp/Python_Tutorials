import sqlite3 as lite #importing sqlite (database)
import sys             #importing module that gives access to computer system
import os, shutil      #importing os module that allows us to use operating system dependent functionality
                       #importing shutil that allows file copying and/or removing. 
from datetime import datetime #importing module enabling us to see the date and time.
import os.path                #importing pathname manipulations
import time                   #importing time module so we can make the programme sleep for a certain amount of secs.

# Create a version of the database in database file (.db)
DB_NAME = "mydatabase.db"
# con = lite.connect(DB_NAME)
#creating a datetime variable, with timezone = none.
datetime.now(tz=None)

#  ---  Function to insert file information in database  --- 
def dbFileInsert(tableName, fileName, filePath):            ##  Can easily be rewritten into universal "insertIntoDB()" thingy-ma-ding, but don't wanna change too much right now
    #Create SQL string
    sql = """ 
        INSERT INTO """ + tableName + """ VALUES('""" + fileName + """','""" + filePath + """'); 
        """
    # Send statement to the Database.
    updateDB(sql)


#  ---  Function to create a database table  ---       takes and string array in the column parameter, including the datatype    ex. "name TEXT"
def createTable(tableName, columns):
    # Start creating SQL string with the tablename
    sql = """
        DROP TABLE IF EXISTS """ + tableName + """; 
        CREATE TABLE """ + tableName + """ ("""

    # Loop over the columns and insert them into the SQL string
    for i in range(len(columns)):
        if i > 0:           # If this isn't the first iteration
            sql += """, """  # Insert a comma to separate them
        sql += columns[i]   # Insert column name into string

    sql += """);""" # Finish up the SQL string
    
    # Send statement to the database.
    updateDB(sql)


# -- Function to copy a file from one place to another -- 
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



#  ---  Function to send update querys to the database  ---
def updateDB(sql):
    print(sql)  # Write out the statement, just for testing purposes
    # Connect to the database
    con = lite.connect(DB_NAME)
    # Creates the SQLite cursor that is used to query the database
    cur = con.cursor()
    #Executing the desired database script
    cur.executescript(sql)
    # Force the database to make changes with the commit command
    con.commit()
    # Close the database
    con.close()


#  ---  Fuction to fetch all from a table  ---
def listAll(tableName):
    sql = 'SELECT * FROM ' + tableName

    # Connect to the database
    con = lite.connect(DB_NAME)
    # Creates the SQLite cursor that is used to query the database
    cur = con.cursor()
    # Execute simple SQL query
    cur.execute(sql)

    # Loop over the returned data and write it out in the console
    for i in cur:
        print("\n")
        for j in i:
            print(j)

    # Close the database
    con.close()
    

### ------------------------- ###
###  ----   TEST AREA   ----  ###
### ------------------------- ###
#calling the functions with the desired variables
createTable("Image", ["fileName TEXT", "filePath TEXT"])
dbFileInsert("Image", r"fisk1.jpg", r"\content\images")
dbFileInsert("Image", r"fisk2.jpg", r"\content\images")
listAll("Image")
#fileCopy("fisk1.jpg",r"C:\\FiskeFolder",r"C:\\NyFiskeFolder")
