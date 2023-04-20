import numpy as np

def calcNeighbors(letters, currentRow, currentCol):
    neighbors = [letters[currentRow + 1][currentCol], letters[currentRow][currentCol], letters[currentRow+1][currentCol+1], letters[currentRow-1][currentCol], letters[currentRow-1][currentCol-1]]
    return neighbors
    
# This will not correctly populate the array with provided charecters 
letters = np.loadtxt("Wordsearch/letters.txt")
# letters = np.array([[]])
# wordBank = []
wordBank = np.loadtxt("Wordsearch/wordbank.txt")
for row in letters:
    for col in row:
        neighbors = calcNeighbors(letters, row, col)
        for charecter in neighbors:
            possibleWords = np.loadtxt("Wordsearch/dictionary.txt")
            for word in wordBank:
                if(str(word).__contains__(charecter)):
                    
