class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {}


class TrieApi:

    def __init__(self):
        self.root  = TrieNode()

    # T = S = O(N)
    def insert(self, word: str) -> None:
        current = self.root

        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]

        current.endOfWord = True

    def searchFullWord(self, word: str) -> bool:

        current = self.root

        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]

        return current.endOfWord

    def startsWith(self, word: str) -> bool:

        current = self.root

        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]


        return True
    
    def delete(self, word: str) -> bool:
        if not self.searchFullWord(word):
            return False # Word doesn't exist; nothing to delete

        def _delete(current: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                current.endOfWord = False
                return len(current.children) == 0

            char = word[index]
            node = current.children.get(char)
            if not node:
                return False

            should_delete = _delete(node, word, index + 1)

            if should_delete:
                del current.children[char]
                return len(current.children) == 0 and not current.endOfWord
            
            return False

        return _delete(self.root, word, 0)

    def printTrie(self, node=None, word=''):
        if node is None:
            node = self.root

        if node.endOfWord:
            print(f'Word: {word}')

        for char, child in node.children.items():
            self.printTrie(child, word + char)
    
# Your Trie object will be instantiated and called as such:
obj = TrieApi()


print('inserts.....')
obj.insert('delete')
obj.insert('delight')
obj.insert('animesh')

print('search full word.....')

param_2 = obj.searchFullWord('delete')
print(param_2)

print('search prefix.....')
param_3 = obj.startsWith('delight')
print(param_3)

print('xx.....')

param_del = obj.delete('delight')
print(param_del)

obj.printTrie()
