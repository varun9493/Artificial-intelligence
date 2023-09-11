from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Input data
# Each data point is represented as [feature1, feature2, feature3, ..., target]
data = [
    [5.1, 3.5, 1.4, 0.2, 0],  # Iris Setosa
    [4.9, 3.0, 1.4, 0.2, 0],  # Iris Setosa
    [6.3, 2.5, 4.9, 1.5, 1],  # Iris Versicolor
    [6.5, 3.0, 5.2, 2.0, 2],  # Iris Virginica
    # Add more data points here
]

# Separate features and target labels
X = [row[:-1] for row in data]
y = [row[-1] for row in data]

# Create a Decision Tree Classifier
clf = DecisionTreeClassifier()

# Fit the model to the data
clf.fit(X, y)

# New data point for prediction
new_data = [6.0, 3.0, 4.8, 1.8]  # You can change this data point

# Make a prediction using the trained model
prediction = clf.predict([new_data])
# Mapping of target labels
target_labels = ['Iris Setosa', 'Iris Versicolor', 'Iris Virginica']
predicted_label = target_labels[prediction[0]]
print(f"Predicted Label: {predicted_label}")
