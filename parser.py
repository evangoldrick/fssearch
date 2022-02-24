

def insertStringInTree(root: dict, string: str) -> None:
    currentNode = root
    currentString = string
    while len(currentString) != 0:
        if currentNode.get(currentString[0]) is not None:
            currentNode = currentNode[currentString[0]]
        else:
            currentNode[currentString[0]] = dict()
            currentNode = currentNode[currentString[0]]
            currentString = currentString[1:]

def makeSearchTreeFromLines(lines: list) -> dict:
    returnVal = dict()
    for line in lines:
        line = line.strip()
        for sub in range(len(line)):
            insertStringInTree(returnVal, line[sub:])
    return returnVal


def searchTreeForString(root: dict, string:str):
    pass
