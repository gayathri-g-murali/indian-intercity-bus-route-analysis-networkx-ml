import streamlit as st
import pandas as pd
import joblib
import networkx as nx

# ===============================
# Load trained model + scaler
# ===============================
rf_model = joblib.load("missing_route_analyser.pkl")
scaler = joblib.load("scaler.pkl")

# Load dataset
data = pd.read_csv("Pan-India_Bus_Routes.csv")

# Build graph for degree centrality
G = nx.Graph()
for idx, row in data.iterrows():
    G.add_edge(row['Departure'], row['Arrival'], distance=row['Distance'])
centrality = nx.degree_centrality(G)

# ===============================
# Streamlit Layout
# ===============================
st.set_page_config(page_title="🚌✨ Smart Bus Route Optimizer", layout="wide")

st.markdown(
    "<h1 style='text-align:center; color:#2c3e50;'>🚌✨ Smart Bus Route Optimizer</h1>",
    unsafe_allow_html=True
)

st.markdown("This tool uses **Machine Learning + Graph Theory** to detect **under-served or missing intercity bus routes** in India.")

# ===============================
# Summary Cards
# ===============================
col1, col2, col3, col4 = st.columns(4)
avg_distance = round(data['Distance'].mean(),2)
unique_cities = data['Departure'].nunique() + data['Arrival'].nunique()
unique_operators = data['Operator'].nunique()
total_routes = len(data)

cards = [
    ("📏 Avg Distance", f"{avg_distance} km", "#1E88E5"),
    ("🏙️ Total Cities", f"{unique_cities}", "#D81B60"),
    ("🚌 Operators", f"{unique_operators}", "#F4511E"),
    ("🛣️ Total Routes", f"{total_routes}", "#43A047")
]

for col, (title, value, color) in zip([col1,col2,col3,col4], cards):
    col.markdown(
        f"""
        <div style='background-color:{color}; padding:20px; border-radius:12px; text-align:center;'>
            <h4 style='color:white;'>{title}</h4>
            <p style='color:white; font-size:20px; font-weight:bold;'>{value}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

# ===============================
# User Inputs (Dropdown for cities)
# ===============================
st.subheader("🔍 Enter Route Details")

cities = sorted(list(set(data['Departure']).union(set(data['Arrival']))))

col1, col2 = st.columns(2)
with col1:
    from_city = st.selectbox("🏙️ From City", cities)
    distance_input = st.number_input("📏 Distance (km)", min_value=10.0, max_value=2000.0, value=300.0)
with col2:
    to_city = st.selectbox("🏙️ To City", cities)

# ===============================
# Prediction Logic
# ===============================
if st.button("🚀 Predict Route Viability"):

    # Degree centrality features from graph
    deg_u = centrality.get(from_city, 0)
    deg_v = centrality.get(to_city, 0)

    # Feature vector as per training
    features = pd.DataFrame([[deg_u, deg_v, distance_input]], columns=['deg_u','deg_v','distance'])
    features_scaled = scaler.transform(features)

    # Predict probability
    prob = rf_model.predict_proba(features_scaled)[:,1][0]

    # ===============================
    # Display Result
    # ===============================
    if prob > 0.7:
        box_color = "#C62828"  # dark red
        result_text = "⚠️ Likely under-served or missing route!"
    else:
        box_color = "#2E7D32"  # dark green
        result_text = "✅ Route seems well-connected."

    st.markdown(
        f"""
        <div style='background-color:{box_color}; padding:25px; border-radius:12px; text-align:center; margin-top:15px;'>
            <h2 style='color:white;'>🔮 Missing Route Probability: {prob*100:.2f}%</h2>
            <p style='color:white; font-size:18px;'>{result_text}</p>
            <p style='color:white; font-size:16px;'>From: {from_city} → To: {to_city} | Distance: {distance_input} km</p>
        </div>
        """,
        unsafe_allow_html=True
    )
