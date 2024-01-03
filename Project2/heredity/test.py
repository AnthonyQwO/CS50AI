import csv
import itertools
import sys

PROBS = {

    # Unconditional probabilities for having gene
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability
    "mutation": 0.01
}


def main():
    people = {
            'Harry': {'name': 'Harry', 'mother': 'Lily', 'father': 'James', 'trait': None},
            'James': {'name': 'James', 'mother': None, 'father': None, 'trait': True},
            'Lily': {'name': 'Lily', 'mother': None, 'father': None, 'trait': False}
            }


    print(joint_probability(people, {"Harry"}, {"James"}, {"James"}))


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]


def inherit_probability(person, one_gene, two_genes):
    """
    Compute and return the probability that `person` inherited zero, one, or
    two genes from their parents, based on how many genes their parents
    passed down.
    """
    if person in two_genes:
        return 1 - PROBS["mutation"]
    elif person in one_gene:
        return 0.5 # 0.5 * (1 - PROBS["mutation"]) + 0.5 * PROBS["mutation"] = 0.5
    return PROBS["mutation"]

def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    ret = 1 
    
    for person in people:
        # Determine how many genes the person has
        if person in one_gene:
            genes = 1
        elif person in two_genes:
            genes = 2
        else:
            genes = 0
        
        # Determine the probability of the person having the gene
        if people[person]["mother"] == None and people[person]["father"] == None:
            ret *= PROBS["gene"][genes]
        else:
            father = inherit_probability(people[person]["father"], one_gene, two_genes)
            mother = inherit_probability(people[person]["mother"], one_gene, two_genes)
            if genes == 2:
                ret *= father * mother
            elif genes == 1:
                ret *= (father * (1 - mother) + mother * (1 - father))
            else:
                ret *= (1 - father) * (1 - mother)
            
        # Determine the probability of the person having the trait
        ret *= PROBS["trait"][genes][person in have_trait]
            
    return ret


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    raise NotImplementedError


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
