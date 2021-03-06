from os import getenv,makedirs,path,remove,startfile,system,utime
from shutil import rmtree
from time import sleep
from sys import exit
from subprocess import run

SyncFileLocation = path.dirname(path.realpath(__file__))+"/portable"
TapeFileLocation = getenv("APPDATA") + "/Tape"
Files=["window-state-main.json","Preferences","Local Storage/file__0.localstorage"]
Folder=["Local Storage"]
IsExe=False

def CompareFiles(First,Second):
    #Get difference between Last Modify tag in 
    #check for file existance (if file doesn't exist if counts as old)
    try:
        diff=path.getmtime(First)
    except:
        diff=-1
    try:
        diff-=path.getmtime(Second)
    except:
        if diff==-1:
            return True

    if diff==0:
        #Same timme
        return True
    if diff > 0:
        #First is the last modify
        CopyFile(First,Second)
        return True
    if diff < 0:
        #Second is the last modify
        CopyFile(Second,First)
        return True
    return False
    
def CopyFile(Source,End):
    with open(Source,"rb") as f:
        with open(End,"wb") as d:
            d.write(f.read())
    utime(End,(path.getatime(Source),path.getmtime(Source))) #Copies Last Modify and Last access to the new copied file

def CheckFolder():
    #Check and Creates Folders in %appdata%/Tape/Local Storage and where Tape.exe is
    try:
        makedirs(TapeFileLocation+"/Local Storage")
    except FileExistsError:
        pass
    try:
        makedirs(SyncFileLocation+"/Local Storage")
    except FileExistsError:
        pass

def Sync():
    #Calls CompareFiles for every file in Files
    for file in Files:
        CompareFiles(TapeFileLocation+"/"+file,SyncFileLocation+"/"+file)

def ReadIniValue(Variable):
    #Returns the value of a Value in a .ini file
    with open(SyncFileLocation+"/Settings.ini","r") as f:
        for line in f.readlines():
            if Variable in line:
                value=line.split("=")[1]
                if value[0]==" ":
                    value=value[1:]
                if value[-1]=="\n":
                    value=value[:-1]
                return value
        return None

def FirstRun():
    #Autoinstalling and auto-deleting funciton
    #It renames Tape.exe to Real_Tape.exe
    #It create a copy of itself and name it Tape.exe (this is to save shortcut created)
    #then it runs the newcopy who delete the old version of itself.
    try:
        makedirs(SyncFileLocation)
    except FileExistsError:
        name=ReadIniValue("OldName")
        if name!="None":
            sleep(.5)
            remove(path.dirname(path.realpath(__file__))+"\\"+name)
            with open(SyncFileLocation+"/Settings.ini","r") as f:
                a=f.read()
            a=a.replace(name,"None")
            with open(SyncFileLocation+"/Settings.ini","w") as f:
                f.write(a)
        return
    selfname=path.basename(__file__)
    if IsExe:
         #using pyInstaller builder this function returns his name in py form (PortableTape.py)
         #so we have to correct it
        selfname=selfname.replace(".py",".exe")
    with open(SyncFileLocation+"/Settings.ini","w") as f:
        f.write(f"OldName = {selfname}\nDeleteTapeFolder = False\n")
    a=path.dirname(path.realpath(__file__))
    CopyFile(a+"\\Tape.exe",a+"/Real_Tape.exe")

    if IsExe:
        NewName="/Tape.exe"
    else:
        NewName="/Tape.py"
    CopyFile(a+"\\"+selfname,a+NewName)
    startfile(a+NewName)
    exit()

FirstRun()
CheckFolder()
Sync()
Path=(fr'"{path.dirname(path.realpath(__file__))}\Real_Tape.exe"')
run(Path, shell=False)
Sync()
if ReadIniValue("DeleteTapeFolder")=="True":
    rmtree(TapeFileLocation)