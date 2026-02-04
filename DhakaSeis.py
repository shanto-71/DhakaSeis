import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="DhakaSeis Pro", page_icon="🏗️", layout="wide")

st.title("🏗️ DhakaSeis: AI-Driven Urban Resilience")
st.subheader("BNBC 2020 Seismic Hazard Analysis & Public Safety")

# 1. Engineering Data
zone_map = {"Dhaka (Z=0.20)": 0.20, "Chittagong (Z=0.28)": 0.28, "Sylhet (Z=0.36)": 0.36, "Khulna (Z=0.12)": 0.12}
soil_params = {
    "SA (Hard Rock)": {"S": 1.0, "TB": 0.05, "TC": 0.25, "TD": 1.2, "desc": "Solid rock foundation."},
    "SB (Rock)": {"S": 1.2, "TB": 0.05, "TC": 0.35, "TD": 1.2, "desc": "Dense rock foundation."},
    "SC (Very Dense Soil)": {"S": 1.15, "TB": 0.10, "TC": 0.45, "TD": 1.5, "desc": "Very dense sand or gravel."},
    "SD (Stiff Soil)": {"S": 1.35, "TB": 0.20, "TC": 0.85, "TD": 2.0, "desc": "Soft/stiff clay. High amplification risk."}
}

# 2. Sidebar
st.sidebar.header("Input Parameters")
location = st.sidebar.selectbox("Location", list(zone_map.keys()))
soil = st.sidebar.selectbox("Soil Type", list(soil_params.keys()))
z = zone_map[location]
p = soil_params[soil]

# 3. Calculations
periods = np.linspace(0, 4, 100)
sa_values = []
for T in periods:
    if T <= p['TB']: sa = z * p['S'] * (1 + (T/p['TB']) * 1.5)
    elif T <= p['TC']: sa = z * p['S'] * 2.5
    else: sa = (z * p['S'] * 2.5) * (p['TC'] / T)
    sa_values.append(sa)
peak_sa = max(sa_values)

# 4. Main Display
col1, col2 = st.columns([2, 1])

with col1:
    st.write("### Design Response Spectrum")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(periods, sa_values, color='#ff4b4b', linewidth=2)
    ax.set_xlabel("Period T (sec)")
    ax.set_ylabel("Spectral Acceleration Sa (g)")
    ax.grid(True, linestyle='--', alpha=0.6)
    st.pyplot(fig)

with col2:
    st.write("### 🏠 Public Safety Guidance")
    
    # Layer 1: Traffic Light System
    if peak_sa < 0.4:
        st.success("🟢 LOW TO MODERATE RISK: Standard building practices are generally sufficient.")
    elif peak_sa < 0.7:
        st.warning("🟡 HIGH RISK: Enhanced structural reinforcement is recommended.")
    else:
        st.error("🔴 EXTREME RISK: Special earthquake-resistant design is MANDATORY.")

    # Layer 2: Soil Explanation
    st.info(f"**Foundation Note:** You are building on **{soil}**. {p['desc']}")

    # Layer 3: Simple Advice
    st.write("**Next Steps for Citizens:**")
    st.markdown("- Verify BNBC 2020 compliance with your engineer.")
    st.markdown("- Check if your building has 'Soft Story' (open ground floor) risks.")