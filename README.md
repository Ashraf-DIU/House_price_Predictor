🏡 House Price Predictor

An end-to-end Machine Learning web application that predicts residential property prices based on various structural features, amenities, and location parameters. Built with Scikit-Learn, FastAPI, Tailwind CSS, and optimized for deployment on Vercel.

📌 Features

Interactive UI Dashboard: Modern, responsive interface with animated numeric transitions, dynamic feature toggles, and live summary cards.

Machine Learning Integration: Linear Regression model trained on real-world housing market data.

Serverless API: Fast API backend running as Vercel Serverless Functions.

Offline / Standalone Fallback: Embedded simulation engine for instant client-side preview when testing static files.

📁 Repository Structure

housing-price-predictor/
├── api/
│   └── index.py            # FastAPI serverless backend route for Vercel
├── model/
│   ├── housing_model.pkl   # Serialized Scikit-Learn model
│   └── model_columns.json  # Saved column layout for feature alignment
├── public/
│   └── index.html          # Main web application dashboard UI
├── Housing.csv             # Kaggle Housing Prices dataset
├── train_model.ipynb       # Jupyter notebook for EDA, preprocessing, and model training
├── vercel.json             # Vercel deployment routing configuration
├── requirements.txt        # Python backend dependencies
└── README.md               # Project documentation


📊 Dataset Information

This project uses the Housing Prices Dataset sourced from Kaggle (Dataset Link).

Features Used:

Numerical: area (sq ft), bedrooms, bathrooms, stories, parking

Binary Categorical: mainroad, guestroom, basement, hotwaterheating, airconditioning, prefarea

Categorical: furnishingstatus (Furnished, Semi-Furnished, Unfurnished)

🚀 Getting Started

1. Prerequisites

Ensure you have Python 3.9+ installed on your machine.

2. Clone the Repository

git clone https://github.com/YOUR_USERNAME/housing-price-predictor.git
cd housing-price-predictor


3. Install Dependencies

pip install -r requirements.txt


4. Train the Model

You can run the training notebook using Jupyter or VS Code:

jupyter notebook train_model.ipynb


Running all cells will generate housing_model.pkl and model_columns.json in the model/ folder.

🌐 Deploying to Vercel

Push your repository to GitHub.

Log in to Vercel and click Add New Project.

Import your GitHub repository.

Keep the default settings and click Deploy.

Vercel will automatically detect vercel.json and deploy your FastAPI backend alongside your static dashboard UI.

🛠 Tech Stack

Frontend: HTML5, Tailwind CSS, Font Awesome, Vanilla JavaScript

Backend: FastAPI, Pydantic, Uvicorn

Machine Learning: Scikit-Learn, Pandas, NumPy, Joblib

Hosting: Vercel (Serverless Functions)

📝 License

This project is open-source and available under the MIT License.
