import os
from spellchecker import SpellChecker
from nltk.tokenize import RegexpTokenizer
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import brown


def getDataFromFile(fileName):
    cwd = os.getcwd()
    script = os.path.realpath(__file__)
    with open(os.path.join(os.path.dirname(script), fileName), "r") as file:
        data = file.read().replace('\n', '')
    return data


def getRegexTokenizer():
    # Set regex tokenizer to get words from the data
    regexTokenizer = RegexpTokenizer('\W', gaps=True)
    return regexTokenizer

# Custom dictionary using brown corpus which can be used in spellchecker
# def getBrownDictionaryFile():
#     cwd = os.getcwd()
#     script = os.path.realpath(__file__)
#     file = open(os.path.join(os.path.dirname(
#         script), 'myDictionary.txt'), "w+")
#     for w in brown.words():
#         file.write(str(w.lower())+',')
#     file.close()

# getBrownDictionaryFile()


# Used pyspellchecker as it uses a Levenshtein Distance algorithm to find permutations within an edit distance of 2 from the original word.
spell = SpellChecker()

misspelled = []
regexTokenizer = getRegexTokenizer()
data = getDataFromFile("mobydick.txt")

# Get tokenized data using regexTokenizer from the mobydick.txt
tokenWords = regexTokenizer.tokenize(data)
# Get all misspelled words list
misspelled = spell.unknown(tokenWords)

# Listing all the mispelled words and getting suitable alternatives
for word in misspelled:
    correctWord = spell.correction(word)
    # Get a list of `likely` options
    alternatives = list(spell.candidates(word))
    alternatives.remove(correctWord)
    alternatives.insert(0, correctWord)
    print(word, ":", alternatives[:3])

print("done")
