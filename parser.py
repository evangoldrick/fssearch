from node import Node

def getMaxLengthString(arr: list) -> int:
    longest = 0
    for element in arr:
        if len(element) > longest:
            longest = len(element)

    return longest

def insertStringInTree(root: Node, string: str) -> None:
    root.strings.append(string)
    root.depth

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

def searchTreeForString(root: dict, string:str) -> list:
    print(string, root.strings)
    if len(string) == 0:
        return root.strings
    else:
        return searchTreeForString(root.children[string[0]], string[1:])
