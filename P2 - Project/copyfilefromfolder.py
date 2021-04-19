# importing os & shutil modules
import os, shutil 
from datetime import datetime
import os.path
import time

datetime.now(tz=None)

# method to change current working directionary to a specified path - here local drive c. 
os.chdir('C:\\')
print("Changing directionary to the C-drive...");
os.path.isfile(r"C:\\NyFiskeFolder")
os.path.isfile(r"C:\\NyFiskeFolder\\fisk1.jpg")

# attempting to create a new folder.. if the folder already exists, the programme proceeds to execute the next step
if os.path.exists(r"C:\\NyFiskeFolder") == False: 
    os.system('mkdir NyFiskeFolder')
    print("Creating new folder...");
elif os.path.exists(r"C:\\NyFiskeFolder") == True:
    print("The folder already exists. Trying to copy image...");
    time.sleep(2)

#copying image from folder to newly created folder
if os.path.exists(r"C:\\NyFiskeFolder\\fisk1.jpg") == False:
    shutil.copy('C:\\FiskeFolder\\fisk1.jpg','C:\\NyFiskeFolder')
    dateTimeObj = datetime.now()
    print("Image has been copied to new folder at this time: ", dateTimeObj);
elif os.path.exists(r"C:\\NyFiskeFolder\\fisk1.jpg") == True:
    print("The image has already been copied!")

