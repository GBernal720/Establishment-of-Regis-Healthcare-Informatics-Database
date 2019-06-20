import os
import shutil
from Import_Function import  *
path = "C:\Users\eltac\Desktop\Regis_Homework\Test_Folder\Test_Data"
Archive="C:\Users\eltac\Desktop\Regis_Homework\Test_Folder\Archive"
def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

for file in files(path):
    csvfile = file
    name = csvfile.replace(".csv", "")
    fullpath = (path + '\\' + csvfile)
    ArchivePath = (Archive + '\\' + csvfile)
    print(csvfile)
    print (name)
    print (fullpath)
    run_test(fullpath, name)
    shutil.move(fullpath, ArchivePath)
