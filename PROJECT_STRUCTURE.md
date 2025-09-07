# Project Structure Overview

```
Phishing-Web-Sites-Detection-Using-Machine-Learning/
│
├── 📁 Core Application Files
│   ├── app.py                 # Main Flask web application
│   ├── feature.py             # Feature extraction engine (30 features)
│   └── config.py              # Configuration and constants
│
├── 📁 Machine Learning
│   ├── train_model.py         # Model training script
│   ├── phishing.csv           # Training dataset (11,054 samples)
│   └── Phishing URL Detection.ipynb  # Jupyter notebook for analysis
│
├── 📁 Web Interface
│   ├── templates/
│   │   └── index.html         # Main web page template
│   └── static/
│       ├── styles.css         # Custom styling
│       └── img/               # Background images
│
├── 📁 Testing & Validation
│   ├── test_urls.py           # URL testing script
│   └── pickle/                # Trained model storage
│       └── model.pkl          # Saved ML model
│
├── 📁 Documentation
│   ├── README.md              # Comprehensive project guide
│   ├── PROJECT_STRUCTURE.md   # This file
│   └── Procfile               # Heroku deployment configuration
│
└── 📁 Dependencies
    └── requirements.txt        # Python package requirements
```

## File Descriptions

### Core Application Files
- **`app.py`**: Flask web server that handles URL submissions and returns phishing detection results
- **`feature.py`**: Core engine that extracts 30 features from URLs for machine learning analysis
- **`config.py`**: Centralized configuration for thresholds, patterns, and system parameters

### Machine Learning Components
- **`train_model.py`**: Script to train the Gradient Boosting Classifier on the phishing dataset
- **`phishing.csv`**: Dataset containing 11,054 URLs with 30 features and labels (safe/phishing)
- **`Phishing URL Detection.ipynb`**: Jupyter notebook for data exploration and model development

### Web Interface
- **`templates/index.html`**: User interface for URL input and results display
- **`static/styles.css`**: Custom styling for the web application
- **`static/img/`**: Background images and visual assets

### Testing & Validation
- **`test_urls.py`**: Command-line tool for testing multiple URLs and validating the system
- **`pickle/model.pkl`**: Serialized trained machine learning model

### Configuration & Deployment
- **`requirements.txt`**: Python package dependencies with version specifications
- **`Procfile`**: Heroku deployment configuration
- **`README.md`**: Comprehensive project documentation and usage guide

## Data Flow

```
User Input URL → Feature Extraction → ML Model → Prediction Result → Web Display
     ↓              ↓              ↓           ↓              ↓
  URL String   30 Features    Model.pkl   Safe/Phishing   Confidence %
```

## Feature Categories

### URL Structure Features (8 features)
- IP address usage, URL length, special characters, subdomains, SSL status

### Domain Analysis Features (6 features)
- Domain age, registration length, DNS records, traffic analysis

### Content Analysis Features (8 features)
- External links, iframes, popups, form handling, right-click disabling

### Behavioral Features (8 features)
- Redirects, status bar customization, Google indexing, PageRank

## Model Architecture

- **Algorithm**: Gradient Boosting Classifier
- **Input**: 30-dimensional feature vector
- **Output**: Binary classification (Safe: 1, Phishing: -1)
- **Performance**: 95%+ accuracy on test data

## Deployment Options

1. **Local Development**: Run `python app.py` for local testing
2. **Heroku**: Use the provided `Procfile` for cloud deployment
3. **Docker**: Containerize the application for consistent deployment
4. **Production Server**: Deploy on AWS, GCP, or other cloud platforms

## Development Workflow

1. **Setup**: Install dependencies with `pip install -r requirements.txt`
2. **Training**: Run `python train_model.py` to create the ML model
3. **Testing**: Use `python test_urls.py` to validate the system
4. **Development**: Run `python app.py` for local web interface
5. **Deployment**: Use appropriate deployment method for production
