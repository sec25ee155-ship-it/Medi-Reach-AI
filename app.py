import streamlit as st
import pandas as pd
from pathlib import Path
from screening import assess_risk, SAMPLE_DATA

st.set_page_config(page_title="MediReach AI", page_icon="🩺", layout="centered")
st.title("🩺 MediReach AI")
st.subheader("Smart Preventive Healthcare for Underserved Communities")
st.info("Educational prototype only. This is not a diagnosis or a substitute for professional medical care. Do not enter real patient-identifying information.")

with st.expander("How this demo works"):
    st.write("Enter simulated vital signs and symptoms. A transparent, rule-based demonstration engine shows a screening flag and general next steps. It is not clinically validated.")

st.header("1. Screening inputs")
mode = st.radio("Choose input", ["Enter sample values", "Load a simulated example"], horizontal=True)
if mode == "Load a simulated example":
    example = st.selectbox("Select simulated case", list(SAMPLE_DATA.keys()))
    vals = SAMPLE_DATA[example]
else:
    vals = {"age": 35, "temperature_c": 36.8, "heart_rate": 78, "systolic_bp": 118, "diastolic_bp": 76, "spo2": 98, "symptoms": []}

with st.form("screening_form"):
    age = st.number_input("Age (years)", min_value=0, max_value=120, value=int(vals["age"]))
    c1, c2 = st.columns(2)
    with c1:
        temp = st.number_input("Temperature (°C)", min_value=30.0, max_value=45.0, value=float(vals["temperature_c"]), step=0.1)
        hr = st.number_input("Heart rate (beats/min)", min_value=20, max_value=250, value=int(vals["heart_rate"]))
        sys = st.number_input("Systolic blood pressure (mmHg)", min_value=50, max_value=280, value=int(vals["systolic_bp"]))
    with c2:
        dia = st.number_input("Diastolic blood pressure (mmHg)", min_value=20, max_value=180, value=int(vals["diastolic_bp"]))
        spo2 = st.number_input("Oxygen saturation SpO₂ (%)", min_value=50, max_value=100, value=int(vals["spo2"]))
    symptom_options = ["fever", "cough", "breathlessness", "chest_pain", "fainting", "severe_headache", "vomiting", "weakness"]
    symptoms = st.multiselect("Symptoms (select any that apply)", symptom_options, default=list(vals["symptoms"]))
    submitted = st.form_submit_button("Assess sample")

if submitted:
    result = assess_risk(age, temp, hr, sys, dia, spo2, symptoms)
    st.header("2. Screening result")
    if result["level"] == "High":
        st.error(f"Demo screening flag: {result['level']}")
    elif result["level"] == "Moderate":
        st.warning(f"Demo screening flag: {result['level']}")
    else:
        st.success(f"Demo screening flag: {result['level']}")
    st.write(result["summary"])
    st.markdown("**Suggested next step**")
    st.write(result["guidance"])
    if result["urgent"]:
        st.error("Urgent warning: symptoms or values entered may indicate an emergency. Contact local emergency services or seek immediate medical care. Do not rely on this demo.")
    st.caption("The rules are illustrative only and have not been clinically validated. A low flag does not mean a person is healthy.")

st.divider()
st.header("3. Simulated dataset")
data = pd.DataFrame([
    {"case": name, "age": v["age"], "temperature_c": v["temperature_c"], "heart_rate": v["heart_rate"],
     "systolic_bp": v["systolic_bp"], "diastolic_bp": v["diastolic_bp"], "spo2": v["spo2"],
     "symptoms": ", ".join(v["symptoms"]) or "none"}
    for name, v in SAMPLE_DATA.items()
])
st.dataframe(data, use_container_width=True, hide_index=True)
csv_bytes = data.to_csv(index=False).encode("utf-8")
st.download_button("Download simulated dataset (CSV)", csv_bytes, "simulated_health_data.csv", "text/csv")
st.caption("No real patient data is stored or included in this prototype.")
