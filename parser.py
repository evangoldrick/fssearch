import json
from node import Node

def getMaxLengthString(arr: list) -> int:
    longest = 0
    for element in arr:
        if len(element) > longest:
            longest = len(element)

    return longest

def insertStringInTree(root: Node, string: str) -> None:
    string = string.strip()
    root.strings.append(string)
    if len(string) > root.depth:
        root.depth = len(string)

    for i in range(len(string)):  # iterate through the letters of the string
        currentNode = root  # set current node to root so that we can start over for each letter in the string
        currentString = string[i:]  # current string to be inserted

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
        insertStringInTree(returnValue, line)  # Insert each line into the search tree

    return returnValue

def makeSearchTreeFromDict(root:dict):
    returnValue = Node()

    for k in root["children"].keys():
        Node.children[k] = makeSearchTreeFromDict(root["children"][k])
    
    Node.strings = root
    print(returnValue)
    assert False and "Not implemented"
    return returnValue    


def searchTreeForString(root: dict, string:str) -> list:
    if len(string) == 0:
        return root.strings
    else:
        return searchTreeForString(root.children[string[0]], string[1:])

