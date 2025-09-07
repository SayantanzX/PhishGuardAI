#importing required libraries

from flask import Flask, request, render_template
import numpy as np
import pandas as pd
from sklearn import metrics 
import warnings
import pickle
warnings.filterwarnings('ignore')
from feature import FeatureExtraction

# Load the trained model
try:
    with open("pickle/model.pkl", "rb") as file:
        gbc = pickle.load(file)
except FileNotFoundError:
    print("Model file not found. Please run train_model.py first.")
    gbc = None


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if gbc is None:
            return render_template("index.html", xx=-1, error="Model not loaded. Please train the model first.")
        
        url = request.form["url"]
        
        try:
            obj = FeatureExtraction(url)
            x = np.array(obj.getFeaturesList()).reshape(1, 30)
            
            y_pred = gbc.predict(x)[0]
            # 1 is safe, -1 is unsafe
            y_pro_phishing = gbc.predict_proba(x)[0, 0]
            y_pro_non_phishing = gbc.predict_proba(x)[0, 1]
            
            return render_template('index.html', xx=round(y_pro_non_phishing, 2), url=url)
        except Exception as e:
            return render_template("index.html", xx=-1, error=f"Error processing URL: {str(e)}")
    
    return render_template("index.html", xx=-1)


if __name__ == "__main__":
    app.run(debug=True)