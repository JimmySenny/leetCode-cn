#!/usr/bin/env python3

import collections

"""
可以将字典树理解成一个个相连接的字典，在本题目中可以理解为一层最多有26个节点，
每个节点互不相同
"""

""" cpp 定义
class TrieNode{
    bool isEnd
    TrieNode* next[26]
}
"""

class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        """ Initialize your data structure here.  """
        self.root = TrieNode()

    #def insert(self, word: str) -> None:
    def insert(self, word):
        """ Inserts a word into the trie.  """
        node = self.root
        for c in word:
            node = node.children[c]
        node.isEnd = True

    #def search(self, word: str) -> bool:
    def search(self, word):
        """ Returns if the word is in the trie.  """
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return node.isEnd

    #def startsWith(self, prefix: str) -> bool:
    def startsWith(self, prefix):
        #Returns if there is any word in the trie that starts with the given prefix.
        node = self.root
        for c in prefix:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True
    #def replaceWord(self, s: str) -> str:
    def replaceWord(self, s):
        node = self.root
        ss = ""
        for c in s:
            if c in node.children:
                node = node.children[c]
                ss += c
                print("s,c,ss",s,c,ss)
                if node.isEnd:
                    return ss
            else:
                break
        return s
    def traversalNTreeFlagIter(self,order):
        res = []
        qs = [(0,self.root)]
        while qs:
            if "level" != order:
                flag, cur = qs.pop()
            else:
                flag, cur = qs.pop(0)
            if not cur:
                continue
            if 0 == flag:
                if "pre" == order:
                    if cur.children:
                        i = len(cur.children) - 1
                        while i >= 0:
                            qs.append((0,cur.children[i]))
                            i -= 1
                    qs.append((1,cur))
                if "post" == order:
                    qs.append((1,cur))
                    if cur.children:
                        i = len(cur.children) - 1
                        while i >= 0:
                            qs.append((0,cur.children[i]))
                            i -= 1
                if "level" == order:
                    qs.append((1,cur))
                    if cur.children:
                        for i in range(len(cur.children)):
                            qs.append((0,cur.children[i]))

                        """
                        for node in cur.children:
                            qs.append((0,node))
                        """
            else:
                res.append(cur.children.keys())
        return res

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

def main():
    obj = Trie()
    obj.insert("apple")
    print("search:",obj.search("apple"))
    print("search:",obj.search("banana"))
    print("startsWith:",obj.startsWith("app"))
    print("startsWith:",obj.startsWith("b"))

    print(obj.traversalNTreeFlagIter("pre"))
    print(obj.traversalNTreeFlagIter("post"))
    print(obj.traversalNTreeFlagIter("level"))

if __name__ == '__main__':
    main()