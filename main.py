from pathlib import Path
from string import whitespace, punctuation
from bst import BST


class Pair:
    ''' Encapsulate letter,count pair as a single entity.
    
    Realtional methods make this object comparable
    using built-in operators. 
    '''
    def __init__(self, letter, count = 1):
        self.letter = letter.lower()
        self.count = count
    
    def __eq__(self, other):
        return self.letter == other.letter
    
    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'
    
    def __str__(self):
        return f'({self.letter}, {self.count})'

def make_tree():
    bst = BST()

    filename = 'around-the-world-in-80-days-3.txt'
    with open(filename, 'r') as file:
        while True:
            letter = file.read(1)
            if not letter:
                break
            if letter.isspace():
                continue
            if letter.isalpha() or letter.isdigit():
                letter = letter.lower()
                #print(f"Processing {letter}")
                try:
                    pair = bst.find(Pair(letter))
                    pair.count += 1
                except ValueError:
                    bst.add(Pair(letter, 1)) 
    return bst

def main():
    bst = make_tree()
    
    print(bst.size())
    print(bst.is_empty())
    print(bst.height())
    
if __name__ == "__main__":
    main()
