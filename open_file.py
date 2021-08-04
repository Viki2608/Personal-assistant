import subprocess
import os

def find_files(filename, search_path):
   result = []
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

def open_file():
    driveStr = subprocess.check_output("fsutil fsinfo drives")
    driveStr1 = driveStr.strip().lstrip().decode()
    driveStr=driveStr1.replace('Drives:','')
    drives = driveStr.split()
    #print("Total no of drives are :",len(drives))
    target='modify_reg.txt'
    print("File name",target)
    for drive in drives:
        if(drive=='C:\\'):
            print('Entered')
            if (find_files(target, drive)):
                print("File Found At", find_files(target, drive))
                str1 = ''.join(find_files(target, drive))
                #target=target.join('\\')
                print(str1.replace(target,''))
                str1=str1.replace(target,'')
                subprocess.Popen(f'explorer "{str1}"')
                #os.system(str1)
                break
        else:
            #filepath = find_file(target, drive)
            if(find_files(target,drive)):
                print("File Found At",find_files(target,drive))
                str1 = ''.join(find_files(target,drive))
                print(str1)
                #os.system(str1)
                break

open_file()
