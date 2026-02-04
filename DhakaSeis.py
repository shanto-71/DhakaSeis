import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="DhakaSeis Pro", page_icon="🏗️", layout="wide")

st.title("🏗️ DhakaSeis: AI-Driven Urban Resilience")
st.subheader("Advanced BNBC 2020 Seismic Hazard Analysis")

# 1. Engineering Data
zone_map = {"Dhaka (Z=0.20)": 0.20, "Chittagong (Z=0.28)": 0.28, "Sylhet (Z=0.36)": 0.36, "Khulna (Z=0.12)": 0.12}
soil_params = {
    "SA (Hard Rock)": {"S": 1.0, "TB": 0.05, "TC": 0.25, "TD": 1.2},
    "SB (Rock)": {"S": 1.2, "TB": 0.05, "TC": 0.35, "TD": 1.2},
    "SC (Very Dense Soil)": {"S": 1.15, "TB": 0.10, "TC": 0.45, "TD": 1.5},
    "SD (Stiff Soil)": {"S": 1.35, "TB": 0.20, "TC": 0.85, "TD": 2.0}
}

# 2. Sidebar
st.sidebar.header("Input Parameters")
location = st.sidebar.selectbox("Location", list(zone_map.keys()))
soil = st.sidebar.selectbox("Soil Type", list(soil_params.keys()))
z = zone_map[location]
p = soil_params[soil]

# 3. Spectrum Calculation
periods = np.linspace(0, 4, 100)
sa_values = []
for T in periods:
    # Simplified BNBC Spectrum Logic
    if T <= p['TB']: sa = z * p['S'] * (1 + (T/p['TB']) * 1.5)
    elif T <= p['TC']: sa = z * p['S'] * 2.5
    else: sa = (z * p['S'] * 2.5) * (p['TC'] / T)
    sa_values.append(sa)

# 4. Display Metrics
c1, c2, c3 = st.columns(3)
c1.metric("Zone Coefficient (Z)", z)
c2.metric("Soil Factor (S)", p['S'])
c3.metric("Peak Sa (g)", round(max(sa_values), 3))

# 5. Plotting the Spectrum
st.write("### Design Response Spectrum")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(periods, sa_values, color='#ff4b4b', linewidth=2)
ax.set_xlabel("Period T (sec)")
ax.set_ylabel("Spectral Acceleration Sa (g)")
ax.grid(True, linestyle='--', alpha=0.6)
st.pyplot(fig)

st.info(f"This curve represents the elastic response spectrum for {location} on {soil} site conditions.")