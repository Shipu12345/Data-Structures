class TrieNode:
    def __init__(self) -> None:
        self.children = [None] * 26
        self.is_end_of_word = False


class Trie:
    def __init__(self) -> None:
        self.root = self.get_node()

    def get_node(self) -> TrieNode:
        return TrieNode()

    # Private helper func that converts key current character into index
    def _char_to_index(self, ch) -> int:
        return ord(ch) - ord("a")

    def insert(self, key) -> None:
        current_node = self.root

        for level in range(len(key)):
            index = self._char_to_index(key[level])
            if not current_node.children[index]:
                current_node.children[index] = self.get_node()

            current_node = current_node.children[index]

        current_node.is_end_of_word = True

    def search(self, key) -> bool:
        current_node = self.root

        for level in range(len(key)):
            index = self._char_to_index(key[level])
            if not current_node.children[index]:
                return False

            current_node = current_node.children[index]

        return current_node.is_end_of_word


def main():
    keys = ["the", "a", "there", "anaswe", "any", "by", "their"]
    output = ["Not present in trie", "Present in trie"]

    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))


if __name__ == "__main__":
    main()


# Complexity:  Time         Space

# insertion->   O(n)         O(n*m)
# search->      O(n)         O(1)
