from node import Node

def insertStringInTree(root: dict, string: str) -> None:
    currentString = string
    root.strings.append(string)
    for i in range(len(string)):
        currentNode = root
        currentString = string[i:]
        for c in currentString:
            if currentNode.children.get(c) is None:
                currentNode.children[c] = Node()
                currentNode = currentNode.children[c]
            else:
                currentNode = currentNode.children[c]
            if string not in currentNode.strings:
                currentNode.strings.append(string)

def makeSearchTreeFromLines(lines: list) -> Node:
    returnValue = Node()
    
    for line in lines:
        insertStringInTree(returnValue, line)

    return returnValue

def searchTreeForString(root: dict, string:str) -> list:
    print(string, root.strings)
    if len(string) == 0:
        return root.strings
    else:
        return searchTreeForString(root.children[string[0]], string[1:])
