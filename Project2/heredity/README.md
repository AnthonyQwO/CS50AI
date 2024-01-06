# heredity

This program is designed to calculate probabilities related to the inheritance of genes and traits in a family based on given data. The program uses a Bayesian network approach to model the relationships between individuals and the probability of having certain genes or traits.

## Program Structure

### Probability Definitions
The program starts by defining a dictionary named `PROBS`, which stores probabilities related to the inheritance of genes and traits. The probabilities include:
- Unconditional probabilities for having a gene (`"gene"`)
- Conditional probabilities for having a trait given the number of genes (`"trait"`)
- Mutation probability (`"mutation"`)

### Main Function (`main()`)
The `main()` function is the entry point of the program. It performs the following steps:
1. Checks for proper command-line usage and exits if incorrect.
2. Loads data from a CSV file using the `load_data()` function.
3. Initializes a dictionary named `probabilities` to store gene and trait probabilities for each person.
4. Iterates over all possible combinations of people who might have a trait (`have_trait`), and people who might have one or two copies of the gene (`one_gene` and `two_genes`).
5. Checks if the current combination violates known information and continues if so.
6. Updates probabilities based on joint probability using the `joint_probability()` and `update()` functions.
7. Normalizes the probabilities to ensure they sum to 1.
8. Prints the results, showing the probability distributions for each person.

### Helper Functions
1. **`load_data(filename)`**: Loads gene and trait data from a CSV file into a dictionary.
2. **`powerset(s)`**: Returns all possible subsets of a set `s`.
3. **`inherit_probability(person, one_gene, two_genes)`**: Computes the probability that a person inherited zero, one, or two genes from their parents.
4. **`genes_number(person, one_gene, two_genes)`**: Returns the number of genes a person has based on the given sets `one_gene` and `two_genes`.
5. **`joint_probability(people, one_gene, two_genes, have_trait)`**: Computes and returns the joint probability based on the given sets of people who have a trait or gene.
6. **`update(probabilities, one_gene, two_genes, have_trait, p)`**: Adds a new joint probability `p` to the `probabilities` dictionary for each person.
7. **`normalize(probabilities)`**: Updates `probabilities` to ensure each probability distribution is normalized.

### Execution
The program is executed only if it is run as the main script (`__name__ == "__main__"`), calling the `main()` function.

## Running the Program
To run the program, use the following command in the terminal:

```
$ python heredity.py DATA.csv
```

Replace `DATA.csv` with the path to your CSV file containing gene and trait data like `data/family0.csv`.

The program calculates and prints the probability distributions for each person in the provided dataset.