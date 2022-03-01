import sys


class Node:
    def __init__(self, depth:int=0) -> None:
        self.parent = None
        self.children = dict()
        self.strings = list()
        self.depth = 0

    def checkIsChild(self, string: str) -> bool:
        return self.children.get(string) is not None

    def getDict(self):
        # Catch recursion errors if we go to deep, then try again with a deeper recursion limit
        recursionLimit = sys.getrecursionlimit()  # Save old recursion limit
        while True:
            try:
                ret = self.__getDict()  # Try to get dict recursively
                sys.setrecursionlimit(recursionLimit)  # Set recursion limit back to old value
                return ret
            except RecursionError as e:
                print(f"Recursion Limit Reached in getDict: {sys.getrecursionlimit()}\nDoubling Limit")
                sys.setrecursionlimit(sys.getrecursionlimit() * 2)

    def __getDict(self):
        children = dict()

        for k in self.children.keys():
            children[k] = self.children[k].__getDict()

        return {"strings":self.strings, "children":children}
