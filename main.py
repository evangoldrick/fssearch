from fileinput import filename
import json
import parser



userInput = ""
searchTreeRoot = None

def getExistingFileNameFromUser(prompt: str="Enter file name: "):
    while True:
            file = input(prompt)
            try:
                with open(file, "r") as inFile:
                    pass
                break
            except FileNotFoundError as e:
                print(e)
                print("Try again")

    return file

while True:
    userInput = input("Enter search mode(h for help): ")
    if userInput == "h":
        print("lj: load pre computed json format file")
        print("lf: load strings from text file")
        print("s: search mode")
        print("wj: write computed json file")
        print("q: quit")
    elif userInput == "lj":
        print("Not yet implemented")
        
    elif userInput == "lf":
        fileName = getExistingFileNameFromUser()
        with open(fileName, "r") as inFile:
            searchTreeRoot = parser.makeSearchTreeFromLines(inFile.readlines())
    elif userInput == "s":
        print("Not yet implemented")
    elif userInput == "wj":
        fileName = input("Enter file name to write out to: ")
        print(f"Writing {fileName}")
        with open(fileName, "w") as outFile:
            outFile.write(json.dumps(searchTreeRoot))
        print("Done")
    elif userInput == "q":
        break
    else:
        print("Unknown command")
