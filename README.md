# Indian Intercity Bus Route Analysis Using NetworkX & Random Forest

This project analyzes intercity bus routes in India using **graph theory** and **NetworkX** for network analysis, combined with **Random Forest** to predict non-connected routes. It also includes **exploratory data analysis (EDA)** and a **Streamlit app** for interactive deployment of the predictive model.

---

## Features
- Analyze bus networks using **NetworkX**  
- Predict non-connected or missing routes using **Random Forest**  
- Conduct **Exploratory Data Analysis (EDA)** on bus routes and connectivity  
- Deploy trained models via **Streamlit** for interactive use  
- Visualizations of network structure, predicted routes, and travel patterns  

---

## Repository Structure

| File / Folder | Description |
|---------------|-------------|
| `.ipynb_checkpoints/` | Jupyter notebook checkpoints |
| `bus_route_analysis.ipynb` | Notebook for EDA, network analysis, and Random Forest modeling |
| `missing_route_analyser.pkl` | Trained Random Forest model (tracked with Git LFS) |
| `*.csv` | Dataset files containing bus routes and schedules |
| `network_analysis.py` | Script for network analysis and route prediction |
| `streamlit_app.py` | Streamlit application for interactive predictions |
| `images/` | Optional images or visualizations |
| `.streamlit/secrets.toml` | Optional: contains API keys if Streamlit app is used |

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/gayathri-g-murali/indian-intercity-bus-route-analysis-networkx-ml.git
