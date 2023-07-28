# Character Frequency Count with Binary Search Tree

## Introduction

This project involves the implementation of a binary search tree (BST) to count the occurrence of characters in a sample text file. The goal is to create a BST class that supports various operations such as adding nodes, finding nodes, and traversing the tree. The project is implemented in Python.

## BST Class

The `BST` class represents a binary search tree and provides the following methods:

- `add(item)`: Add an item to its proper place in the tree. Return the modified tree.
- `find(item)`: Find the matched item in the tree. If the item is not in the tree, raise a `ValueError`.
- `preorder()`: Return a list with the data items in order of preorder traversal.
- `inorder()`: Return a list with the data items in order of inorder traversal.
- `postorder()`: Return a list with the data items in order of postorder traversal.

## Pair Class

The `Pair` class is used to store character-count pairs in the binary search tree. It provides relational methods to compare objects based on character values.

## Usage

To use the BST class for character frequency counting, follow these steps:

1. Create an instance of the `BST` class.
2. Read the sample text file character by character.
3. For each character, check if it is a letter or digit (excluding whitespace and punctuation).
4. Convert the character to lowercase (if it's a letter) for case-insensitive counting.
5. Use the `add()` method of the `BST` class to add the character-count pair to the tree.
6. Use the `find()` method to increment the count if the character is already present in the tree.

## Example

```python
# Import the BST and Pair classes
from bst import BST, Pair

# Create a BST instance
bst = BST()

# Sample text file name
filename = 'sample.txt'

# Read characters from the file and count their occurrences
with open(filename, 'r') as file:
    while True:
        char = file.read(1)
        if not char:
            break

        if char.isalpha() or char.isdigit():
            char = char.lower()
            pair = bst.find(Pair(char))
            if pair:
                pair.count += 1
            else:
                bst.add(Pair(char, 1))

# Print the size, height, and character frequencies
print("Size of the tree:", bst.size())
print("Height of the tree:", bst.height())

print("Character frequencies:")
for node in bst.inorder():
    print(f"Character: {node.letter}, Frequency: {node.count}")
