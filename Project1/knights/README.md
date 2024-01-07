# knights

This Python program is a solver for a set of logic puzzles involving characters who may be either knights or knaves. Knights always tell the truth, while knaves always lie. The program uses propositional logic to represent the information given in each puzzle and employs a model-checking algorithm to determine the possible identities of the characters.

## Symbols

The program defines symbols for the characters in the puzzles:

- `AKnight`, `AKnave`: Symbols for character A being a knight or a knave.
- `BKnight`, `BKnave`: Symbols for character B being a knight or a knave.
- `CKnight`, `CKnave`: Symbols for character C being a knight or a knave.

## Main Function

The `main` function initializes symbols and knowledge bases for each puzzle, then uses a model-checking algorithm to determine possible character identities. It prints the results for each puzzle.

## Usage
To run the program, execute the script. The output will display the possible identities of characters for each puzzle.
```bash
puzzle.py
```

