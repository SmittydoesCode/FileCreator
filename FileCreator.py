from FileCreatorFunctions import textFileType_Function, PythonFileType_Function, OtherFileType_Function
print("Welcome to File Creator!")
print("Okay. What kind of file would you like to create?")
fileTypes = ["[1] - .txt","[2] - .py", "[3] - Other"]
print(f"Here are your options:")
#Prints the available file types
for types in fileTypes:
    print(types)
fileType_Selection = int(input("Please enter 1, 2, or 3: "))
if fileType_Selection == 1:
    txt = int(input("How many .txt files do you need?\n> " ))
    textFileType_Function(txt)
elif fileType_Selection == 2:
    py = int(input("How many .py files do you need?\n> "))
    PythonFileType_Function(py)
elif fileType_Selection == 3:
    other = int(input("Okay no problem! Please enter how many files you need: "))
    OtherFileType_Function(other)