import sys


class Node:
    def __init__(self) -> None:
        self.parent = None
        self.children = dict()
        self.strings = list()

    def checkIsChild(self, string: str) -> bool:
        return self.children.get(string) is not None

    def getDict(self):
        children = dict()

        for k in self.children.keys():
            children[k] = self.children[k].getDict()

        return {"strings":self.strings, "children":children}