# traffic

This Python script implements a Convolutional Neural Network (CNN) for Traffic Sign Recognition using the TensorFlow and OpenCV libraries. The project aims to classify images of traffic signs into 43 different categories. Below is a brief overview of the key components of the script:

### Code Structure

1. **Imports:**
   - Imports necessary libraries, including OpenCV, NumPy, TensorFlow, and scikit-learn.

2. **Constants:**
   - Defines constants such as the number of epochs, image dimensions, the number of categories, and test size.

3. **Main Function:**
   - Processes command-line arguments, loads image data, splits it into training and testing sets, and trains a CNN model.

4. **Load Data Function:**
   - Loads image data from the specified directory, assuming a directory structure with subdirectories named after each category.

5. **Get Model Function:**
   - Constructs a CNN model with convolutional layers, max-pooling, dropout, and dense layers.

### Model Training

1. **Data Preprocessing:**
   - Resizes images and converts labels to categorical format.

2. **Model Architecture:**
   - Utilizes a CNN architecture with convolutional layers, max-pooling, dropout for regularization, and dense layers.

3. **Compilation:**
   - Compiles the model with the Adam optimizer and categorical cross-entropy loss.

4. **Training:**
   - Fits the model on the training data for a specified number of epochs.

5. **Evaluation:**
   - Evaluates the model on the test set to measure accuracy.

6. **Model Saving:**
   - Optionally saves the trained model to a specified file.

### Conclusion

The script provides a modular and well-organized approach to implement a Traffic Sign Recognition model. Users can experiment with hyperparameters, model architecture, and image data to further optimize performance.

### Usage
```bash
python traffic.py DATASETPATH
```
`DATASETPATH` is your data's path like `gtsrb`

If you want save the model run
```bash
python traffic.py DATASETPATH model.h5
```

