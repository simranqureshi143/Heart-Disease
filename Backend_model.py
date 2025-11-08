import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
df = pd.read_csv("heart.csv")   # CSV must be in same folder

# Features and Target
X = df.drop("condition", axis=1)   # ✅ target column is 'condition'
y = df["condition"]

# Split data
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42
)

# Model
model = LogisticRegression(max_iter=1000)

# Train
model.fit(x_train, y_train)

# Save model
pickle.dump(model, open("heart_model.pkl", "wb"))

print("✅ Model trained and saved as heart_model.pkl")
 