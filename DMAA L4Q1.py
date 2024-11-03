import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

# Load the dataset
user_data = pd.read_csv('user_data.csv')

# For demonstration, we will classify based on age into categories.
# Create a simple target variable based on age.
user_data['Age_Category'] = pd.cut(user_data['Age'], bins=[0, 30, 40, 50, 60, 70], labels=['Young', 'Adult', 'Middle-Aged', 'Senior', 'Elderly'])

# Prepare the feature set and target variable
X = user_data[['Height', 'Weight']]
Y = user_data['Age_Category']

# Encode categorical labels
le = LabelEncoder()
Y_encoded = le.fit_transform(Y)

# Split the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y_encoded, test_size=0.2, random_state=42)

# Initialize the KNeighbors Classifier
knn = KNeighborsClassifier(n_neighbors=3)

# Fit the model
knn.fit(X_train, Y_train)

# Make predictions
Y_pred = knn.predict(X_test)

print(classification_report(Y_test, Y_pred, target_names=le.classes_, zero_division=1))
accuracy = accuracy_score(Y_test, Y_pred)
report = classification_report(Y_test, Y_pred, target_names=le.classes_)