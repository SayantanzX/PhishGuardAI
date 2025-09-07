#!/usr/bin/env python3
"""
Test script for Phishing Website Detection
Tests the system with various URLs to validate functionality
"""

import pickle
import numpy as np
from feature import FeatureExtraction

def test_url(url, model_path="pickle/model.pkl"):
    """Test a single URL with the trained model"""
    try:
        # Load the model
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        
        # Extract features
        obj = FeatureExtraction(url)
        features = obj.getFeaturesList()
        
        # Make prediction
        x = np.array(features).reshape(1, 30)
        prediction = model.predict(x)[0]
        probability = model.predict_proba(x)[0]
        
        # Interpret results
        if prediction == 1:
            result = "SAFE"
            confidence = probability[1] * 100
        else:
            result = "PHISHING"
            confidence = probability[0] * 100
        
        return {
            'url': url,
            'result': result,
            'confidence': confidence,
            'features': features
        }
        
    except Exception as e:
        return {
            'url': url,
            'error': str(e)
        }

def main():
    """Test multiple URLs"""
    print("=" * 60)
    print("PHISHING WEBSITE DETECTION - TESTING")
    print("=" * 60)
    
    # Test URLs (mix of safe and potentially suspicious)
    test_urls = [
        "https://www.google.com",
        "https://www.github.com",
        "https://www.microsoft.com",
        "https://www.apple.com",
        "https://www.amazon.com",
        "https://www.facebook.com",
        "https://www.twitter.com",
        "https://www.linkedin.com",
        "https://www.youtube.com",
        "https://www.netflix.com"
    ]
    
    print(f"Testing {len(test_urls)} URLs...\n")
    
    for url in test_urls:
        print(f"Testing: {url}")
        result = test_url(url)
        
        if 'error' in result:
            print(f"  Error: {result['error']}")
        else:
            print(f"  Result: {result['result']}")
            print(f"  Confidence: {result['confidence']:.2f}%")
        
        print("-" * 40)
    
    print("\nTesting completed!")

if __name__ == "__main__":
    main()
