# Portable Tape
Portable tabe is an excutable that allows to have all needed Tape files in a single forlder.
This allow Tape to be 100% portable.

## Installation
* Download and install [Aeriform Tape](https://www.aeriform.io/docs/tape)
* Copy the installation folder of Tape where you want it to be (Usb, GDrive OneCloud)

| OS | Location |
| ------ | ------ |
| Windows | %LOCALAPPDATA%\Programs\Tape |

* Uninstall Tape
* Download the [PortableTape.exe](https://github.com/Super99Master/Portable_Tape/raw/master/PortableTape.exe) and place it in the same folder
* Run it

## How It Works

The first time PortableTape.exe is started it renames the real *Tape.exe* in *Real_Tape.exe* and renames itself *Tape.exe*  
With this all your shortcut should keep working even if the Application is different.

PortableTape then check for Tape file in *%appdata%/Tape* and compares them to his saved file (./portable).  
The newer one gets copied to the other location.  
Then it runs *Real_Tape.exe* and it will detect the copied files and load them.  
When *Real_Tape.exe* is closed PortableTape will recheck each file to see if any of them changed and copy the newer one.  
The last thing it does **IF ENABLED** it deletes *%appdata%/Tape*. Deleting the last proof of ever running the software on your pc.  

## Enable AppData CleanUp
* Run PortableTape at least once
* Go to your Tape folder (where you placed PortableTape.exe)
* Then open "portable" (is a folder)
* Open with any editor "Settings.ini"
* Change "DeleteTapeFolder = False" to "DeleteTapeFolder = True"
* Save

## Bugs
* When you run the shortcut of the new Tape.exe with a Environment Variables (Es: %TapeFolder%/Tape.exe)  
PyInstaller fucks up the location of the .exe, running it in the folder of the shortcut itself, crashing the program. 

## TODO
The .exe file is being created by PyInstaller using --onefile.  
This is great for the purpose of this project but it's really slow to open, 4 seconds more or less.  
In the end it works, if u don't mine having to wait then it's perfect.  
For those who really mind the 4 seconds, i'll try my best in optimizing it but there is a limit on how much i can speed up PyInstaller --onefile.