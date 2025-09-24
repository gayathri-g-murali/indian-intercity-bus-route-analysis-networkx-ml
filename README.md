# 🚍 Indian Intercity Bus Route Analysis Using NetworkX & Random Forest

![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-1.5-lightblue?style=flat-square&logo=pandas&logoColor=white)
![NetworkX](https://img.shields.io/badge/NetworkX-2.x-lightgrey?style=flat-square&logo=graphviz&logoColor=blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-0.24-lightgrey?style=flat-square&logo=scikitlearn&logoColor=orange)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat-square&logo=jupyter&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-deployed-red?style=flat-square&logo=streamlit&logoColor=white)

---

## 🌟 Project Overview
This project performs **analysis and prediction on intercity bus networks in India**. Using **graph theory** and **NetworkX**, it analyzes bus connectivity, while **Random Forest** predicts missing or non-connected routes. The workflow also includes **Exploratory Data Analysis (EDA)** and a **Streamlit app** for interactive visualization and deployment.  

> This repository helps planners, data scientists, and transport analysts understand network gaps and improve route planning efficiently.

---

## 🚀 Key Features
- **🕸 Network Analysis:** Explore bus networks using NetworkX graph algorithms  
- **🔮 Predictive Modeling:** Random Forest to predict missing or non-connected routes  
- **📊 Exploratory Data Analysis:** Visualize bus routes, travel patterns, and network metrics  
- **💻 Interactive Deployment:** Streamlit app to visualize network and predicted routes  
- **🖼 Visual Insights:** Network graphs, heatmaps, and route maps  

---

## 📂 Repository Structure

| File / Folder | Description |
|---------------|-------------|
| `.ipynb_checkpoints/` | Jupyter notebook checkpoints |
| `bus_route_analysis.ipynb` | Notebook for EDA, network analysis, and Random Forest modeling |
| `missing_route_analyser.pkl` | Trained Random Forest model (**tracked with Git LFS** due to size) |
| `*.csv` | Dataset files containing bus routes and schedules |
| `network_analysis.py` | Script for network analysis and route prediction |
| `streamlit_app.py` | Streamlit application for interactive predictions |
| `images/` | Visualizations and plots |
| `.streamlit/secrets.toml` | Optional: contains API keys if Streamlit app uses external services |

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/gayathri-g-murali/indian-intercity-bus-route-analysis-networkx-ml.git
