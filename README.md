# Portable Tape
Portable tabe is an excutable that allows to have all needed Tape files in a single forlder.
This allow Tape to be 100% portable.

## Installation
* Download and install [Aeriform Tape](https://www.aeriform.io/docs/tape)
* Copy the installetion folder of Tape where you want it to be (Usb, GDrive OneCloud)
* Uninstall Tape

| OS | Location |
| ------ | ------ |
| Windows | %LOCALAPPDATA%\Programs\Tape |

* Download the PortableTape.exe and place it in the same folder
* Run it

## How It Works

The first time PortableTape.exe is started it rename the real Tape.exe in Real_Tape.exe and rename himself Tape.exe
With this all your shortcut should keep working even if the Application is different.

PortableTape then check for Tape file is *%appdata%/Tape* and compares them to his saved file (./portable)
The newer one gets copied to the other location. 
Then it runs Real_Tape.exe and it will detect the copied files and load them.
When Real_Tape.exe is closed PortableTape will recheck each file to see if any of them changed and copy the newer one.
The last thing it does **IF ENABLED** it deletes *%appdata%/Tape*. Deleting the last proof of ever running the software on your pc.

## Enable AppData CleanUp
* Run PortableTape at least once
* Go to your Tape folder (where you placed PortableTape.exe)
* Then open "portable" (is a folder)
* Open with any editor Settings.ini
* Change "DeleteTapeFolder = False" to "DeleteTapeFolder = True"
* Save
