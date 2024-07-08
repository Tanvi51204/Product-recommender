# Product Recommendation System

This project is a content-based product recommendation system built using Python and Streamlit. The system recommends products based on their tags and descriptions using TF-IDF vectorization and cosine similarity.

## Features

- Load and preprocess product data
- Compute similarity between products using TF-IDF vectorization and cosine similarity
- Provide recommendations based on user-selected products
- Interactive web interface with Streamlit

## Installation

1. **Clone the repository**:
   ```sh
   git clone 
   cd product-recommendation-system

2. **Create a virtual environment and activate it**:
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3.  **Install the required packages**:
   pip install -r requirements.txt

4. **Run the streamlit app**:
   streamlit run app.py
