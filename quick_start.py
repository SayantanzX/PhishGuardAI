#!/usr/bin/env python3
"""
Quick Start Script for Phishing Website Detection Project
Automates the setup and training process
"""

import os
import sys
import subprocess
import time

def print_header():
    """Print project header"""
    print("=" * 60)
    print(" PHISHING WEBSITE DETECTION - QUICK START")
    print("=" * 60)
    print()

def check_python_version():
    """Check if Python version is compatible"""
    print(" Checking Python version...")
    if sys.version_info < (3, 7):
        print(" Python 3.7+ is required. Current version:", sys.version)
        return False
    print(f" Python version: {sys.version}")
    return True

def install_dependencies():
    """Install required Python packages"""
    print("\n Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print(" Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print(" Failed to install dependencies")
        return False

def check_dataset():
    """Check if the dataset exists"""
    print("\n Checking dataset...")
    if os.path.exists("phishing.csv"):
        print(" Dataset found: phishing.csv")
        return True
    else:
        print(" Dataset not found: phishing.csv")
        print("   Please ensure the dataset file is in the project directory")
        return False

def train_model():
    """Train the machine learning model"""
    print("\n Training machine learning model...")
    try:
        subprocess.check_call([sys.executable, "train_model.py"])
        print(" Model training completed!")
        return True
    except subprocess.CalledProcessError:
        print(" Model training failed")
        return False

def check_model():
    """Check if the trained model exists"""
    print("\n🔍 Checking trained model...")
    if os.path.exists("pickle/model.pkl"):
        print(" Trained model found: pickle/model.pkl")
        return True
    else:
        print(" Trained model not found")
        return False

def test_system():
    """Test the system with sample URLs"""
    print("\n Testing system with sample URLs...")
    try:
        subprocess.check_call([sys.executable, "test_urls.py"])
        print(" System testing completed!")
        return True
    except subprocess.CalledProcessError:
        print(" System testing failed")
        return False

def start_web_app():
    """Start the Flask web application"""
    print("\n Starting web application...")
    print("   The application will be available at: http://localhost:5000")
    print("   Press Ctrl+C to stop the server")
    print()
    
    try:
        subprocess.call([sys.executable, "app.py"])
    except KeyboardInterrupt:
        print("\n\n Web application stopped")

def main():
    """Main quick start function"""
    print_header()
    
    # Check Python version
    if not check_python_version():
        return
    
    # Check dataset
    if not check_dataset():
        return
    
    # Install dependencies
    if not install_dependencies():
        return
    
    # Train model
    if not train_model():
        return
    
    # Check model
    if not check_model():
        return
    
    # Test system
    if not test_system():
        return
    
    print("\n" + "=" * 60)
    print(" SETUP COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print("\n Next steps:")
    print("   1. Run 'python app.py' to start the web application")
    print("   2. Open http://localhost:5000 in your browser")
    print("   3. Enter URLs to test for phishing detection")
    print("\n For development:")
    print("   - Edit config.py to customize settings")
    print("   - Modify feature.py to add new features")
    print("   - Use test_urls.py for batch testing")
    
    # Ask if user wants to start the web app
    print("\n" + "=" * 60)
    response = input(" Would you like to start the web application now? (y/n): ").lower().strip()
    
    if response in ['y', 'yes']:
        start_web_app()
    else:
        print("\n Setup complete! Run 'python app.py' when you're ready to start.")

if __name__ == "__main__":
    main()
