from http.client import LineTooLong
import parser
from node import Node


def test_insertANode():
    root = Node()
    parser.insertStringInTree(root, "a")
    assert root.checkIsChild("a")
    assert not root.checkIsChild("b")

def test_insertTwoLetters():
    root = Node()
    parser.insertStringInTree(root, "ab")
    assert root.checkIsChild("a")
    assert root.checkIsChild("b")
    assert "ab" in root.strings
    assert "a" not in root.strings
    assert "b" not in root.strings

    assert root.children["a"].checkIsChild("b")
    assert not root.children["a"].checkIsChild("a")
    assert "ab" in root.children["a"].strings
    assert "a" not in root.children["a"].strings
    assert "b" not in root.children["a"].strings

def test_insertList():
    lines = ["abc", "abcd", "bcd"]
    root = parser.makeSearchTreeFromLines(lines)
    for line in lines:
        for c in line:
            assert root.checkIsChild(c)

    for line in lines:
        assert line in root.strings

    
    


def test_search():
    lines = ["abc", "abcd", "bcd"]
    root = parser.makeSearchTreeFromLines(lines)
    
    for letter in "abcd":
        res = parser.searchTreeForString(root, letter)
        for line in lines:
            if letter in line:
                assert line in res
            else:
                assert line not in res

    
    res = parser.searchTreeForString(root, "abc")
    assert "abc" in res
    assert "abcd" in res
    assert "bcd" not in res

    res = parser.searchTreeForString(root, "bc")
    assert "abc" in res
    assert "abcd" in res
    assert "bcd" in res

    res = parser.searchTreeForString(root, "bcd")
    assert "abc" not in res
    assert "abcd" in res
    assert "bcd" in res
    
    res = parser.searchTreeForString(root, "abcd")
    assert "abc" not in res
    assert "abcd" in res
    assert "bcd" not in res

    """
    testText = check_output(["find", "."])
    with open("tmp/test.txt", "wb") as outFile:
        outFile.write(testText)

    with open("tmp/test.txt", "r") as inFile:
        with open("tmp/test.json", "w") as outFile:
            output = json.dumps(parser.makeSearchTreeFromLines(inFile.readlines()))
            assert output != None
            assert output != ""
            assert output != "{}"
            outFile.write(output)
            """