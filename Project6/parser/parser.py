import nltk
import sys

TERMINALS = """
Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
Adv -> "down" | "here" | "never"
Conj -> "and" | "until"
Det -> "a" | "an" | "his" | "my" | "the"
N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
N -> "smile" | "thursday" | "walk" | "we" | "word"
P -> "at" | "before" | "in" | "of" | "on" | "to"
V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
V -> "smiled" | "tell" | "were"
"""

NONTERMINALS = """
S -> N V
S -> NP VP
S -> S Conj S
S -> S Conj VP
S -> NP VP Conj VP
NP -> N | Det N | Det AP N | Det N PP | Det AP N PP | Det N PP PP
NP -> Det AP N PP PP | Det AP N PP | Det AP N PP PP | Det AP N PP PP
VP -> V | V NP | V PP | V NP PP | V PP PP | V NP PP PP
VP -> Adv VP | VP Adv | VP Adv PP | VP Adv PP PP
VP -> VP Conj VP | VP Conj VP PP | VP Conj VP PP PP
AP -> Adj | Adj AP
PP -> P NP | P S | P NP PP | P S PP
"""

grammar = nltk.CFG.fromstring(NONTERMINALS + TERMINALS)
parser = nltk.ChartParser(grammar)


def main():

    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)

    # Attempt to parse sentence
    try:
        trees = list(parser.parse(s))
    except ValueError as e:
        print(e)
        return
    if not trees:
        print("Could not parse sentence.")
        return

    # Print each tree with noun phrase chunks
    for tree in trees:
        tree.pretty_print()

        print("Noun Phrase Chunks")
        for np in np_chunk(tree):
            print(" ".join(np.flatten()))


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    # return list of words
    ret = []
    # use nltk to tokenize sentence
    for word in nltk.word_tokenize(sentence):
        # check if word is alphabetic
        if word.isalpha():
            # add word to return list
            ret.append(word.lower())
    
    return ret


def np_chunk(tree):
    """
    Return a list of all noun phrase chunks in the sentence tree.
    A noun phrase chunk is defined as any subtree of the sentence
    whose label is "NP" that does not itself contain any other
    noun phrases as subtrees.
    """
    # return list of noun phrase chunks
    ret = []
    # iterate through subtrees of tree
    for subtree in tree.subtrees():
        # check if subtree is a noun phrase chunk
        if subtree.label() == "NP" and not any(subtree.label() == "NP" for subtree in subtree.subtrees()):
            # add subtree to return list
            ret.append(subtree)

    return ret


if __name__ == "__main__":
    main()
