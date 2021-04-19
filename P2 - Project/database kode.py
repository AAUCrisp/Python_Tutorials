import sqlite3 as lite
import sys

# Create a version of the database in database file (.db)
DB_NAME = "mydatabase.db"
con = lite.connect(DB_NAME)


# Create a version of the database in RAM 
#con = lite.connect(':memory:')

# Creates the SQLite cursor that is used to query the database
cur = con.cursor()  


    #DROP TABLE IF EXISTS Images;
    #CREATE TABLE Images(Id INT, Name TEXT, path TEXT);
# Execute desired SQL script
cur.executescript("""
    DROP TABLE IF EXISTS Images;
    CREATE TABLE Images(Name TEXT, path TEXT);
    INSERT INTO Images VALUES('fisk1.jpg','\content\images');
    INSERT INTO Images VALUES('fisk2.jpg','\content\images');
    INSERT INTO Images VALUES('fisk3.jpg','\content\images');
    INSERT INTO Images VALUES('fisk4.jpg','\content\images');
    """)

# Force the database to make changes with the commit command
con.commit()

# Execute simple SQL query
cur.execute('SELECT * FROM Images')
for i in cur:
    print("\n")
    for j in i:
        print(j)
        

# Close the database
con.close()
