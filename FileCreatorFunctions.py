import os 

def checkExists(directoryPath):
    if os.path.exists(directoryPath)==False:
        print("Sorry that directory does not exist. Please try again.")
        quit()   

def textFileType_Function(txt):
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
        bulk_duplicates_trimmed = bulk_duplicates.strip() ; bulk_duplicates_lower = bulk_duplicates_trimmed.lower()
        if bulk_duplicates_lower == "no":
            while txt > len(number_created)-1:
                i = number_created[-1] + 1
                number_created.append(i)
                if number_created == [0, 1]:
                    filename = input("What do you want the first file to be called? ")
                    number_of_file = f"({number_created[-1]})"
                    complete_name = os.path.join(directorySelection_Lower, filename+"{}.txt".format(number_of_file))
                    finalname = filename+"{}.txt".format(number_of_file)
                    open(complete_name, "x")
                    filesinpath.append(finalname)
                else:
                    filename = input("What do you want the next file to be called? ")
                    number_of_file = f"({number_created[-1]})"
                    complete_name = os.path.join(directorySelection_Lower, filename+"{}.txt".format(number_of_file))
                    finalname = filename+"{}.txt".format(number_of_file)
                    open(complete_name, "x")
                    filesinpath.append(finalname)
            print(f"Here are the current files in that directory: {filesinpath}")
            quit()
        elif bulk_duplicates_lower == "yes":
            filename = input("What do you want the files to be called? ")
            while txt > len(number_created)-1:
                i = number_created[-1] + 1
                number_created.append(i)
                number_of_file = f"({number_created[-1]})"
                complete_name = os.path.join(directorySelection_Lower, filename+"{}.txt".format(number_of_file))
                finalname = filename+"{}.txt".format(number_of_file)
                open(complete_name, "x")
                filesinpath.append(finalname)
            print(f"Here are the current files in that directory: {filesinpath}")
            quit()
    else:
        quit()

def PythonFileType_Function(py):
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
        bulk_duplicates_trimmed = bulk_duplicates.strip() ; bulk_duplicates_lower = bulk_duplicates_trimmed.lower()
        if bulk_duplicates_lower == "no":
            while py > len(number_created)-1:
                i = number_created[-1] + 1
                number_created.append(i)
                if number_created == [0, 1]:
                    filename = input("What do you want the first file to be called? ")
                    number_of_file = f"({number_created[-1]})"
                    complete_name = os.path.join(directorySelection_Lower, filename+"{}.py".format(number_of_file))
                    finalname = filename+"{}.py".format(number_of_file)
                    open(complete_name, "x")
                    filesinpath.append(finalname)
                else:
                    filename = input("What do you want the next file to be called? ")
                    number_of_file = f"({number_created[-1]})"
                    complete_name = os.path.join(directorySelection_Lower, filename+"{}.py".format(number_of_file))
                    finalname = filename+"{}.py".format(number_of_file)
                    open(complete_name, "x")
                    filesinpath.append(finalname)
            print(f"Here are the current files in that directory: {filesinpath}")
            quit()
        elif bulk_duplicates_lower == "yes":
            filename = input("What do you want the files to be called? ")
            while py > len(number_created)-1:
                i = number_created[-1] + 1
                number_created.append(i)
                number_of_file = f"({number_created[-1]})"
                complete_name = os.path.join(directorySelection_Lower, filename+"{}.py".format(number_of_file))
                finalname = filename+"{}.py".format(number_of_file)
                open(complete_name, "x")
                filesinpath.append(finalname)
            print(f"Here are the current files in that directory: {filesinpath}")
            quit()
    else:
        quit()


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
        bulk_duplicates_trimmed = bulk_duplicates.strip() ; bulk_duplicates_lower = bulk_duplicates_trimmed.lower()
        if bulk_duplicates_lower == "yes":
            filename = input("What do you want the file to be called? ")
            while other > len(number_created)-1:
                i = number_created[-1] + 1
                number_created.append(i)
                fileType = input("Please enter the type of file you need (Example: txt, py, doc, pdf, etc.)\n> ")
                number_of_file = f"({number_created[-1]})"
                complete_name = os.path.join(directorySelection_Lower, filename+"{}.{}".format(number_of_file, fileType))
                finalname = filename+"{}.{}".format(number_of_file, fileType)
                open(complete_name, "x")
                filesinpath.append(finalname)
            print(f"Here are the current files in that directory: {filesinpath}")
        elif bulk_duplicates_lower == "no":
            while other > len(number_created)-1:
                i = number_created[-1] + 1
                number_created.append(i)
                if number_created == [0, 1]:
                    filename = input("What do you want the first file to be called? ")
                    fileType = input("Please enter the type of file you need (Example: txt, py, doc, pdf, etc.)\n> ")
                    number_of_file = f"({number_created[-1]})"
                    complete_name = os.path.join(directorySelection_Lower, filename+"{}.{}".format(number_of_file, fileType))
                    finalname = filename+"{}.{}".format(number_of_file, fileType)
                    open(complete_name, "x")
                    filesinpath.append(finalname)
                    print(f"Here are the current files in that directory: {filesinpath}")
                else:
                    filename = input("What do you want the next file to be called? ")
                    fileType = input("Please enter the type of file you need (Example: txt, py, doc, pdf, etc.)\n> ")
                    number_of_file = f"({number_created[-1]})"
                    complete_name = os.path.join(directorySelection_Lower, filename+"{}.{}".format(number_of_file, fileType))
                    finalname = filename+"{}.{}".format(number_of_file, fileType)
                    open(complete_name, "x")
                    filesinpath.append(finalname)
                    print(f"Here are the current files in that directory: {filesinpath}")
    else:
        quit()