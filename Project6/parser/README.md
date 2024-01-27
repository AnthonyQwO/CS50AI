# parser

This Python script utilizes the Natural Language Toolkit (NLTK) to parse sentences and identify noun phrase chunks within them. The script defines a context-free grammar, preprocesses input sentences, and employs a chart parser to generate parse trees. Additionally, the script identifies and prints noun phrase chunks within the parse trees.

## Example Usage

```bash
python parser.py [filename.txt]
```

`[filename.txt]` is a txt file of sentence like `sentences/1.txt`


The script demonstrates natural language processing capabilities, showcasing the parsing of sentences and extraction of noun phrase chunks using NLTK.

### Grammar Rules

The script defines a set of context-free grammar rules for terminals and non-terminals. Terminals represent words in the language, while non-terminals represent syntactic structures.

- **Terminals (`TERMINALS`)**
  - Adjectives (Adj)
  - Adverbs (Adv)
  - Conjunctions (Conj)
  - Determiners (Det)
  - Nouns (N)
  - Prepositions (P)
  - Verbs (V)

- **Non-terminals (`NONTERMINALS`)**
  - Sentence (S)
  - Noun Phrase (NP)
  - Verb Phrase (VP)
  - Adjective Phrase (AP)
  - Prepositional Phrase (PP)

### Main Function (`main`)

The `main` function reads a sentence from either the command-line argument or user input. It then preprocesses the sentence, attempts to parse it using the defined grammar, and prints the parse tree along with identified noun phrase chunks.

### Preprocessing Function (`preprocess`)

The `preprocess` function converts a sentence to a list of lowercase words, excluding any words that do not contain at least one alphabetic character.

### Noun Phrase Chunking Function (`np_chunk`)

The `np_chunk` function identifies and returns a list of all noun phrase chunks in a given sentence tree. A noun phrase chunk is defined as any subtree with the label "NP" that does not contain other noun phrases as subtrees.
