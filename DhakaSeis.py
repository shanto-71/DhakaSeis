import streamlit as st

st.set_page_config(page_title="DhakaSeis Assistant", page_icon="🏗️")

st.title("🏗️ DhakaSeis: AI-Driven Urban Resilience")
st.subheader("BNBC-Grounded Structural Triage Prototype")

# User Inputs for Engineering Logic
st.sidebar.header("Building Parameters")
height = st.sidebar.number_input("Building Height (meters)", min_value=0.0, value=15.0)
occupancy = st.sidebar.selectbox("Occupancy Category", ["Standard Residential", "Essential (Hospital/School)", "Hazardous Storage"])

# Mock Logic for Viva Demo
st.write(f"### Current Analysis for {occupancy}")

if height > 20 and occupancy == "Essential (Hospital/School)":
    st.error("⚠️ BNBC Warning: Special Seismic Detailing required for high-rise essential facilities.")
else:
    st.success("✅ Height is within standard limits for this occupancy category.")

st.info("💡 Next Phase: Integrating RAG to fetch specific BNBC 2020 clauses automatically.")