"""A small trie used for prefix autocomplete."""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self, words=()):
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, word):
        node = self.root
        for char in word:
            node = node.children.setdefault(char, TrieNode())
        node.is_word = True

    def starts_with(self, prefix):
        """Return all stored words that begin with prefix, in alphabetical order."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        results = []
        self._collect(node, prefix, results)
        return results

    def _collect(self, node, path, results):
        if node.is_word:
            results.append(path)
        for char in sorted(node.children):
            self._collect(node.children[char], path + char, results)
