# IBM Applied Data Science Capstone: SpaceX Falcon 9 Landing Prediction

Welcome to my repository for the **IBM Applied Data Science Capstone** project! This capstone project concludes the IBM Data Science Professional Certificate, focusing on predicting whether the first stage of a SpaceX Falcon 9 rocket will successfully land[cite: 1].

---

## Project Overview

SpaceX promotes reusable rockets as a cost-saving measure, with Falcon 9 first-stage landings being a key component. The primary goal of this project is to analyze launch data, determine the factors influencing successful landings, and build a machine learning model to predict landing outcomes.

---

## Project Structure & Files

The repository is organized into a step-by-step data science pipeline:

* **`01_SpaceX_API_Data_Collection.py`**: Gathers launch data directly from the SpaceX REST API[cite: 1].
* **`02_Web_Scraping.py`**: Scrapes Falcon 9 launch records and historical data from Wikipedia[cite: 1].
* **`03_Data_Wrangling.py`**: Cleans, formats, and prepares the collected data for analysis and machine learning[cite: 1].
* **`04_EDA_Data_Visualization.py`**: Performs exploratory data analysis (EDA) using matplotlib and seaborn to visualize launch trends[cite: 1].
* **`05_EDA_SQL.py`**: Analyzes the dataset using SQL queries to extract key insights regarding payload mass, launch sites, and success rates[cite: 1].
* **`06_Folium_Interactive_Map.py`**: Maps launch sites and launch outcomes geographically using Folium[cite: 1].
* **`07_Plotly_Dash_Dashboard.py`**: Implements an interactive Plotly Dash web application for exploring launch success analytics[cite: 1].
* **`08_Predictive_Analysis.py`**: Trains and evaluates multiple machine learning classification models (Logistic Regression, SVM, Decision Tree, KNN) to predict first-stage landing success[cite: 1].
* **`requirements.txt`**: Lists all necessary Python dependencies and libraries needed to run the scripts[cite: 1].
* **`GITHUB_UPLOAD_GUIDE.md`**: Instructions and guidelines for repository management and version control[cite: 1].

---

## Methodology & Pipeline

1. **Data Collection**: Sourced raw data via the SpaceX API and web scraping[cite: 1].
2. **Data Wrangling & EDA**: Standardized variables, handled missing values, engineered features (like creating landing outcome binary labels), and ran SQL queries[cite: 1].
3. **Visualization & Dashboards**: Built geographic maps with Folium and an interactive dashboard using Plotly Dash to present key performance indicators[cite: 1].
4. **Predictive Modeling**: Split data into training and test sets, applied feature scaling, tuned hyperparameters via GridSearchCV, and evaluated model performance[cite: 1].

---

## Getting Started

To run the code locally, clone the repository and install the required dependencies:

```bash
git clone [https://github.com/ZikhonaManga/IBM-Applied-Data-Science-Capstone.git](https://github.com/ZikhonaManga/IBM-Applied-Data-Science-Capstone.git)
cd IBM-Applied-Data-Science-Capstone
pip install -r requirements.txt
