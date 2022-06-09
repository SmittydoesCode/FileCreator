import os 

def checkExists(directoryPath):
    if os.path.exists(directoryPath)==False:
        print("Sorry that directory does not exist. Please try again.")
        OtherFileType_Function()
def OtherFileType_Function(other):
    #Directory Selection    
    directorySelection = input("Please enter the path of the directory you wish to store the files in:\n> ")
    directorySelection_Trimmed = directorySelection.strip()
    directorySelection_Lower = directorySelection_Trimmed.lower()
    checkExists(directorySelection_Lower)
    print(f"You said: {directorySelection}. Is that correct?")
    #Directory Confirmation
    directory_Confirm = input("Yes or no? ")
    directory_Confirm_Trimmed = directory_Confirm.strip()
    directory_Confirm_Lower = directory_Confirm_Trimmed.lower()
    if directory_Confirm_Lower == "yes":
        number_created = [0]
        filesinpath = os.listdir(directorySelection_Lower)
        bulk_duplicates = input("Do you want them all to be the same name?\nYes or No? ")
        filetype_bulk = input("Are they all the same type?\n Yes or no? ")
        filetype_bulk_trimmed = filetype_bulk.strip() ; filetype_bulk_lower = filetype_bulk_trimmed.lower()
        bulk_duplicates_trimmed = bulk_duplicates.strip() ; bulk_duplicates_lower = bulk_duplicates_trimmed.lower()
        if bulk_duplicates_lower == "yes" and filetype_bulk_lower == "yes":
            filename = input("What do you want the files to be called? ")
            fileType = input("Please enter the type of files you need (Example: txt, py, doc, pdf, etc.)\n> ")
            while other > len(number_created)-1:
                i = number_created[-1] + 1
                number_created.append(i)
                number_of_file = f"({number_created[-1]})"
                complete_name = os.path.join(directorySelection_Lower, filename+"{}.{}".format(number_of_file, fileType))
                finalname = filename+"{}.{}".format(number_of_file, fileType)
                open(complete_name, "x")
                filesinpath.append(finalname)
            print(f"Here are the current files in that directory: {filesinpath}")
        elif bulk_duplicates_lower == "no" and filetype_bulk_lower == "yes":
            fileType = input("Please enter the type of file you need (Example: txt, py, doc, pdf, etc.)\n> ")
            while other > len(number_created)-1:
                i = number_created[-1] + 1
                number_created.append(i)
                if number_created == [0, 1]:
                    filename = input("What do you want the first file to be called? ")
                    number_of_file = f"({number_created[-1]})"
                    complete_name = os.path.join(directorySelection_Lower, filename+"{}.{}".format(number_of_file, fileType))
                    finalname = filename+"{}.{}".format(number_of_file, fileType)
                    open(complete_name, "x")
                    filesinpath.append(finalname)                    
                else:
                    filename = input("What do you want the next file to be called? ")
                    number_of_file = f"({number_created[-1]})"
                    complete_name = os.path.join(directorySelection_Lower, filename+"{}.{}".format(number_of_file, fileType))
                    finalname = filename+"{}.{}".format(number_of_file, fileType)
                    open(complete_name, "x")
                    filesinpath.append(finalname)
            print(f"Here are the current files in that directory: {filesinpath}")
        elif bulk_duplicates_lower == "yes" and filetype_bulk_lower == "no":
            filename = input("What do you want the files to be called? ")
            while other > len(number_created)-1:
                i = number_created[-1] + 1
                number_created.append(i)
                if number_created == [0, 1]:
                    fileType = input("Please enter the file type of the first file. (Example: txt, py, doc, pdf, etc.):\n> ")
                    number_of_file = f"({number_created[-1]})"
                    complete_name = os.path.join(directorySelection_Lower, filename+"{}.{}".format(number_of_file, fileType))
                    finalname = filename+"{}.{}".format(number_of_file, fileType)
                    open(complete_name, "x")
                    filesinpath.append(finalname)
                else:
                    fileType = input("Please enter the file type of the next file. (Example: txt, py, doc, pdf, etc.):\n> ")
                    number_of_file = f"({number_created[-1]})"
                    complete_name = os.path.join(directorySelection_Lower, filename+"{}.{}".format(number_of_file, fileType))
                    finalname = filename+"{}.{}".format(number_of_file, fileType)
                    open(complete_name, "x")
                    filesinpath.append(finalname)
            print(f"Here are the current files in that directory: {filesinpath}")
        elif bulk_duplicates_lower == "no" and filetype_bulk_lower == "no":
            while other > len(number_created)-1:
                i = number_created[-1] + 1
                number_created.append(i)
                if number_created == [0, 1]:
                    filename = input("Please enter the file name of the first file. (Example: Name")
                    fileType = input("Please enter the file type of the first file. (Example: txt, py, doc, pdf, etc.):\n> ")
                    number_of_file = f"({number_created[-1]})"
                    complete_name = os.path.join(directorySelection_Lower, filename+"{}.{}".format(number_of_file, fileType))
                    finalname = filename+"{}.{}".format(number_of_file, fileType)
                    open(complete_name, "x")
                    filesinpath.append(finalname)
                else:
                    filename = input("Please enter the file name of the next file. (Example: Name")
                    fileType = input("Please enter the file type of the next file. (Example: txt, py, doc, pdf, etc.):\n> ")
                    number_of_file = f"({number_created[-1]})"
                    complete_name = os.path.join(directorySelection_Lower, filename+"{}.{}".format(number_of_file, fileType))
                    finalname = filename+"{}.{}".format(number_of_file, fileType)
                    open(complete_name, "x")
                    filesinpath.append(finalname)
            print(f"Here are the current files in that directory: {filesinpath}")
    else:
        OtherFileType_Function(other)