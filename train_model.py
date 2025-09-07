#!/usr/bin/env python3
"""
Phishing Website Detection - Model Training Script
This script trains a machine learning model to detect phishing websites
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import pickle
import os

def load_and_prepare_data():
    """Load the phishing dataset and prepare features"""
    print("Loading dataset...")
    data = pd.read_csv("phishing.csv")
    
    # Remove the 'Index' column if it exists
    if 'Index' in data.columns:
        data = data.drop('Index', axis=1)
    
    # Separate features and target
    X = data.drop('class', axis=1)
    y = data['class']
    
    print(f"Dataset shape: {data.shape}")
    print(f"Features: {X.shape[1]}")
    print(f"Target classes: {y.unique()}")
    print(f"Class distribution:\n{y.value_counts()}")
    
    return X, y

def train_model(X, y):
    """Train the Gradient Boosting Classifier"""
    print("\nTraining model...")
    
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Initialize and train the model
    gbc = GradientBoostingClassifier(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=5,
        random_state=42
    )
    
    gbc.fit(X_train, y_train)
    
    # Make predictions
    y_pred = gbc.predict(X_test)
    
    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\nModel Accuracy: {accuracy:.4f}")
    
    # Print detailed classification report
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    # Print confusion matrix
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    return gbc, X_test, y_test, y_pred

def save_model(model):
    """Save the trained model to a pickle file"""
    print("\nSaving model...")
    
    # Create pickle directory if it doesn't exist
    os.makedirs("pickle", exist_ok=True)
    
    # Save the model
    with open("pickle/model.pkl", "wb") as f:
        pickle.dump(model, f)
    
    print("Model saved to pickle/model.pkl")

def main():
    """Main function to execute the training pipeline"""
    print("=" * 50)
    print("PHISHING WEBSITE DETECTION - MODEL TRAINING")
    print("=" * 50)
    
    try:
        # Load and prepare data
        X, y = load_and_prepare_data()
        
        # Train the model
        model, X_test, y_test, y_pred = train_model(X, y)
        
        # Save the model
        save_model(model)
        
        print("\n" + "=" * 50)
        print("TRAINING COMPLETED SUCCESSFULLY!")
        print("=" * 50)
        
    except Exception as e:
        print(f"Error during training: {str(e)}")
        raise

if __name__ == "__main__":
    main()
