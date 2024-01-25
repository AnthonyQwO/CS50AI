# Shopping Classifier

This Python script (`shopping.py`) is a program that reads shopping data from a CSV file, processes it, trains a k-nearest neighbors classifier, and evaluates its performance. The script uses the scikit-learn library for machine learning tasks.

## Program Overview

### Main Function (`main()`)

The `main()` function orchestrates the overall flow of the program. It performs the following steps:

1. **Command-line Argument Check**: Ensures that the program is provided with the correct number of command-line arguments.
2. **Data Loading and Splitting**: Loads shopping data from the specified CSV file, splits it into training and testing sets using the scikit-learn `train_test_split` function.
3. **Model Training and Prediction**: Utilizes the k-nearest neighbors algorithm (`KNeighborsClassifier`) to train a model on the training set and make predictions on the testing set.
4. **Evaluation**: Calculates and prints various metrics, including the number of correct and incorrect predictions, true positive rate, and true negative rate.

### Data Loading Function (`load_data(filename)`)

The `load_data` function reads shopping data from a CSV file and processes it into two lists: `evidence` (features) and `labels` (target variable). The CSV file is assumed to have columns representing various shopping-related features.

### Month-to-Integer Conversion Function (`monthToInt(month)`)

This function converts abbreviated month names to integers. For example, "Jan" is converted to 0, "Feb" to 1, and so on.

### Model Training Function (`train_model(evidence, labels)`)

The `train_model` function takes evidence (features) and labels as input and returns a k-nearest neighbors classifier model trained on the data. The k-neighbors parameter is set to 1 (`n_neighbors=1`).

### Evaluation Function (`evaluate(labels, predictions)`)

The `evaluate` function compares actual labels with predicted labels and calculates sensitivity and specificity. Sensitivity represents the true positive rate, and specificity represents the true negative rate.

## Example Usage

```bash
python shopping.py shopping.csv
```

## Note

The script assumes a specific format for the input CSV file, where each row represents a shopping-related observation with various features and a binary label indicating whether a purchase was made (`Revenue`). The script uses this information to train and evaluate the k-nearest neighbors classifier.