class Trie_Node:
    def __init__(self):


        self.children = [None]*26
        self.isEndString = False


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Trie_Node()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        trie_node = self.root

        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if trie_node.children[index] == None:
                new_node = Trie_Node()
                trie_node.children[index] = new_node
            trie_node = trie_node.children[index]
        trie_node.isEndString = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        #print('in search'+word)
        if len(word) == 0:
            return False
        word_trie = self.root.children[ord(word[0])-ord('a')]
        i = 0
        for i in range(1, len(word)):
            if word_trie is None:
                return False
                #print(word_trie, ord(word[i])-ord('a'))
            word_trie = word_trie.children[ord(word[i])-ord('a')]

        return word_trie != None and word_trie.isEndString and (i+1) == len(word)


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        #print('in startwith'+prefix)
        if len(prefix) == 0:
            return True
        word_trie = self.root.children[ord(prefix[0])-ord('a')]
        i = 0
        for i in range(1, len(prefix)):
            if word_trie is None:
                return False
            word_trie = word_trie.children[ord(prefix[i])-ord('a')]

        return word_trie != None and (i+1) == len(prefix)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)