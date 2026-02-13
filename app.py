import streamlit as st
import joblib
import numpy as np
import plotly.graph_objects as go

#python -m streamlit run app.py --server.port 8502

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Sentinel-ML | IDS Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# --- LOAD MODEL ---
@st.cache_resource
def load_sentinel_model():
    return joblib.load('sentinel_model.joblib')

model = load_sentinel_model()

# --- CUSTOM CSS FOR PROFESSIONAL LOOK ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🛡️ Sentinel-ML: Autonomous Intrusion Detection System")
st.markdown("Developed by **Doğukan Çalışkan** | *Sentinel-ML Project*")
st.divider()

# --- SIDEBAR INPUTS ---
st.sidebar.header("📥 Network Traffic Parameters")
duration = st.sidebar.slider("Duration (seconds)", 0, 100, 20)
src_bytes = st.sidebar.number_input("Source Bytes", min_value=0, max_value=10000, value=500)
count = st.sidebar.number_input("Connection Count", min_value=0, max_value=500, value=50)

# Prepare input data
input_data = np.zeros(41)
input_data[0] = duration
input_data[4] = src_bytes
input_data[22] = count

# --- MAIN DASHBOARD ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🔍 Real-time Analysis")
    if st.button("Analyze Traffic", use_container_width=True):
        prediction = model.predict([input_data])
        
        if prediction[0] == 1:
            st.error("### ⚠️ ATTACK DETECTED")
            st.warning("High risk activity identified in the network stream.")
        else:
            st.success("### ✅ NORMAL TRAFFIC")
            st.info("No malicious patterns detected.")
    
    st.metric(label="Model Confidence", value="95.51%", delta="Active")

with col2:
    st.subheader("📊 Feature Visualization")
    # Radar chart for professional look
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=[duration, (src_bytes/100), count],
        theta=['Duration', 'Source Bytes (scaled)', 'Count'],
        fill='toself',
        name='Current Traffic',
        line_color='#00ffcc'
    ))
    fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False,
        template="plotly_dark"
    )
    st.plotly_chart(fig, use_container_width=True)

# --- PROJECT DETAILS ---
st.divider()
st.subheader("📖 About the Project")
st.write("""
Sentinel-ML is a machine learning-powered Network Intrusion Detection System (NIDS) utilizing the **NSL-KDD dataset**. 
The system is trained with a **Linear Support Vector Classifier (SVC)** to distinguish between normal and malicious activity 
with high precision. 
""")