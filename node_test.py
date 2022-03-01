from node import Node
import parser

def test_emptyNode():
    n = Node()
    assert n.parent == None
    assert len(n.children) == 0
    assert len(n.strings) == 0

def test_checkIsChild():
    n = Node()
    n.children["a"] = Node()
    assert n.checkIsChild("a")

def test_getDictEmpty():
    n = Node()

    assert len(n.getDict()["strings"]) == 0
    assert len(n.getDict()["children"]) == 0

def test_getDictAfterInsertList():
    lines = ["abc", "abcd"]
    root = parser.makeSearchTreeFromLines(lines)
    res = root.getDict()

    assert "abc" in res["strings"]
    assert "abc" in res["children"]["a"]["strings"]
    assert "abc" in res["children"]["a"]["children"]["b"]["strings"]
    assert "abc" in res["children"]["a"]["children"]["b"]["children"]["c"]["strings"]
    assert "abc" in res["children"]["b"]["children"]["c"]["strings"]
    assert "abc" in res["children"]["c"]["strings"]
    assert "abc" in res["children"]["b"]["strings"]
    assert "abc" in res["children"]["c"]["strings"]

def test_superLongLines():
    lines = ["abcd", "z" * 5000]
    root = parser.makeSearchTreeFromLines(lines)
    res = root.getDict()
    assert True