### Data Set Link
Download the [Dataset](https://cdn.cs50.net/ai/2023/x/projects/5/gtsrb.zip).

## Table of Experiments

1. [Experiment 0 Summary](#experiment-0-summary)
   - [Result](#result)
   - [Model Architecture](#model-architecture)
   - [Training Results](#training-results)
   - [Considerations](#considerations)

2. [Experiment 1 Summary](#experiment-1-summary)
   - [Result](#result-1)
   - [Model Architecture](#model-architecture-1)
   - [Training Results](#training-results-1)
   - [Considerations](#considerations-1)

3. [Experiment 2 Summary](#experiment-2-summary)
   - [Result](#result-2)
   - [Model Architecture](#model-architecture-2)
   - [Training Results](#training-results-2)
   - [Considerations](#considerations-2)

4. [Experiment 3 Summary](#experiment-3-summary)
   - [Result](#result-3)
   - [Model Architecture](#model-architecture-3)
   - [Training Results](#training-results-3)
   - [Considerations](#considerations-3)

5. [Experiment 4 Summary](#experiment-4-summary)
   - [Result](#result-4)
   - [Model Architecture](#model-architecture-4)
   - [Training Results](#training-results-4)
   - [Considerations](#considerations-4)

6. [Summary of Experiments](#summary-of-experiments)
   - [Conclusion](#conclusion)


## Experiment 0 Summary

### Result
```bash
Epoch 1/10
500/500 [==============================] - 7s 13ms/step - loss: 5.2826 - accuracy: 0.0556
Epoch 2/10
500/500 [==============================] - 6s 13ms/step - loss: 3.5851 - accuracy: 0.0502
Epoch 3/10
500/500 [==============================] - 6s 13ms/step - loss: 3.5334 - accuracy: 0.0524
Epoch 4/10
500/500 [==============================] - 7s 14ms/step - loss: 3.5118 - accuracy: 0.0561
Epoch 5/10
500/500 [==============================] - 7s 13ms/step - loss: 3.5043 - accuracy: 0.0572
Epoch 6/10
500/500 [==============================] - 6s 13ms/step - loss: 3.5008 - accuracy: 0.0567
Epoch 7/10
500/500 [==============================] - 6s 13ms/step - loss: 3.4996 - accuracy: 0.0567
Epoch 8/10
500/500 [==============================] - 7s 15ms/step - loss: 3.4992 - accuracy: 0.0567
Epoch 9/10
500/500 [==============================] - 7s 14ms/step - loss: 3.4988 - accuracy: 0.0567
Epoch 10/10
500/500 [==============================] - 7s 13ms/step - loss: 3.4988 - accuracy: 0.0561
333/333 - 1s - loss: 3.4977 - accuracy: 0.0557 - 1s/epoch - 4ms/step
```

### Model Architecture
- Simple CNN with one convolutional layer, max-pooling, and two dense layers.

### Training Results
- Training Loss: Gradual decrease.
- Training Accuracy: Around 5-6%.

### Considerations
1. Increase model complexity.
2. Experiment with learning rates.
3. Implement data augmentation.
4. Evaluate using precision, recall, and F1 score.
5. Check for class imbalance.


## Experiment 1 Summary

### Result
```bash
Epoch 1/10
500/500 [==============================] - 21s 40ms/step - loss: 10.2321 - accuracy: 0.0820 
Epoch 2/10
500/500 [==============================] - 21s 42ms/step - loss: 2.7796 - accuracy: 0.2828
Epoch 3/10
500/500 [==============================] - 23s 46ms/step - loss: 2.2010 - accuracy: 0.4085
Epoch 4/10
500/500 [==============================] - 20s 41ms/step - loss: 1.8472 - accuracy: 0.4901
Epoch 5/10
500/500 [==============================] - 21s 42ms/step - loss: 1.5965 - accuracy: 0.5502
Epoch 6/10
500/500 [==============================] - 21s 41ms/step - loss: 1.4004 - accuracy: 0.5975
Epoch 7/10
500/500 [==============================] - 23s 46ms/step - loss: 1.2614 - accuracy: 0.6340
Epoch 8/10
500/500 [==============================] - 23s 46ms/step - loss: 1.1751 - accuracy: 0.6602
Epoch 9/10
500/500 [==============================] - 21s 43ms/step - loss: 1.1153 - accuracy: 0.6790
Epoch 10/10
500/500 [==============================] - 20s 41ms/step - loss: 0.9962 - accuracy: 0.7143
333/333 - 2s - loss: 0.5182 - accuracy: 0.8587 - 2s/epoch - 5ms/step
```

### Model Architecture
- Expanded CNN with three hidden layers, each followed by dropout.

### Training Results
- Training Loss: Decreased significantly.
- Training Accuracy: Improved, reaching around 71% by the final epoch.

### Considerations
1. **Model Complexity:** Increased layers, enhancing the model's capacity to capture features.
2. **Learning Rates:** Not explicitly mentioned; consider experimenting with learning rates for optimization.
3. **Dropout Rate:** Applied dropout to mitigate overfitting; tune rates if necessary.

This modified architecture shows improved performance, with higher accuracy. Continue experimenting with hyperparameters for further enhancements.


## Experiment 2 Summary

### Result
```bash
Epoch 1/10
500/500 [==============================] - 23s 44ms/step - loss: 6.2918 - accuracy: 0.1659
Epoch 2/10
500/500 [==============================] - 23s 45ms/step - loss: 2.1247 - accuracy: 0.4100
Epoch 3/10
500/500 [==============================] - 24s 48ms/step - loss: 1.5243 - accuracy: 0.5589
Epoch 4/10
500/500 [==============================] - 23s 46ms/step - loss: 1.1952 - accuracy: 0.6488
Epoch 5/10
500/500 [==============================] - 21s 42ms/step - loss: 0.9676 - accuracy: 0.7127
Epoch 6/10
500/500 [==============================] - 21s 43ms/step - loss: 0.8237 - accuracy: 0.7612
Epoch 7/10
500/500 [==============================] - 21s 42ms/step - loss: 0.7262 - accuracy: 0.7935
Epoch 8/10
500/500 [==============================] - 22s 45ms/step - loss: 0.6574 - accuracy: 0.8159
Epoch 9/10
500/500 [==============================] - 21s 43ms/step - loss: 0.6158 - accuracy: 0.8295
Epoch 10/10
500/500 [==============================] - 21s 41ms/step - loss: 0.5491 - accuracy: 0.8465
333/333 - 2s - loss: 0.2588 - accuracy: 0.9298 - 2s/epoch - 6ms/step
```

### Model Architecture
- Modified CNN with three hidden layers, each followed by dropout. Adjusted dropout rates.

### Training Results
- Training Loss: Decreased significantly.
- Training Accuracy: Improved, reaching around 85% by the final epoch.

### Considerations
1. **Dropout Tuning:** Fine-tuned dropout rates, potentially mitigating overfitting.
2. **Model Capacity:** Expanded layers, enhancing the model's ability to capture complex features.
3. **Learning Rates:** Not explicitly mentioned; consider experimenting with learning rates for optimization.

The adjusted architecture shows improved performance, achieving higher accuracy. Continue tuning hyperparameters for further optimization.


## Experiment 3 Summary

### Result
```bash
Epoch 1/10
500/500 [==============================] - 44s 85ms/step - loss: 6.2089 - accuracy: 0.1491
Epoch 2/10
500/500 [==============================] - 43s 86ms/step - loss: 2.2444 - accuracy: 0.3983
Epoch 3/10
500/500 [==============================] - 43s 86ms/step - loss: 1.6405 - accuracy: 0.5325
Epoch 4/10
500/500 [==============================] - 43s 85ms/step - loss: 1.3094 - accuracy: 0.6281
Epoch 5/10
500/500 [==============================] - 43s 86ms/step - loss: 1.0917 - accuracy: 0.6854
Epoch 6/10
500/500 [==============================] - 43s 86ms/step - loss: 0.9054 - accuracy: 0.7369
Epoch 7/10
500/500 [==============================] - 43s 86ms/step - loss: 0.8292 - accuracy: 0.7579
Epoch 8/10
500/500 [==============================] - 42s 85ms/step - loss: 0.7684 - accuracy: 0.7832
Epoch 9/10
500/500 [==============================] - 42s 84ms/step - loss: 0.7478 - accuracy: 0.8007
Epoch 10/10
500/500 [==============================] - 42s 83ms/step - loss: 0.6574 - accuracy: 0.8182
333/333 - 3s - loss: 0.4117 - accuracy: 0.8875 - 3s/epoch - 9ms/step
```

### Model Architecture
- Further expanded CNN with four hidden layers, each followed by dropout. Increased neuron count in hidden layers.

### Training Results
- Training Loss: Decreased significantly.
- Training Accuracy: Improved, reaching around 82% by the final epoch.

### Considerations
1. **Increased Model Capacity:** Expanded layers and neuron count, potentially increasing the model's capacity to capture intricate patterns.
2. **Dropout Tuning:** Adjusted dropout rates for regularization.
3. **Learning Rates:** Not explicitly mentioned; consider experimenting with learning rates for optimization.

Despite increased capacity, the model's performance did not improve as expected. Consider revisiting the architecture and experimenting with different configurations to achieve better results.


## Experiment 4 Summary

### Result
```bash
Epoch 1/10
500/500 [==============================] - 31s 60ms/step - loss: 7.0535 - accuracy: 0.1946
Epoch 2/10
500/500 [==============================] - 30s 60ms/step - loss: 1.9173 - accuracy: 0.4718
Epoch 3/10
500/500 [==============================] - 29s 59ms/step - loss: 1.4025 - accuracy: 0.6002
Epoch 4/10
500/500 [==============================] - 29s 59ms/step - loss: 1.0974 - accuracy: 0.6807
Epoch 5/10
500/500 [==============================] - 29s 59ms/step - loss: 0.9040 - accuracy: 0.7362
Epoch 6/10
500/500 [==============================] - 29s 58ms/step - loss: 0.8041 - accuracy: 0.7669
Epoch 7/10
500/500 [==============================] - 30s 60ms/step - loss: 0.7443 - accuracy: 0.7912
Epoch 8/10
500/500 [==============================] - 31s 62ms/step - loss: 0.6533 - accuracy: 0.8175
Epoch 9/10
500/500 [==============================] - 30s 60ms/step - loss: 0.6280 - accuracy: 0.8258
Epoch 10/10
500/500 [==============================] - 31s 61ms/step - loss: 0.5756 - accuracy: 0.8390
333/333 - 2s - loss: 0.3058 - accuracy: 0.9161 - 2s/epoch - 7ms/step
```

### Model Architecture
- Modified CNN with increased filter count in the convolutional layer.

### Training Results
- Training Loss: Decreased significantly.
- Training Accuracy: Improved, reaching around 84% by the final epoch.

### Considerations
1. **Filter Count Increase:** Raised the number of filters in the convolutional layer, potentially capturing more complex patterns.
2. **Dropout Tuning:** Adjusted dropout rates for regularization.
3. **Learning Rates:** Not explicitly mentioned; consider experimenting with learning rates for optimization.

The adjusted architecture demonstrates improved performance with increased accuracy. Further hyperparameter tuning may lead to even better results.


## Summary of Experiments

1. **Experiment 1:**
   - Architecture: Three hidden layers with dropout.
   - Accuracy: 71%

2. **Experiment 2:**
   - Architecture: Fine-tuned dropout rates in Experiment 1.
   - Accuracy: 85%

3. **Experiment 3:**
   - Architecture: Increased layers and neuron count.
   - Accuracy: 82%

4. **Experiment 4:**
   - Architecture: Increased filter count in the convolutional layer.
   - Accuracy: 84%

### Conclusion
Experiment 2 achieved the highest accuracy of 85%, indicating that the fine-tuning of dropout rates in a moderately complex model was effective. Further exploration and fine-tuning of hyperparameters may lead to continued improvements in model performance.