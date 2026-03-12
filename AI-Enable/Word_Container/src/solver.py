"""You'll implement this."""

from typing import List

from word_list import WordList


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        node.word = word
    
    def find_substrings_in_word(self, word):
        """Find all words in the trie that are substrings of the given word."""
        substrings = set()
        
        # Check all possible starting positions in the word
        for i in range(len(word)):
            node = self.root
            # Try to match from position i
            for j in range(i, len(word)):
                char = word[j]
                if char not in node.children:
                    break
                node = node.children[char]
                if node.is_word and node.word != word:  # Don't include the word itself
                    substrings.add(node.word)
        
        return substrings


class Solver:
    def __init__(self, word_list: WordList) -> None:
        self.word_list = word_list

    def find_containers(self) -> List[str]:
        """
        Find all words that contain at least one other word as a substring.

        Returns:
            List of words that contain other words from the list.
            A word cannot contain itself.

        Example:
            ["apple", "app", "banana", "nana"] -> ["apple", "banana"]
            ["cat", "dog", "bird"] -> []
        """
        words = self.word_list.get_words()
        
        # Build trie with all words
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        containers = []
        
        # For each word, check if it contains any other words as substrings
        for word in words:
            substrings = trie.find_substrings_in_word(word)
            if substrings:  # If any substrings found
                containers.append(word)
        
        return containers